from .utils import validate_post_content, generate_ai_response


def _build_summarize_prompt(post_content):
    return f"Summarize the following blog post in 2-3 sentences:\n\n{post_content}"


def summarize_post(post_content):
    cleaned_content = validate_post_content(post_content)
    summary = generate_ai_response(cleaned_content, _build_summarize_prompt)
    if not summary:
        raise ValueError("The AI returned an empty summary.")
    return {"summary": summary, "length": len(summary)}
