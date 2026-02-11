import requests
import msgpack
import numpy as np
import json

ENDEE_URL = "http://localhost:8080"
INDEX_NAME = "jobs_index1"


# =========================
# INSERT VECTOR
# =========================
def insert_vector(job_id, title, description, embedding):
    url = f"{ENDEE_URL}/api/v1/index/{INDEX_NAME}/vector/insert"

    # Convert embedding to float16 binary buffer
    vector_bytes = np.array(embedding, dtype=np.float16).tobytes()

    payload = {
        "id": job_id,
        "dense_vector": vector_bytes,
        "metadata": json.dumps({
            "title": title,
            "description": description
        })
    }

    packed_payload = msgpack.packb(payload, use_bin_type=True)

    headers = {
        "Content-Type": "application/msgpack"
    }

    response = requests.post(url, data=packed_payload, headers=headers)

    return response.status_code, response.text


# =========================
# SEARCH VECTOR
# =========================
def search_vector(embedding):
    url = f"{ENDEE_URL}/api/v1/index/{INDEX_NAME}/vector/search"

    vector_bytes = np.array(embedding, dtype=np.float16).tobytes()

    payload = {
        "dense_vector": vector_bytes,
        "top_k": 5
    }

    packed_payload = msgpack.packb(payload, use_bin_type=True)

    headers = {
        "Content-Type": "application/msgpack"
    }

    response = requests.post(url, data=packed_payload, headers=headers)

    if response.status_code == 200:
        return response.status_code, response.json()
    else:
        return response.status_code, response.text
