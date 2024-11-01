from transaction.models import Transaction


class TransactionServices:
    def __init__(self):
        self.queryset = Transaction.objects.all()

    def list(self):
        return self.queryset
    
    def create(self, data):
        txn = Transaction.objects.create(**data)
        return txn

    def retrieve(self, txn_id):
        return self.queryset.filter(txn_id=txn_id).first()

    def update(self, txn_id, data):
        txn = self.retrieve(txn_id)
        for field, value in data.items():
            setattr(txn, field, value)
        txn.save()
        return txn

    def delete(self, txn_id):
        txn = self.retrieve(txn_id)
        return txn.delete()