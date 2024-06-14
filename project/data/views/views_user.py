from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from data.models.user import UserModel
from data.serializers.serializers_user import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_user(request):
    # Implement login logic here
    pass

@api_view(['POST'])
def logout_user(request):
    # Implement logout logic here
    pass

@api_view(['PUT'])
def update_profile(request):
    # Implement update profile logic here
    pass