from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Post
from .serializers import UserSerializer, PostSerializer
from ai.content.content_service import generate_post, summarize_post


# ---- WAY 1: ViewSet (Router auto-builds all CRUD URLs) ----
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# ---- WAY 2: MANUAL (function-based view) ----
@api_view(["GET"])
def get_posts(request):
    try:
        page = int(request.query_params.get("page", 1))
        limit = int(request.query_params.get("limit", 10))
        start = (page - 1) * limit
        end = start + limit

        posts = Post.objects.filter(is_published=True)[start:end]
        serializer = PostSerializer(posts, many=True)

        return Response(
            {"page": page, "limit": limit, "results": serializer.data},
            status=status.HTTP_200_OK,
        )

    except Exception:
        return Response(
            {"error": "An unexpected error occurred."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    # GET /blog/posts/manual/?page=1&limit=5


@api_view(["GET"])
def get_users(request):
    users = User.objects.filter(is_active=True)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def hello(request):
    return Response({"message": "Hello, API is working!"})


# ---- AI FEATURE 1: Summarize an existing post ----
@api_view(["POST"])
def summarize_post_view(request):
    post_id = request.data.get("post_id")

    try:
        post_id = int(post_id)
    except (TypeError, ValueError):
        return Response({"error": "valid post_id is required"}, status=400)

    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=404)

    try:
        result = summarize_post(post.content)
    except ValueError as e:
        return Response({"error": str(e)}, status=400)

    return Response({
        "post_id": post.id,
        "title": post.title,
        "summary": result["summary"],
    }, status=200)


# ---- AI FEATURE 2: Generate a new post from a title ----
@api_view(["POST"])
def generate_post_view(request):
    title = request.data.get("title")
    tone = request.data.get("tone")

    try:
        result = generate_post(title, tone)
    except ValueError as e:
        return Response({"error": str(e)}, status=400)

    return Response(result, status=200)