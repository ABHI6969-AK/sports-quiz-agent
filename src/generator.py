import json
from groq import Groq
from src.config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)


def generate_quiz(sport, difficulty, context):

    prompt = f"""
You are an expert sports quiz generator.

Generate EXACTLY 5 multiple-choice questions.

Rules:

- Questions must ONLY be about {sport}
- Difficulty: {difficulty}
- Use the context provided
- Exactly 4 options
- Exactly one correct answer
- Return ONLY valid JSON
- No markdown
- No explanation

Context:

{context}

Return this format:

[
  {{
    "question":"...",
    "options":[
        "...",
        "...",
        "...",
        "..."
    ],
    "answer":"..."
  }}
]
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.6,
    )

    content = response.choices[0].message.content.strip()

    if content.startswith("```"):
        content = content.replace("```json", "")
        content = content.replace("```", "")

    return json.loads(content)