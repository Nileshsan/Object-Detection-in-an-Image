from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Return a list of APIView feature"""
        an_apiview = [
             'Uses HTTP methods as function(get, lost, patch, put, delete)',
             'Is similar to a traditional Django View',
             'Gives you the most control over you application logic',
             'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello!', 'an_apiview': an_apiview})
