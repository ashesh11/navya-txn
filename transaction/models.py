from django.db import models


TRANSACTION_APPROVE_STATUS_CHOICES = [
    ('approved', 'approved'),
    ('rejected', 'rejected')
]
class Transaction(models.Model):
    txn_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateField()
    approve_status = models.CharField(max_length=20, choices=TRANSACTION_APPROVE_STATUS_CHOICES, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.txn_id:
            last_transaction = Transaction.objects.order_by('txn_id').last()
            if last_transaction:
                last_id_number = int(last_transaction.txn_id[5:])  # Strip 'TXNID' prefix
                new_id_number = last_id_number + 1
            else:
                new_id_number = 1
            self.txn_id = f"TXNID{new_id_number:04d}"  # Format with leading zeros

        super().save(*args, **kwargs)
