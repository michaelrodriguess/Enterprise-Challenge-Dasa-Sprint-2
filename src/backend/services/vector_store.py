import json
import os
from pathlib import Path
from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

load_dotenv()

CURRENT_DIR = Path(__file__).parent
BACKEND_DIR = CURRENT_DIR.parent
PROJECT_ROOT = BACKEND_DIR.parent.parent
JSON_PATH = PROJECT_ROOT / "proposta_estrutura_de_dados.json"
FAISS_INDEX_PATH = BACKEND_DIR / "faiss_index"

def carregar_dados_json() -> list[Document]:
    print(f"Lendo dados de: {JSON_PATH}")
    
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        dados = json.load(f)
        
    paciente_id = dados.get("paciente_id", "desconhecido")
    documentos = []
    
    for painel in dados.get("paineis_geneticos", []):
        nome_painel = painel.get("nome_painel")
        
        for resultado in painel.get("resultados", []):
            conteudo_texto = (
                f"Característica: {resultado['caracteristica']}. "
                f"Conclusão: {resultado['conclusao_curta']}. "
                f"Explicação: {resultado['explicacao_detalhada']}"
            )
            
            metadados = {
                "paciente_id": paciente_id,
                "painel": nome_painel,
                "caracteristica": resultado.get("caracteristica"),
                "gene": resultado.get("dados_tecnicos", {}).get("gene", "N/A"),
                "conclusao_curta": resultado.get("conclusao_curta")
            }
            
            doc = Document(page_content=conteudo_texto, metadata=metadados)
            documentos.append(doc)
            
    print(f"Total de {len(documentos)} documentos extraídos com sucesso.")
    return documentos

def criar_e_salvar_banco_vetorial():
    documentos = carregar_dados_json()
    
    if not documentos:
        print("Nenhum documento encontrado.")
        return

    print("Conectando ao Google AI Studio (Gemini) para gerar Embeddings...")
    
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        task_type="RETRIEVAL_DOCUMENT"
    )
    
    print("Gerando vetores e criando o banco FAISS...")
    vector_store = FAISS.from_documents(documentos, embeddings)
    
    print(f"Salvando banco vetorial em: {FAISS_INDEX_PATH}")
    vector_store.save_local(str(FAISS_INDEX_PATH))
    print("✅ Ingestão finalizada com sucesso! Banco Vetorial pronto para uso.")

if __name__ == "__main__":
    criar_e_salvar_banco_vetorial()