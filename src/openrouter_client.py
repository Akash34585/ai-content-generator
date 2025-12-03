import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "openai/gpt-oss-20b:free"


if not OPENROUTER_API_KEY:
    raise RuntimeError("OPENROUTER_API_KEY not found in .env file")


def generate_content(system_prompt: str, user_prompt: str, max_tokens: int = 800) -> str:
    """
    Call OpenRouter with given system + user prompt and return model response text.
    Also prints raw response for debugging if something goes wrong.
    """
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        # Optional but good practice:
        "HTTP-Referer": "https://github.com/your-username/ai-content-generator",
        "X-Title": "AI Content Generator CLI",
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        "max_tokens": max_tokens,
        "temperature": 0.8,
    }

    try:
        resp = requests.post(BASE_URL, json=payload, headers=headers, timeout=60)
        resp.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error calling OpenRouter API: {e}")

    data = resp.json()

    # DEBUG: print the raw JSON so we know what the hell is happening
    print("\n[DEBUG] Raw API response:")
    print(data)
    print("[DEBUG] End of raw response\n")

    # Try to extract text in the normal OpenAI-style format
    try:
        content = data["choices"][0]["message"]["content"]
    except (KeyError, IndexError) as e:
        raise RuntimeError(f"Unexpected API response format: {e}\nFull response: {data}")

    # If the content is empty or just whitespace, complain
    if not isinstance(content, str) or not content.strip():
        raise RuntimeError(f"Model returned empty content.\nFull response: {data}")

    return content
