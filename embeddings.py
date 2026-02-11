from sentence_transformers import SentenceTransformer

model = None

def get_embedding(text: str):
    global model
    if model is None:
        model = SentenceTransformer("all-MiniLM-L6-v2")
    return model.encode(text).tolist()
