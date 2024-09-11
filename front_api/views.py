from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from front_api import serializers

class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView feature"""
        an_apiview = [
             'Uses HTTP methods as function(get, lost, patch, put, delete)',
             'Is similar to a traditional Django View',
             'Gives you the most control over you application logic',
             'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello!', 'an_apiview': an_apiview})


    def post(self, request):
         """Create hello message with our name """

         serializer = self.serializer_class(data = request.data)

         if serializer.is_valid():
             name = serializer.validated_data.get('name')
             message = f'Hello {name}'
             return Response({'message': message})

         else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )

    def put(self, request, pk=None):
        """handle updateing an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
