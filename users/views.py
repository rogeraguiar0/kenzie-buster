from rest_framework.views import APIView, Request, Response, status
from .models import User
from .serializers import UserSerializer

class UserViews(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)