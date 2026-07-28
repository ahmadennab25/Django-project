from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import User
from ..serializers import UserSerializer


@api_view(["GET"])
def get_users(request):
    users = User.objects.filter(is_active=True)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)