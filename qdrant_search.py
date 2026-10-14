from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

def main():
    print("--- INITIALIZING IN-MEMORY QDRANT VECTOR DATABASE ---")
    
    client = QdrantClient(":memory:")

    client.create_collection(
        collection_name="guide_chunks",
        vectors_config=VectorParams(size=4, distance=Distance.COSINE),
    )

    client.upsert(
        collection_name="guide_chunks",
        points=[
            PointStruct(id=1, vector=[0.05, 0.61, 0.76, 0.74], payload={"text": "Navigate to security settings and click password reset."}),
            PointStruct(id=2, vector=[0.19, 0.81, 0.75, 0.11], payload={"text": "Billing history is located under the payments tab."}),
            PointStruct(id=3, vector=[0.33, 0.12, 0.89, 0.44], payload={"text": "The requested resource or endpoint does not exist on the server."}),
        ]
    )

    query_vector = [0.05, 0.61, 0.76, 0.74]
    search_result = client.query_points(
        collection_name="guide_chunks",
        query=query_vector,
        limit=1
    ).points

    print("\n--- QDRANT VECTOR SEARCH RESULT ---")
    for hit in search_result:
        print(f"Match ID: {hit.id} | Score: {hit.score:.4f}")
        print(f"Text Payload: {hit.payload['text']}")

if __name__ == "__main__":
    main()
