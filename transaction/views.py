from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from transaction.services import TransactionServices
from transaction.serializers import TransactionSerializer
from transaction.utils import generate_transaction_pdf
from account.permissions import TransactionListViewPermissionHandler, TransactionDetailViewPermissionHandler


class TransactionListView(APIView):
    permission_classes = [TransactionListViewPermissionHandler]
    service = TransactionServices()

    def get(self, request):
        try:
            transactions = self.service.list()
            serializer = TransactionSerializer(transactions, many=True)
            return Response(data={'data': serializer.data}, status=200)
        except Exception as e:
            return Response({'error': e}, status=400)

    def post(self, request):
        try:
            serializer = TransactionSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            transaction = self.service.create(serializer.validated_data)
            data = {'txn_id': transaction.txn_id}
            return Response(data={'data': data}, status=200)
        except Exception as e:
            return Response({'error': e}, status=400)


class TransactionDetailView(APIView):
    service = TransactionServices()
    permission_classes = [TransactionDetailViewPermissionHandler]

    def get(self, request, txn_id):
        try:
            txn = self.service.retrieve(txn_id=txn_id)
            if not txn:
                return Response('No content', status=204)
            serializer = TransactionSerializer(txn)
            return Response(data={'data': serializer.data}, status=200)
        except Exception as e:
            return Response({'error': e}, status=400)

    def put(self, request, txn_id):
        try:
            serializer = TransactionSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.service.update(txn_id=txn_id, data=serializer.validated_data)
            updated_txn = self.service.retrieve(txn_id=txn_id)
            serializer = TransactionSerializer(updated_txn)
            return Response(data={'data': serializer.data}, status=200)
        except Exception as e:
            return Response({'error': e}, status=400)

    def patch(self, request, txn_id):
        try:
            serializer = TransactionSerializer(data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.service.update(txn_id=txn_id, data=serializer.validated_data)
            updated_txn = self.service.retrieve(txn_id=txn_id)
            serializer = TransactionSerializer(updated_txn)
            return Response(data={'data': serializer.data}, status=200)
        except Exception as e:
            return Response({'error': e}, status=400)

    def delete(self, request, txn_id):
        try:
            self.service.delete(txn_id=txn_id)
            return Response(status=200)
        except Exception as e:
            return Response({'error': e}, status=400)
    

class AllTransactionPDFView(APIView):
    service = TransactionServices()

    def get(self, request):
        try:
            txns = self.service.queryset.filter(approve_status='approved')
            if not txns:
                return Response({'error': 'No available/approved transactions to create PDF'}, status=204)
            pdf = generate_transaction_pdf(txns, type='all')
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="transactions.pdf"'
            return response
        except Exception as e:
            return Response({'error': e}, status=400)


class DetailTransactionPDFView(APIView):
    service = TransactionServices()

    def get(self, request, txn_id):
        try:
            txn = self.service.queryset.filter(txn_id=txn_id, approve_status='approved').first()
            if not txn:
                return Response({'error': 'Transaction not available or rejected'}, status=204)
            pdf = generate_transaction_pdf(txn, type='detail')
            if not pdf:
                return Response({'error': 'Unable to create PDF'}, status=400)
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="transactions.pdf"'
            return response
        except Exception as e:
            return Response({'error': e}, status=400)