from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    RegisterView,
    LoginView,
    LogoutView,
    RefreshTokenView,
    AdminRoleUpdateView,
    AdminListView,
    UserUpdateView
)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name = "logout"),

    path('token/refresh/', RefreshTokenView.as_view(), name='token_refresh'),

    path('list/', AdminListView.as_view(), name='list'),
    path('role/<int:pk>/', AdminRoleUpdateView.as_view(), name='only-admin'),
    path('info/<int:pk>/', UserUpdateView.as_view(), name='update_user_info')
]
