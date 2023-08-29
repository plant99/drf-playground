from django.contrib.auth import authenticate
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from rest_framework_simplejwt.tokens import RefreshToken

from trequser.users.permission import ViewProfileWithJWTUserPermission
from trequser.users.serializers import UserSerializer


class JWTView(APIView):
    def post(self, request):
        user = authenticate(
            request,
            username=request.data["username"],
            password=request.data["password"],
        )
        if user is None:
            return Response(
                {"response": "Incorrect Credentials."}, status=status.HTTP_403_FORBIDDEN
            )
        else:
            token = RefreshToken.for_user(user)
            return Response(
                {"token": str(token), "access_token": str(token.access_token)}
            )


class ProfileView(APIView):
    permission_classes = [ViewProfileWithJWTUserPermission]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return JsonResponse(serializer.data, safe=False)
