import os
from langchain_community.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.docstore.document import Document as LangDoc
from tools.config import OPENAI_API_KEY

class MemoryManager:
    def __init__(self, persist_dir="memory/faiss_index"):
        self.embedder = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        self.persist_dir = persist_dir

        index_path = os.path.join(persist_dir, "index.faiss")
        if os.path.exists(index_path):
            self.db = FAISS.load_local(persist_dir, self.embedder,allow_dangerous_deserialization=True)
        else:
            # Bootstrap with dummy doc to initialize FAISS
            dummy_doc = LangDoc(page_content="bootstrap", metadata={"type": "dummy"})
            self.db = FAISS.from_documents([dummy_doc], self.embedder)
            self.db.save_local(persist_dir)

    def add_memory(self, subject, body, classification, reply):
        content = f"Subject: {subject}\nBody: {body}\nClassification: {classification}\nReply: {reply}"
        doc = LangDoc(page_content=content, metadata={"classification": classification, "type": "email"})
        self.db.add_documents([doc])
        self.db.save_local(self.persist_dir)

    def search_similar(self, subject, body, top_k=2):
        query = f"{subject}\n{body}"
        results = self.db.similarity_search(query, k=top_k + 1)  
        
        return [r for r in results if r.metadata.get("type") != "dummy"][:top_k]
