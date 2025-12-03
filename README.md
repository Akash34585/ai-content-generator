AI Content Generator (Python + OpenRouter)

A Python CLI tool that generates content (blogs, tweets, YouTube scripts, etc.) using the OpenRouter API with the free model `openai/gpt-oss-20b:free`.

All generated content is automatically saved into an `outputs/` folder as markdown files.

---

Features

- Multiple content modes:
  - Blog posts
  - Tweet / Thread
  - YouTube script
- Topic + tone + extra instructions
- Automatic saving to `outputs/` folder
- Clean project structure
- Uses `.env` for API key safety (not pushed to GitHub)

---

Project Structure

```
ai-content-generator/
├─ src/
│  ├─ main.py
│  ├─ openrouter_client.py
│  ├─ prompts.py
├─ outputs/               # auto-created when generating content
├─ .env                   # contains API key (not committed)
├─ .gitignore
├─ requirements.txt
├─ README.md
```

---

Setup

1. Create Virtual Environment

```
python -m venv .venv
.venv\Scripts\activate
```

2. Install Dependencies

```
pip install -r requirements.txt
```

3. Create `.env` File

```
OPENROUTER_API_KEY=your_key_here
```

---

Usage

Run the CLI:

```
python src\main.py
```

Follow the prompts:

1. Choose content type  
2. Enter topic  
3. Choose tone (optional)  
4. Extra instructions (optional)

---

Output Saving

Each result is automatically saved in:

```
outputs/
```

With filenames like:

```
20251203-youtube_script-forex-trading.md
```

---

Technologies Used

- Python
- OpenRouter API
- requests
- python-dotenv

---

Notes

- `.env` is ignored by Git for safety.
- The free model may be slower or rate-limited.
- You can extend content types easily by modifying `prompts.py` and `main.py`.

