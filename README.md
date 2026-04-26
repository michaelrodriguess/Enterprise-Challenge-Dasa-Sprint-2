# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "[https://www.fiap.com.br/](https://www.fiap.com.br/)"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Genera Intelligence: RAG Multimodelo para Laudos Genéticos

## Grupo: Squad AI Engineering

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/arthur-alentejo">Arthur Guimarães Alentejo</a>
- <a href="https://www.linkedin.com/in/michaelrodriguess">Michael Rodrigues</a>
- <a href="https://www.linkedin.com/in/nathalia-vasconcelos-18a390292/">Nathalia Vasconcelos</a> 

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="#">Caique (CaiqueFiap-2026)</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/andregodoichiovato/">André Godói</a>

## 📜 Descrição
O projeto visa resolver o gargalo de interpretação de dados genéticos do produto Genera (Grupo Dasa). Atualmente, os laudos são entregues em arquivos PDF extensos e repletos de terminologias técnicas, o que dificulta a compreensão do paciente e a tomada de decisão ágil pelo médico. 

Nossa solução propõe uma camada de inteligência baseada em **RAG (Retrieval-Augmented Generation)** que transforma esses documentos não estruturados em uma base de conhecimento consultável. Através de um Dashboard interativo aliado a um assistente conversacional (chatbot), o usuário pode "conversar" com seu DNA, recebendo explicações em linguagem simples, recomendações personalizadas e visualizações intuitivas de riscos e predisposições.

## 🎯 Contexto do Problema e Solução

### O Problema
O volume de dados gerado por um mapeamento genético é massivo. Informações sobre ancestralidade, farmacogenética (Farma), nutrição (Nutri), performance física (Fit) e riscos de doenças graves (Aging/Doenças Genéticas) ficam isoladas em silos de texto técnico. Isso gera:
1. **Baixo engajamento:** O paciente recebe o laudo, mas não sabe como aplicar as informações em sua rotina.
2. **Dificuldade Médica:** Profissionais de saúde precisam gastar tempo de consulta filtrando marcadores específicos (SNPs) em PDFs de dezenas de páginas.
3. **Falta de Interatividade:** O dado é estático; o usuário não consegue tirar dúvidas pontuais sem uma nova consulta.

### A Solução
Desenvolvemos uma pipeline completa de processamento que utiliza IA para:
- **Extrair e Estruturar:** Converter PDFs técnicos em JSONs organizados por categorias de saúde.
- **Anonimizar:** Garantir que nenhum dado sensível (PII) saia do ambiente seguro da AWS para ferramentas de terceiros.
- **Interpretar:** Utilizar múltiplos agentes especialistas (LangGraph) para responder dúvidas sobre diferentes painéis genéticos (Ex: um agente focado em Nutrição e outro em Risco Clínico).

## 👥 Perfis de Usuários (Personas)

Para garantir que a solução entregue valor real, o sistema foi desenhado pensando em duas frentes de interação principais, cada uma com necessidades bem diferentes em relação aos dados genéticos:

1. **🧬 O Paciente (Usuário Final)**
   * **A Dor:** Recebe um laudo denso e se sente perdido. Quer otimizar sua rotina, mas não entende o que significa um "alelo rs324640-G".
   * **O Caso de Uso:** Uma pessoa focada em melhorar o desempenho físico e a dieta (hipertrofia, emagrecimento ou longevidade). Ela acessa o chat da plataforma para perguntar: *"Com base no meu painel Genera Fit e Nutri, como está a minha predisposição para absorção de proteínas e recuperação muscular?"*. O sistema traduz a genética em respostas práticas e acionáveis para o dia a dia.
   * **O Valor:** Autonomia, engajamento com a própria saúde e desmistificação da genética.

