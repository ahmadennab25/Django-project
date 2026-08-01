from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Post
from ai.content.service import summarize_post


@api_view(["POST"])
def summarize_post_view(request):
    post_id = request.data.get("post_id")

    try:
        post_id = int(post_id)
    except (TypeError, ValueError):
        return Response({"error": "valid post_id is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    try:
        result = summarize_post(post.content)
    except ValueError as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    post.summary = result["summary"]
    post.summary_generated_at = timezone.now()
    post.save(update_fields=["summary", "summary_generated_at"])

    return Response({
        "post_id": post.id,
        "title": post.title,
        "summary": post.summary,
        "summary_generated_at": post.summary_generated_at,
    }, status=status.HTTP_200_OK)