from rest_framework.views import APIView
from rest_framework.response import Response
from transaction.services import TransactionServices
from transaction.serializers import TransactionSerializer


class TransactionListView(APIView):
    service = TransactionServices()
    permission_classes = []
    authentication_classes = []

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
    permission_classes = []
    authentication_classes = []

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