2. **🩺 O Profissional de Saúde (Médico, Nutricionista ou Geneticista)**
   * **A Dor:** Tempo de consulta limitado. Analisar um PDF de 60 páginas para cruzar variáveis genéticas (SNPs) com o quadro clínico do paciente é um processo lento e sujeito a erros.
   * **O Caso de Uso:** O profissional acessa a visão de "Especialista" no Dashboard. O RAG já filtrou os marcadores de alto risco (ex: predisposição no painel Farma para reações adversas a medicamentos ou baixo nível de Vitamina D).
   * **O Valor:** Agilidade na tomada de decisão clínica, visualização estruturada dos riscos (PRS - *Polygenic Risk Score*) e assertividade na prescrição de tratamentos ou dietas.

---

## 🏗 Arquitetura da Solução

A solução é construída sobre a infraestrutura **AWS**, utilizando modelos de linguagem via **Amazon Bedrock** e orquestração de agentes com **LangGraph**.

### Diagrama de Arquitetura

<img src="assets/hld.png" alt="High Level Design">

## 📊 Estrutura de Dados (Exemplo JSON)
Abaixo, um exemplo de como os dados extraídos dos PDFs (como o Genera Skin e Fit) são estruturados para consulta da IA:

```json
{
  "paciente_id": "uuid-123",
  "paineis": [
    {
      "categoria": "Genera Fit",
      "marcadores": [{
          "caracteristica": "Densidade óssea",
          "gene": "WNT16",
          "predisposicao": "Menor densidade óssea",
          "recomendacao": "Monitorar ingestão de cálcio e vitamina D."
      }]
    }
  ]
}
```


## 🚀 Próximos Passos (Evolução para as Próximas Sprints)

Nesta Sprint 1, consolidamos a visão de negócio, a modelagem dos dados e a arquitetura em nuvem. Para as próximas fases do Challenge, o desenvolvimento será dividido nas seguintes frentes táticas:

* **Fase 1: Infraestrutura e Ingestão (Backend)**
  * Provisionar os serviços base na AWS (Buckets S3 para os PDFs e tabelas do DynamoDB para o *Data Vault* de anonimização).
  * Criar o script inicial em Python para ler os laudos de exemplo (Fit, Skin, Aging, Nutri) e forçar a extração para o formato JSON definido.

* **Fase 2: Orquestração da IA (O Cérebro da Operação)**
  * Configurar o ambiente do LangGraph.
  * Criar o backend e o vector store para alimentar os agentes especialistas.
  * Desenvolver os *system prompts* para cada agente, garantindo que eles consigam interpretar os dados genéticos e responder de forma contextualizada.
  * Desenvolver e implementar o agente supervisor para roteamento inteligente das perguntas dos usuários.

* **Fase 3: Prototipação da Interface (Frontend)**
  * Criar o wireframe de alta fidelidade do Dashboard.
  * Conectar a interface web com a API do LangGraph para simular as primeiras conversas reais com a IA usando os dados de teste.
  * Implementar os guardrails de segurança para garantir que o bot sempre inclua um *disclaimer* médico em suas respostas.

***

## 📁 Estrutura de pastas

- <b>.github</b>: Workflows de automação e CI/CD.
- <b>assets</b>: Diagramas de arquitetura, imagens dos laudos e logo da FIAP.
- <b>config</b>: Configurações de ambiente (env vars) e definições dos agentes LangGraph.
- <b>document</b>: Documentação técnica detalhada e o arquivo de kick-off do Challenge Dasa.
- <b>scripts</b>: Scripts Python para anonimização de PDFs e carga inicial no banco vetorial.
- <b>src</b>: Código-fonte do backend (FastAPI), processamento Lambda e frontend (React).
- <b>README.md</b>: Este guia do projeto.

## 🔧 Como executar o código

Nesta **Sprint 1**, o foco é a proposta técnica e arquitetural. Não há necessidade de execução de código funcional.
1. Clone o repositório.
2. Acesse a pasta `/document` para ler a especificação técnica.
3. Visualize o diagrama de arquitetura na seção acima.

## 🗃 Histórico de lançamentos

* 0.1.0 - 24/04/2026
    * Estruturação inicial do projeto, definição da arquitetura AWS e pipeline de anonimização.

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
