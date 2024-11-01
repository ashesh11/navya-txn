from django.urls import path
from transaction.views import TransactionListView, TransactionDetailView

urlpatterns = [
    path('transactions/', TransactionListView.as_view(), name='list-txn'),
    path('transactions/<str:txn_id>/', TransactionDetailView.as_view(), name='detail-txn')
]