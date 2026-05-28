# MedAssist Guardrail - MVP

## Descrição do Projeto
O **MedAssist Guardrail** é um protótipo funcional de um chatbot para triagem inicial de sintomas, focado em segurança e ética no uso de IA generativa (LLMs). O sistema implementa mecanismos de **Guardrails** (filtros de entrada e saída) e **Human-in-the-Loop (HITL)** para garantir que a IA não forneça diagnósticos definitivos, não exponha dados sensíveis e peça intervenção humana em casos de emergência.

Este projeto faz parte da disciplina de **Tópicos em Engenharia de Software** da PUC-Campinas (2026).

## Funcionalidades Principais
- **Input Guardrail**: Detecção de PII (Informações Pessoais Identificáveis) e bloqueio de linguagem inadequada.
- **Output Guardrail**: Bloqueio de recomendações médicas diretas e diagnósticos conclusivos.
- **Human-in-the-Loop (HITL)**: Casos classificados como "alto risco" ou "emergência" são interrompidos para aprovação humana via interface.
- **Painel de Métricas**: Visualização de logs de segurança e intervenções realizadas.

## Stack Técnica
- **Linguagem**: Python 3.10+
- **Orquestração**: LangGraph
- **Segurança**: Guardrails AI (Lógica Customizada)
- **Interface**: Streamlit
- **LLM**: Groq Llama 3.3 70B Versatile

## Estrutura de Arquivos e Responsabilidades
Para atender aos requisitos de commits distribuídos, o projeto foi modularizado:
1. `README.md`: Documentação e visão geral (Responsável: Gabriella Santos).
2. `guardrails_logic.py`: Implementação dos filtros de segurança de entrada e saída (Responsável: Rodolfo Abrahão).
3. `llm_service.py`: Abstração da API da Groq (Responsável: Paulo Corrêa).
4. `workflow.py`: Definição do grafo de estados e lógica HITL (Responsável: Rodolfo Infantini).
5. `interface.py`: Interface web e chat com Streamlit (Responsável: Rodolfo Infantini).
6. `logger_metrics.py`: Sistema de logs e métricas de segurança (Responsável: Marcella Brito).


## Como Executar
1. Clone o repositório.
2. Crie um ambiente virtual: `python -m venv venv`.
3. Ative o ambiente: `source venv/bin/activate` (Linux/macOS) ou `venv\Scripts\activate` (Windows).
4. Instale as dependências: `pip install -r requirements.txt`.
5. Configure sua chave da Groq no arquivo `.env` (ou variável de ambiente) (GROQ_API_KEY).
6. Execute o app: `streamlit run interface.py`.

---
**Grupo G10**: Gabriella Santos, Marcella Brito, Paulo Corrêa, Rodolfo Abrahão, Rodolfo Infantini.
