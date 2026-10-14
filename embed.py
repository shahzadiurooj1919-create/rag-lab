import numpy as np
from fastembed import TextEmbedding

MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
model = TextEmbedding(MODEL, cache_dir="models")

sentences = [
    "I want a refund.",
    "How do I get my money back?",
    "أريد استرداد أموالي",
    "The library opens at 8:00.",
    "مجھے اپنے پیسے واپس چاہئیں"
]
vectors = np.array(list(model.embed(sentences)))
vectors = vectors / np.linalg.norm(vectors, axis=1, keepdims=True)
print(vectors.shape)
print(np.round(vectors @ vectors.T, 2))
