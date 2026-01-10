from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView,ListAPIView, UpdateAPIView
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.decorators import permission_classes
from rest_framework_simplejwt.tokens import RefreshToken,TokenError

from .serializers import (
    UserSerializer, UserRoleUpdateSerializer,
    UserDetailsUpdateWithoutRole
)

from .permissions import IsAdminOnly

User = get_user_model()

# Register
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

# login view
@permission_classes([AllowAny])
class LoginView(APIView):
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'login'
    
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                {"error":"Invalid credential"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        response = Response(
            {"message":"Login successful"},
            status=status.HTTP_200_OK
        )
        response.set_cookie(
            key="access_token",
            value = str(refresh.access_token),
            httponly = True,
            secure = False,
            samesite = "lax",
            max_age=60*10
        )

        response.set_cookie(
            key="refresh_token",
            value = str(refresh),
            httponly = True,
            secure = False,
            samesite = "lax",
            max_age=24*60*60
        )
        return response

# refresh token to generate new access token
class RefreshTokenView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")

        if not refresh_token:
            return Response({"error": "No refresh token"}, status=401)

        try:
            refresh = RefreshToken(refresh_token)
            access_token = refresh.access_token

            new_refresh_token = str(refresh)

        except TokenError:
            response = Response({"error": "Invalid or expired refresh token"}, status=401)
            response.delete_cookie("access_token")
            response.delete_cookie("refresh_token")
            return response

        response = Response({"message": "Token refreshed"})

        response.set_cookie(
            key='access_token',
            value=str(access_token),
            httponly=True,
            secure=False,     
            samesite='Lax',
            max_age=5*60      
        )

        response.set_cookie(
            key='refresh_token',
            value=new_refresh_token,
            httponly=True,
            secure=False,    
            samesite='Lax',
            max_age=24*60*60  
        )

        return response

# only admin can change role (only)
class AdminRoleUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRoleUpdateSerializer
    permission_classes = [IsAuthenticated, IsAdminOnly]

# all user update his own info without role
class UserUpdateView(UpdateAPIView):
    serializer_class = UserDetailsUpdateWithoutRole
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

# only admin view all teacher and student list
class AdminListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminOnly]

    def get_queryset(self):
        current_user = self.request.user

        return User.objects.exclude(id=current_user.id)


# logout
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.COOKIES.get("refresh_token")

        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
            except Exception:
                pass

        response = Response(
            {"message":"Logged out successfully"},
            status=status.HTTP_200_OK
        )

        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")

        return response