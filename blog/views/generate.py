from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ai.service.generate import generate_post

@api_view(["POST"])
def generate_post_view(request):
    title = request.data.get("title")
    tone = request.data.get("tone")

    try:
        result = generate_post(title, tone)
    except ValueError as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    return Response(result, status=status.HTTP_200_OK)