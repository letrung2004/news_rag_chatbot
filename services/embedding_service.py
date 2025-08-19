from langchain_google_genai import GoogleGenerativeAIEmbeddings


class EmbeddingService:
    def __init__(self, google_api_key, model_name="models/embedding-001"):
        self.model = GoogleGenerativeAIEmbeddings(
            model=model_name,
            google_api_key=google_api_key
        )

    def embed_chunks(self, chunks):
        texts = [c["cleaned"] for c in chunks]
        embeddings = self.model.embed_documents(texts)
        for idx, emb in enumerate(embeddings):
            chunks[idx]["embedding"] = emb
        return chunks

    def embed_query(self, query: str):
        return self.model.embed_query(query)
