from django.urls import path
from transaction.views import TransactionListView, TransactionDetailView, AllTransactionPDFView, DetailTransactionPDFView

urlpatterns = [
    path('transactions/', TransactionListView.as_view(), name='list-txn'),
    path('transactions/<str:txn_id>/', TransactionDetailView.as_view(), name='detail-txn'),
    path('pdf/transactions/', AllTransactionPDFView.as_view(), name='all-txns-pdf'),
    path('pdf/transactions/<str:txn_id>/', DetailTransactionPDFView.as_view(), name='one-txn-pdf'),
]