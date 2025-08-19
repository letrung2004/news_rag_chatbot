from langchain.text_splitter import RecursiveCharacterTextSplitter
import re


def clean(text: str) -> str:
    text = text.lower()
    text = re.sub(r'\S+@\S+\.\S+', 'email', text)
    text = re.sub(r'[^\w\s]', '', text)
    return re.sub(r'\s+', ' ', text).strip()


def chunk_text(content: str, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", "!", "?", " ", ""]
    )

    texts = splitter.split_text(content)

    chunks = []
    for idx, t in enumerate(texts):
        chunks.append({
            "index": idx,
            "original": t.strip(),
            "cleaned": clean(t)
        })

    return chunks
