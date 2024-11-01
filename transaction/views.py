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
        transactions = self.service.list()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(data={'data': serializer.data}, status=200)

    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        transaction = self.service.create(serializer.validated_data)
        data = {'txn_id': transaction.txn_id}
        return Response(data={'data': data}, status=200)


class TransactionDetailView(APIView):
    service = TransactionServices()
    permission_classes = [TransactionDetailViewPermissionHandler]

    def get(self, request, txn_id):
        txn = self.service.retrieve(txn_id=txn_id)
        if not txn:
            return Response('No content', status=204)
        serializer = TransactionSerializer(txn)
        return Response(data={'data': serializer.data}, status=200)

    def put(self, request, txn_id):
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.service.update(txn_id=txn_id, data=serializer.validated_data)
        updated_txn = self.service.retrieve(txn_id=txn_id)
        serializer = TransactionSerializer(updated_txn)
        return Response(data={'data': serializer.data}, status=200)

    def patch(self, request, txn_id):
        serializer = TransactionSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.service.update(txn_id=txn_id, data=serializer.validated_data)
        updated_txn = self.service.retrieve(txn_id=txn_id)
        serializer = TransactionSerializer(updated_txn)
        return Response(data={'data': serializer.data}, status=200)

    def delete(self, request, txn_id):
        self.service.delete(txn_id=txn_id)
        return Response(status=200)
    

class AllTransactionPDFView(APIView):
    service = TransactionServices()
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        txns = self.service.queryset
        pdf = generate_transaction_pdf(txns, type='all')
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="transactions.pdf"'
        return response


class DetailTransactionPDFView(APIView):
    service = TransactionServices()
    permission_classes = []
    authentication_classes = []

    def get(self, request, txn_id):
        txn = self.service.retrieve(txn_id=txn_id)
        pdf = generate_transaction_pdf(txn, type='detail')
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="transactions.pdf"'
        return response