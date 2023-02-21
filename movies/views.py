from rest_framework.views import APIView, Request, Response, status

from .models import Movie
from .serializers import MovieSerializer, MovieOrderSerializer

from users.permissions import IsAdminOrReadOnly

from django.shortcuts import get_object_or_404

from rest_framework.pagination import PageNumberPagination

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class MovieViews(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()

        result_page = self.paginate_queryset(movies, request, view=self)

        serializer = MovieSerializer(result_page, many=True)

        return self.get_paginated_response(serializer.data)
    
    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)
    
class MovieDetailViews(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request: Request, movie_id: int) -> Response:
        find_movie = get_object_or_404(Movie, pk=movie_id)

        serializer = MovieSerializer(find_movie)

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request: Request, movie_id: int) -> Response:
        find_movie = get_object_or_404(Movie, pk=movie_id)

        find_movie.delete()

        return Response(status=204)
    
class MovieOrderDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, movie_id: int) -> Response:
        serializer = MovieOrderSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        find_movie = get_object_or_404(Movie, pk=movie_id)

        serializer.save(user=request.user, movie=find_movie)

        return Response(serializer.data, status.HTTP_201_CREATED)