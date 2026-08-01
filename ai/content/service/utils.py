from ai.content.content_client import ContentClient

MAX_CONTENT_LENGTH = 500
MIN_INPUT_LENGTH = 20


def validate_title(title):
    if not title or not title.strip():
        raise ValueError("Title cannot be empty.")
    cleaned_title = title.strip()
    if len(cleaned_title) < 5:
        raise ValueError("Title must be at least 5 characters long.")
    return cleaned_title


def validate_post_content(post_content):
    if not post_content or not post_content.strip():
        raise ValueError("Post content cannot be empty.")
    cleaned_content = post_content.strip()
    if len(cleaned_content) < MIN_INPUT_LENGTH:
        raise ValueError("Content is too short to summarize.")
    return cleaned_content


def generate_ai_response(cleaned_text, build_prompt):
    prompt = build_prompt(cleaned_text)
    client = ContentClient()
    raw_response = client.generate(prompt)
    return raw_response.strip()
