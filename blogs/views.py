from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import BlogSerializer, CommentSerializer
from .models import Blog, Comment
from users.permissions import IsAdmin, IsEditor, IsOwnerOrAdmin
from rest_framework import viewsets
from django.utils.translation import gettext as _
from rest_framework.decorators import api_view, permission_classes


class BlogListView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BlogSerializer

    def get(self, request):
        blogs = Blog.objects.all().order_by("-date")
        serializer = self.serializer_class(blogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BlogDetailView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BlogSerializer

    def get(self, request, pk):
        try:
            blog = Blog.objects.get(id=pk)
        except Blog.DoesNotExist:
            return Response(
                {"error": "Blog no encontrado"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(blog)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BlogCreateView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated & (IsAdmin | IsEditor)]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BlogUpdateView(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated & (IsAdmin | IsEditor)]

    def perform_update(self, serializer):
        if (
            self.get_object().user == self.request.user
            or self.request.user.role == "admin"
        ):
            serializer.save()
        else:
            return Response(
                {"error": "No autorizado"}, status=status.HTTP_401_UNAUTHORIZED
            )


class BlogDeleteView(generics.DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated & (IsAdmin | IsEditor)]

    def perform_destroy(self, instance):
        if instance.user == self.request.user or self.request.user.role == "admin":
            id = instance.id
            instance.delete()
            return Response(
                {"mensaje": _("Publicación Eliminada"), "id": id},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"error": "No autorizado"}, status=status.HTTP_401_UNAUTHORIZED
            )


class BlogImageView(generics.UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated & (IsAdmin | IsEditor)]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        if instance.user == request.user or request.user.role == "admin":
            instance.image = request.FILES.get("image")
            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response(
                {"error": "No autorizado"}, status=status.HTTP_401_UNAUTHORIZED
            )


class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        # todo Asignar el usuario autenticado al campo 'user'
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.request.method in ["PUT", "DELETE"]:
            self.permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
