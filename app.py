from flask import Flask, request, jsonify
from flask_cors import CORS

from services.article_service import ArticleService
from services.rag_chat import Chatbot

app = Flask(__name__)
CORS(app)

GOOGLE_API_KEY = "AIzaSyAGXyz4q6xk3QaRTo4dIjesz-QZlhSI-oY"

article_service = ArticleService(google_api_key=GOOGLE_API_KEY)
embedding_service = article_service.embedding_service
chatbot = Chatbot(
    api_key=GOOGLE_API_KEY,
    embedding_service=embedding_service,
    article_service=article_service
)


@app.route('/api/embedding', methods=['POST'])
def save_article():
    data = request.get_json()
    articleId = data.get("articleId")
    content = data.get("content")

    if not articleId or not content:
        return jsonify({"error": "Missing articleId or content"}), 400

    result = article_service.process_and_save_article(articleId, content)
    return jsonify(result)


@app.route('/api/embedding/<articleId>', methods=['GET'])
def get_article(articleId):
    doc = article_service.load_article(articleId)
    if not doc:
        return jsonify({"error": "Article not found"}), 404
    return jsonify(doc)


@app.route('/api/embeddings', methods=['GET'])
def list_articles():
    return jsonify(article_service.list_articles())


@app.route('/api/ask', methods=['POST'])
def ask():
    data = request.get_json()
    articleId = data.get("articleId")
    question = data.get("question")

    if not articleId or not question:
        return jsonify({"error": "Missing articleId or question"}), 400

    answer = chatbot.ask(articleId, question)
    return jsonify({"answer": answer})


@app.route('/api/embedding/<articleId>', methods=['DELETE'])
def delete_article(articleId):
    success = article_service.delete_article_embedding(articleId)
    if not success:
        return jsonify({"error": "Article embedding not found"}), 404
    return jsonify({"message": "Article embedding deleted successfully"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
