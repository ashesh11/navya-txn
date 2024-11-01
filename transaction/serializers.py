from rest_framework import serializers


class TransactionSerializer(serializers.Serializer):
    txn_id = serializers.CharField(read_only=True)
    name = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.EmailField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = serializers.DateField()