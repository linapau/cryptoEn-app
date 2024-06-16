from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# a new API endpoint that returns a JSON response with the message
@api_view(['GET'])
def siema(request):
    return Response({'message': 'Hello, world!'}) 