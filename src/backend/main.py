from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import chat

app = FastAPI(
    title="Genera Intelligence API",
    description="Motor RAG e Multi-Agent para Interpretação de Laudos Genéticos (Dasa)",
    version="0.2.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Acopla os roteadores
app.include_router(chat.router, prefix="/api/chat", tags=["Chat Conversacional"])

# Rota básica de health check
@app.get("/health", tags=["Monitoramento"])
def health_check():
    return {"status": "ok", "message": "A API Genera Intelligence está no ar!"}