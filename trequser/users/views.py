from django.contrib.auth import authenticate

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from rest_framework_simplejwt.tokens import RefreshToken

from trequser.users.permission import ViewProfileWithJWTUserPermission


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
        return Response(
            {"first_name": request.user.first_name, "last_name": request.user.last_name}
        )
