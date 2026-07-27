from decouple import config
from openai import OpenAI


class ContentClient:
    """
    The only class allowed to talk to the OpenAI API directly.
    Any AI feature (summarization, generation, etc.) must go through this client.
    """

    def __init__(self):
        api_key = config('OPENAI_API_KEY')
        self.client = OpenAI(api_key=api_key)

    def generate(self, prompt):
        """
        Sends a prompt to a cheap OpenAI chat model and returns the plain text reply.
        """
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
        return response.choices[0].message.content