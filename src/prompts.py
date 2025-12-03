BLOG_SYSTEM_PROMPT = """
You are an expert blog content writer. 
You write clear, structured, SEO-friendly blog posts with headings, subheadings, and bullet points when useful.
Keep language simple and readable.
"""

TWEET_SYSTEM_PROMPT = """
You are an expert Twitter ghostwriter.
You write short, engaging tweets or threads. Avoid hashtags unless specifically requested.
"""

YOUTUBE_SYSTEM_PROMPT = """
You are a YouTube script writer.
You write engaging scripts with hook, intro, body, and call to action.
Write in a natural spoken style, not like a formal essay.
"""


def build_user_prompt(content_type: str, topic: str, tone: str | None, extra_instructions: str | None) -> str:
    tone_part = f"Tone: {tone}." if tone else ""
    extra_part = f"\nAdditional instructions: {extra_instructions}" if extra_instructions else ""

    return f"""
Content type: {content_type}
Topic: {topic}
{tone_part}
{extra_part}
"""
