from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from api.user.serializers import UserSignUpSerializer, UserActivitySerializer


class UserSignUpView(CreateAPIView):
    serializer_class = UserSignUpSerializer


class UserActivityView(APIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = UserActivitySerializer(user)
        return Response(serializer.data)
