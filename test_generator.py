from src.generator import generate_quiz
from src.database import retrieve_context

context = retrieve_context("Cricket")

quiz = generate_quiz(
    "Cricket",
    "Easy",
    "\n".join(context)
)

print(quiz)