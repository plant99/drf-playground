
from rest_framework_simplejwt.authentication import JWTAuthentication

class JWTVerificationMiddleware(object):
    def __init__(self, get_response) -> None:
        self.get_response = get_response
        pass

    def __call__(self, request):
        JWT_authenticator = JWTAuthentication()
        try:
            response = JWT_authenticator.authenticate(request)
            if response is not None:
                user , _ = response    
                request.jwt_user = user
            else:
                request.jwt_user = None
        except:
            request.jwt_user = None
        response = self.get_response(request)
        return response

    def process_request(self, request):
        print(request)
        return None