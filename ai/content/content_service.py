from .content_client import ContentClient


MAX_CONTENT_LENGTH = 500


def _build_generate_prompt(title, tone=None):
    """
    The ONE place where the prompt text lives.
    """
    prompt = f"Write a short blog post about: {title}."
    if tone:
        prompt += f" Use a {tone} tone."
    return prompt


def generate_post(title, tone=None):
    # ---- 1. Input validation ----
    if not title or not title.strip():
        raise ValueError("Title cannot be empty.")

    if len(title.strip()) < 5:
        raise ValueError("Title must be at least 5 characters long.")

    # ---- 2. AI processing ----
    prompt = _build_generate_prompt(title, tone)
    client = ContentClient()
    raw_content = client.generate(prompt)

    # ---- 3. Post-processing ----
    content = raw_content.strip()

    if not content:
        raise ValueError("The AI returned an empty response.")

    if len(content) > MAX_CONTENT_LENGTH:
        content = content[:MAX_CONTENT_LENGTH]

    # ---- 4. Response formatting ----
    return {
        "title": title,
        "content": content,
        "length": len(content),
    }


def _build_summarize_prompt(post_content):
    """
    The ONE place where the summarization prompt text lives.
    """
    return f"Summarize the following blog post in 2-3 sentences:\n\n{post_content}"


def summarize_post(post_content):
    # ---- 1. Input validation ----
    if not post_content or not post_content.strip():
        raise ValueError("Post content cannot be empty.")

    # ---- 2. AI processing ----
    prompt = _build_summarize_prompt(post_content)
    client = ContentClient()
    raw_summary = client.generate(prompt)

    # ---- 3. Post-processing ----
    summary = raw_summary.strip()

    if not summary:
        raise ValueError("The AI returned an empty summary.")

    # ---- 4. Response formatting ----
    return {
        "summary": summary,
        "length": len(summary),
    }