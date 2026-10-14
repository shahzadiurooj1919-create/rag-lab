"""Lesson 5 helper: loads the guide and the test questions, and scores a search.
Keep it in rag-lab next to your own files. You do not need to change it."""
import json

import numpy as np
from fastembed import TextEmbedding

model = TextEmbedding("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", cache_dir="models")


def embed(texts):
    """Turn each text into 384 numbers, scaled as in task 1, so that @ gives the similarity."""
    vectors = np.array(list(model.embed(texts)))
    return vectors / np.linalg.norm(vectors, axis=1, keepdims=True)


def load(path):
    """Read a questions file: one {"id", "question", "answer"} per line."""
    return [json.loads(line) for line in open(path, encoding="utf-8-sig") if line.strip()]


GUIDE = open("campus_guide.md", encoding="utf-8").read()
SECTIONS = ["## " + part.strip() for part in GUIDE.split("\n## ")[1:]]   # 70 sections
QUESTIONS = load("questions.jsonl")                                       # 20 test questions


def evaluate(search, questions=QUESTIONS):
    """Ask every question. Count how often the right section comes back first, and in the top 5."""
    first, top5, missed = 0, 0, []
    for q in questions:
        results = search(q["question"])[:5]
        right = [q["answer"] in section for section in results]
        if any(right):
            top5 += 1
            first += right[0]
        else:
            missed.append(q["id"])
    n = len(questions)
    print(f"{search.__name__:14}  first {first:2}/{n}   top 5 {top5:2}/{n}   missed: {' '.join(missed) or '-'}")
