from configs.database import articles


class ArticleRepository:
    def save(self, articleId, content, chunks):
        doc = {
            "articleId": articleId,
            "content": content,
            "chunks": chunks
        }
        articles.update_one({"articleId": articleId}, {"$set": doc}, upsert=True)
        return articleId

    def load(self, articleId):
        return articles.find_one({"articleId": articleId})

    def list_all(self):
        return list(articles.find({}, {"_id": 0, "articleId": 1, "content": 1}))
