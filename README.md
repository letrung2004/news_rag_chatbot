# RAG Chatbot - MAGNEWS Intelligent News Assistant

An intelligent chatbot system using RAG (Retrieval-Augmented Generation) technique to answer questions based on news article content. The chatbot can understand and extract information from articles, then provide accurate and well-grounded responses.

## Key Features

- **Intelligent Responses**: Analyzes questions and searches for relevant information from article content
- **Optimized Storage**: Uses MongoDB to store embeddings, avoiding recalculation for processed articles
- **Semantic Search**: Utilizes embedding vectors to find information with high similarity
- **Natural Language Processing**: Integrates Google Gemini AI to generate natural responses

## Data Structure

### Input Embedding
```json
{
    "articleId": "1234",
    "content": "Full article content..."
}
```

### Chunk Structure
```json
{
    "index": 0,
    "original": "Original text segment",
    "cleaned": "cleaned text segment",
    "embedding": [0.1, 0.2, 0.3, ...]
}
```

## API Configuration
```python
GOOGLE_API_KEY = "your_google_api_key_here"
MONGODB_URI = "your_mongodb_connection_string"
```

### 2. Process New Article
```python
# Prepare article data
article_data = {
    "articleId": "1234",
    "content": "Article content..."
}

# Process and save to database
article_service.process_and_save_article(article_data)
```

### 3. Ask Questions
```python
# Ask about article content
answer = chatbot.ask(
    articleId="1234",
    question="What position did Vietnam rank in SEA V.League 2025?"
)
print(answer)
```

## Core Components

### Text Processing
- **Cleaning**: Removes special characters, normalizes text
- **Chunking**: Splits articles into 500-character segments with 50-character overlap
- **Embedding**: Uses Google Embedding model `models/embedding-001`

### Search Engine
- **Similarity Search**: Uses cosine similarity to find the most relevant chunks
- **Top-K Retrieval**: Retrieves the top 3 most similar text segments

### Answer Generation
- **Context Building**: Combines relevant chunks into context
- **Prompt Engineering**: Uses optimized prompts for Vietnamese language
- **Gemini Integration**: Uses Gemini 1.5 Flash to generate answers

## Customization

### Chunk Size
```python
# Modify chunk size
chunks = chunk_text(content, chunk_size=800, chunk_overlap=100)
```

### Top-K Results
```python
# Retrieve more context
contexts, scores = chatbot.search_query(articleId, query, top_k=5)
```

### Prompt Customization
You can customize the prompt in the `generate_answer_with_gemini()` method to suit specific domains.


## References

- [LangChain Documentation](https://docs.langchain.com/)
- [Google Generative AI](https://ai.google.dev/)
- [MongoDB Documentation](https://docs.mongodb.com/)

## Contributing

All contributions are welcome! Please create issues or pull requests to improve the system.
