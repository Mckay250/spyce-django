import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_api_key.permissions import  HasAPIKey

from rest_framework import viewsets
from .models import Transaction
from .serializers import TransactionSerializer
from .mail_transaction import mail_transaction
# Create your views here.


@api_view(['GET', 'POST'])
@permission_classes([HasAPIKey])
def trans_email(request):
    if request.method == 'GET':
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = {}
        model_data = {}
        email = request.data['email']
        items = request.data['items']
        prices = request.data['prices']
        types = request.data['types']
        links = request.data['links']
        total = request.data['total']
        data['email'] = email
        data['products'] = items
        data['prices'] = prices
        data['types'] = types
        data['links'] = links
        data['total'] = total
        model_data['email'] = email
        model_data['items'] = str(items)
        model_data['prices'] = str(prices)
        model_data['types'] = str(types)
        model_data['links'] = str(links)
        model_data['total'] = total
        serializer = TransactionSerializer(data=model_data)
        if serializer.is_valid():
            serializer.save()
            data['trans_id'] = serializer.data['id']
            mail_transaction(data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([HasAPIKey])
def tran_email(request, pk):
    """
    Retrieve a transaction.
    """
    try:
        snippet = Transaction.objects.get(pk=pk)
    except Transaction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TransactionSerializer(snippet)
        return Response(serializer.data)
