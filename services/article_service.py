from models.article_repository import ArticleRepository
from services.chunker import chunk_text
from services.embedding_service import EmbeddingService


class ArticleService:
    def __init__(self, google_api_key):
        self.embedding_service = EmbeddingService(google_api_key=google_api_key)
        self.repo = ArticleRepository()

    def process_and_save_article(self, articleId, content):
        chunks = chunk_text(content)
        chunks = self.embedding_service.embed_chunks(chunks)
        self.repo.save(articleId, content, chunks)
        return {"articleId": articleId, "chunks": len(chunks)}

    def load_article(self, articleId):
        return self.repo.load(articleId)

    def list_articles(self):
        return self.repo.list_all()

    def delete_article_embedding(self, articleId):
        return self.repo.delete(articleId)
