from .utils import validate_title, generate_ai_response, MAX_CONTENT_LENGTH


def _build_generate_prompt(title, tone=None):
    prompt = f"Write a short blog post about: {title}."
    if tone:
        prompt += f" Use a {tone} tone."
    return prompt


def generate_post(title, tone=None):
    cleaned_title = validate_title(title)
    content = generate_ai_response(cleaned_title, lambda t: _build_generate_prompt(t, tone))
    if not content:
        raise ValueError("The AI returned an empty response.")
    if len(content) > MAX_CONTENT_LENGTH:
        content = content[:MAX_CONTENT_LENGTH]
    return {"title": cleaned_title, "content": content, "length": len(content)}
