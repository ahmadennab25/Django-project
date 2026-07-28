from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Post
from ..serializers import PostSerializer


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