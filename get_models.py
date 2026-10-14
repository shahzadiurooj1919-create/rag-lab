"""Lesson 5: download the two models used in the tasks (about 0.8 GB) into ./models.

Run it inside rag-lab:  uv run get_models.py
Got the models folder on a USB stick? Copy it into rag-lab first and still run this script:
it then downloads nothing, and it also keeps the models out of Git.
"""
import os
from pathlib import Path

os.environ["HF_HUB_DISABLE_SYMLINKS"] = "1"  # plain files, so the models folder can be copied to a USB stick

from fastembed import TextEmbedding  # noqa: E402  (imported after the setting above on purpose)
from fastembed.rerank.cross_encoder import TextCrossEncoder  # noqa: E402

ignore = Path(".gitignore")                 # keep the models, API keys and the Qdrant folder out of Git
text = ignore.read_text(encoding="utf-8") if ignore.exists() else ""
missing = [p for p in ["models/", ".env", "qdrant_db/"] if p not in text.split()]
if missing:
    ignore.write_text(text.rstrip("\n") + "\n" + "\n".join(missing) + "\n", encoding="utf-8")

TextEmbedding("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", cache_dir="models")  # tasks 1-4
print("ready: the meaning model, for tasks 1-4. Your laptop is ready for task 1.")
print("       Keep this window open while the reranker for task 4 downloads;")
print("       run the tasks in a second terminal.")
TextCrossEncoder("BAAI/bge-reranker-v2-m3-int8", cache_dir="models")                              # task 4
print("ready: the reranker, for task 4")
print("All models are in ./models")
