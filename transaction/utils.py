import os
from io import BytesIO
from django.template import loader
from xhtml2pdf import pisa

def generate_transaction_pdf(transaction, type):
    if type == 'detail':
        template = loader.get_template('transaction/detail_txn_template.html')
        context_name = 'transaction'
    elif type == 'all':
        template = loader.get_template('transaction/all_txns_template.html')
        context_name = 'transactions'

    context = {
        context_name: transaction,
        'logo_path': os.path.abspath('logo.jpeg') 
    }

    # Render the template with context
    html = template.render(context)

    buffer = BytesIO()

    # Convert HTML to PDF and store it in the buffer
    pisa.CreatePDF(html, dest=buffer)

    # Reset buffer position to the beginning for reading
    buffer.seek(0)

    return buffer