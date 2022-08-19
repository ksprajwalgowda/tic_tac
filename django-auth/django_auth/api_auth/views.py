from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import UserSerializer , PasswordSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def helloView(request):
    # print(request.user.username)
    content = {'message': 'Hello, World!'}
    return Response(content)


@api_view(['POST'])
def create_auth(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        get_user_model().objects.create_user(
            serialized.initial_data['username'],
            serialized.initial_data['email'],
            serialized.initial_data['password']
        )
        dic_res = {
            'username':serialized.initial_data['username'],
            'email':serialized.initial_data['email'],
            'password': serialized.initial_data['password']
        }
        return Response(dic_res, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


# {
# "username":"qwe",
# "email":"a@gmail.com",
# "password":"Hype#123"
# }

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def set_password(request):
    serializer = PasswordSerializer(data=request.data)
    user = User.objects.get(username=request.user.username)

    if serializer.is_valid():
        if not user.check_password(serializer.data.get('old_password')):
            return Response({'old_password': ['Wrong password.']}, 
                            status=status.HTTP_400_BAD_REQUEST)
        # set_password also hashes the password that the user will get
        user.set_password(serializer.data.get('new_password'))
        user.save()
        return Response({'status': 'password changed'}, status=status.HTTP_200_OK)

    return Response(serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)