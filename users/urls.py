from django.urls import path

from . import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("users/", views.UserViews.as_view()),
    path("users/<int:user_id>/", views.UserDetailViews.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
    path("users/refresh/", TokenRefreshView.as_view())
]