from fastapi import APIRouter
from domain.schemas import ChatRequest, ChatResponse, FonteDado

router = APIRouter()

@router.post("/", response_model=ChatResponse)
async def chat_com_agente(request: ChatRequest):
    """
    Recebe a pergunta do paciente e retorna a resposta gerada pela IA,
    junto com as fontes genéticas utilizadas.
    """
    # TODO: injetar o motor LangGraph e a busca no Banco Vetorial aqui.
    
    # Mock estratégico para desbloquear a Nathalia no Front-end:
    resposta_mockada = ChatResponse(
        resposta=f"Avaliando seu perfil para a dúvida: '{request.mensagem}'. Identificamos uma variação genética importante no seu laudo simulado.",
        fontes=[
            FonteDado(
                painel="Genera Nutri",
                marcador="Sensibilidade à Cafeína",
                gene="CYP1A2",
                conclusao_curta="Metabolismo lento de cafeína"
            )
        ]
    )
    
    return resposta_mockada