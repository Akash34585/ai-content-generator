import os
from datetime import datetime
from openrouter_client import generate_content
from prompts import (
    BLOG_SYSTEM_PROMPT,
    TWEET_SYSTEM_PROMPT,
    YOUTUBE_SYSTEM_PROMPT,
    build_user_prompt,
)

def save_output_to_file(content_type: str, topic: str, output: str) -> str:
    """
    Save the generated content into outputs/ as a markdown file.
    Returns the file path.
    """
    os.makedirs("outputs", exist_ok=True)

    # Make a safe filename from the topic
    safe_topic = "".join(
        c if c.isalnum() or c in (" ", "-", "_") else "" for c in topic
    )
    safe_topic = "-".join(safe_topic.lower().split())
    if not safe_topic:
        safe_topic = "content"

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{timestamp}-{content_type}-{safe_topic}.md"
    filepath = os.path.join("outputs", filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {topic}\n\n")
        f.write(output)

    return filepath



def choose_content_type() -> str:
    print("Select content type:")
    print("1. Blog post")
    print("2. Tweet / Thread")
    print("3. YouTube script")

    choice = input("Enter choice (1/2/3): ").strip()

    mapping = {
        "1": "blog",
        "2": "tweet",
        "3": "youtube_script",
    }

    if choice not in mapping:
        print("Invalid choice. Defaulting to blog post.")
        return "blog"

    return mapping[choice]


def get_system_prompt(content_type: str) -> str:
    if content_type == "blog":
        return BLOG_SYSTEM_PROMPT
    if content_type == "tweet":
        return TWEET_SYSTEM_PROMPT
    if content_type == "youtube_script":
        return YOUTUBE_SYSTEM_PROMPT

    # fallback
    return BLOG_SYSTEM_PROMPT


def main():
    print("=== AI Content Generator (OpenRouter) ===")

    content_type = choose_content_type()
    topic = input("Enter topic / idea: ").strip()

    if not topic:
        print("Topic cannot be empty. Exiting.")
        return

    tone = input("Optional: desired tone (e.g., formal, casual, funny) or leave blank: ").strip()
    tone = tone if tone else None

    extra = input("Optional: any extra instructions (SEO, word limit, etc.) or leave blank: ").strip()
    extra = extra if extra else None

    system_prompt = get_system_prompt(content_type)
    user_prompt = build_user_prompt(content_type, topic, tone, extra)

    print("\nGenerating content...\n")

    try:
        output = generate_content(system_prompt, user_prompt)
    except Exception as e:
        print(f"Error: {e}")
        return

    print("=== Generated Content ===\n")
    print(output)  # normal print, will show proper newlines
    print("\n=========================")


    # Save to file
    filepath = save_output_to_file(content_type, topic, output)
    print(f"Content saved to file: {filepath}")



if __name__ == "__main__":
    main()
