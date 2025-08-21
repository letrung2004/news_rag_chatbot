import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import google.generativeai as genai


class Chatbot:
    def __init__(self, api_key, embedding_service, article_service):
        self.embedding_service = embedding_service
        self.article_service = article_service
        genai.configure(api_key=api_key)
        self.gemini_model = genai.GenerativeModel("gemini-1.5-flash")

    def search_query(self, articleId, query, top_k=3):
        doc = self.article_service.load_article(articleId)
        if not doc:
            return [], []

        chunks = doc["chunks"]
        embeddings = np.array([c["embedding"] for c in chunks])

        query_emb = self.embedding_service.embed_query(query)
        similarities = cosine_similarity([query_emb], embeddings)
        top_indices = np.argsort(similarities[0])[::-1][:top_k]

        contexts = [chunks[idx]["original"] for idx in top_indices]
        scores = [similarities[0][idx] for idx in top_indices]
        return contexts, scores

    def generate_answer_with_gemini(self, context, question):
        prompt = f"""
        Bạn là trợ lý báo thông minh MAGNEWS.
        Dựa trên nội dung bài báo được cung cấp, hãy trả lời câu hỏi sau.

        Câu hỏi:
        {question}

        Ngữ cảnh:
        {context}

        Nếu không tìm thấy thông tin hãy trả lời:
        "Tôi không thấy thông tin này được nhắc đến trong bài báo."
        """
        try:
            response = self.gemini_model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error: {e}"

    def ask(self, articleId, question):
        contexts, _ = self.search_query(articleId, question)
        context_text = "\n".join(contexts)
        return self.generate_answer_with_gemini(context_text, question)
