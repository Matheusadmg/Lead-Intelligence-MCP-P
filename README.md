<div align="center">

# Lead Intelligence MCP

</div>

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.141%2B-009688?logo=fastapi&logoColor=white)
![Model Context Protocol](https://img.shields.io/badge/MCP-Protocol-purple?logo=anthropic&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16--alpine-336791?logo=postgresql&logoColor=white)
![Arize Phoenix](https://img.shields.io/badge/Arize%20Phoenix-Observability-orange)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)
![DeepEval](https://img.shields.io/badge/DeepEval-LLM%20Evaluation-critical)
![Poetry](https://img.shields.io/badge/Packaging-Poetry-blueviolet?logo=poetry&logoColor=white)

**Servidor MCP (Model Context Protocol) para enriquecimento semântico, detecção de anomalias e qualificação preditiva de leads B2B com IA e Observabilidade.**

[Visão Geral](#visão-geral) •
[Problema de Negócio](#problema-de-negócio) •
[Lógica de Scoring](#lógica-de-qualificação-e-scoring) •
[Arquitetura](#arquitetura-do-sistema) •
[Tech Stack](#stack-tecnológica) •
[Como Executar](#como-executar)

---

</div>

## Visão Geral

O **Lead Intelligence MCP** é um serviço projetado para padronizar e controlar o fornecimento de contexto de negócio para agentes de **Inteligência Artificial (LLMs)**.

Através do **Model Context Protocol (MCP)**, o sistema atua como uma interface segura entre a IA e o banco de dados (CRM). O protocolo cria uma camada de abstração sobre as APIs tradicionais, garantindo que o agente acesse estritamente os dados permitidos e eliminando a necessidade de reescrever integrações caso o modelo fundacional seja substituído.

Projetado sob princípios de **Clean Architecture**, **SOLID** e tipagem estrita via **Pydantic**, o projeto integra uma esteira de **Observabilidade de LLMs (Arize Phoenix)** e testes de robustez semântica para mitigar falsos positivos e garantir decisões precisas.

---

## Problema de Negócio

Empresas de software B2B SaaS enfrentam perdas de produtividade comercial quando seus times de vendas gastam tempo com:
1. **Falsos Positivos:** Contatos de estagiários ou estudantes em empresas gigantes que não possuem poder de decisão de compra.
2. **Concorrentes:** Concorrentes baixando materiais de topo de funil ou solicitando demonstrações para engenharia reversa.
3. **Cargos Inflados / Ambíguos:** Títulos de cargos informais ou de microempresas (ex: "CEO" de MEI de entregas vs "Head de Inbound" de uma grande corporação).
4. **Anomalias de Comportamento:** Leads que abriram chamados de cancelamento/reclamação mascarados como engajamento, ou bots inundando formulários.

O Lead Intelligence MCP resolve isso combinando **análise contextual via LLM**, regras determinísticas de negócio e inferência semântica de ICP.

---

## Lógica de Qualificação e Scoring

Para transformar dados brutos em decisões acionáveis, o sistema atua como uma camada de inteligência semântica sobre o Lead Score existente. O motor de decisão cruza a pontuação atual com regras determinísticas e análise de contexto em três dimensões principais:

```mermaid
flowchart LR
    subgraph Entrada
        L[Lead Data & Histórico]
    end

    subgraph "Motor de Decisão (MCP + LLM)"
        F[1. Fit de Perfil\n- Cargo e Senioridade\n- Tamanho e Setor\n- Domínio Corporativo vs Genérico]
        E[2. Engajamento e Intenção\n- Jornada no Funil\n- Recência e Frequência\n- Ações de Alta Intenção]
        A[3. Detecção de Anomalias\n- Concorrentes\n- Bots / Spam\n- Risco de Churn]
    end

    subgraph "Classificação Final"
        S[Lead Score: 0 a 100]
        R{Decisão}
        R -->|Score Alto| V[Encaminhar para Vendedor]
        R -->|Score Médio| N[Nutrição Automatizada]
        R -->|Score Baixo / Anomalia| D[Descarte / Flag Concorrente]
    end

    L --> F & E & A
    F & E & A --> S --> R
```

1. **Perfil (Fit ICP):** Avalia se o lead possui orçamento e autoridade decisória (C-Level, Diretores e Gerentes corporativos recebem maior ponderação que e-mails públicos ou cargos júnior).
2. **Interesse (Intenção de Compra):** Pede demo corporativa ou acessa página de preços tem peso significativamente superior a apenas assinar uma newsletter.
3. **Filtros de Proteção e Resiliência:** Detecção de e-mails corporativos de competidores, setores não-alvo (acadêmico, órgãos públicos B2G com processos licitatórios longos) e inconsistência cadastral.

---

## Arquitetura do Sistema

A arquitetura do projeto foi desenhada para garantir desacoplamento total entre transporte, regras de negócio e persistência de dados:

```mermaid
graph TD
    Client["Agente / Cliente MCP\n"] <-->|Protocolo MCP via HTTP| MCPServer["MCP Server Layer\n(FastAPI / MCP Python SDK)"]
    
    MCPServer <--> Services["Camada de Serviço & Regras de Negócio"]
    Services <--> LLMOrchestrator["Orquestrador de IA\n(LangChain / LangGraph)"]
    LLMOrchestrator <--> OpenAI["OpenAI API\n(Análise Semântica)"]
    
    Services <--> DB[("PostgreSQL 16\n(SQLAlchemy Async + asyncpg)")]
    
    LLMOrchestrator --> Phoenix["Arize Phoenix\n(Observabilidade de LLM)"]
```

### Destaques Arquiteturais:
- **Camada MCP Oficial:** Contratos de entrada e saída validados com schemas estritos via `pydantic`.
- **Persistência Assíncrona:** Acesso ao banco com `SQLAlchemy 2.0` no modo assíncrono sobre `asyncpg`.
- **Observabilidade OpenInference:** Instrumentação automática via OpenTelemetry reportando traces detalhados para o coletor do Arize Phoenix.
- **Camada de Testes com LLM Evaluation:** Validação de conformidade semântica com o framework `DeepEval`.

---

## Stack Tecnológica

| Categoria | Tecnologias |
| :--- | :--- |
| **Linguagem & Runtime** | Python 3.12 (Slim) |
| **Framework MCP & API** | MCP Python SDK (`mcp[httpx]`), FastAPI, Uvicorn |
| **Modelagem & Validação** | Pydantic V2, Pydantic-Settings |
| **IA & Orquestração** | LangChain, LangGraph |
| **Banco de Dados & ORM** | PostgreSQL 16 (Alpine), SQLAlchemy 2.0, Asyncpg |
| **Observabilidade & Tracing** | Arize Phoenix, OpenInference |
| **Testes & Qualidade** | Pytest, Pytest-Asyncio, DeepEval, Playwright |
| **Empacotamento & DevOps** | Docker, Poetry |

---

## Como Executar

### Pré-requisitos
- [Docker](https://www.docker.com/) e Docker Compose instalados
- [Poetry](https://python-poetry.org/) (opcional para execução local fora do Docker)
- Python 3.12+

### 1. Clonar o repositório e configurar ambiente
```bash
git clone https://github.com/matheusadam/Lead-Intelligence-MCP-PP.git
cd Lead-Intelligence-MCP-PP

# Copie o arquivo de variáveis de ambiente
cp .env.example .env
```

Edite o arquivo `.env` preenchendo sua chave da OpenAI e ajustando as portas se necessário:
```dotenv
OPENAI_API_KEY=sua-chave-aqui
DATABASE_URL=postgresql+asyncpg://admin:admin@localhost:5432/rd_leads
```

### 2. Subir o ambiente com Docker Compose
```bash
docker compose up -d --build
```

Os seguintes serviços estarão disponíveis:
- **MCP Server / Backend:** `http://localhost:4200`
- **Dashboard Arize Phoenix (Observabilidade):** `http://localhost:6006`
- **PostgreSQL Database:** `localhost:5432`

---

## Autor

Desenvolvido por **Matheus Adam**.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Matheus%20Adam-blue?logo=linkedin)](https://linkedin.com/in/matheus-adam-gabalda)
[![GitHub](https://img.shields.io/badge/GitHub-matheusadam-181717?logo=github)](https://github.com/Matheusadmg)

---
<div align="center">
  <sub>Projeto construído com foco em arquitetura limpa, engenharia de contexto para LLMs e observabilidade de ponta a ponta.</sub>
</div>
