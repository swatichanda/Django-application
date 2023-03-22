from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ('id', 'invoice', 'description', 'quantity', 'unit_price', 'price')

class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True, read_only=True)
    invoice_details = InvoiceDetailSerializer(many=True)

    class Meta:
        model = Invoice
        fields = ('id', 'date', 'invoice_no', 'customer_name', 'details', 'invoice_details')

    def create(self, validated_data):
        invoice_details_data = validated_data.pop('invoice_details')
        invoice = Invoice.objects.create(**validated_data)
        for detail_data in invoice_details_data:
            InvoiceDetail.objects.create(invoice=invoice, **detail_data)
        return invoice
