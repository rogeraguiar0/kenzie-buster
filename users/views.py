from rest_framework.views import APIView, Request, Response, status

from django.shortcuts import get_object_or_404

# from .permissions import IsUserOwner

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserSerializer

class UserViews(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

class UserDetailViews(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, user_id: int) -> Response:
        find_user = get_object_or_404(User, pk=user_id)

        serializer = UserSerializer(find_user)

        if request.user == find_user or request.user.is_superuser:
            return Response(serializer.data, status.HTTP_200_OK)

        return Response({"detail": "You do not have permission to perform this action."}, 403)

    def patch(self, request: Request, user_id: int) -> Response:
        find_user = get_object_or_404(User, pk=user_id)

        serializer = UserSerializer(find_user, request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        if request.user == find_user or request.user.is_superuser:
            return Response(serializer.data, status.HTTP_200_OK)

        return Response({"detail": "You do not have permission to perform this action."}, 403)