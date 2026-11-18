
# 🛍️ StoreAI — Assistente Virtual Inteligente

O StoreAI é um projeto de chatbot desenvolvido em Python, utilizando Streamlit e a API Google Gemini, com o objetivo de simular o atendimento virtual de uma loja online.

A aplicação permite que clientes consultem produtos, preços, estoque e informações disponíveis no catálogo, utilizando inteligência artificial para interpretar perguntas e gerar respostas.

Além do desenvolvimento da aplicação, o projeto também explora testes funcionais e fundamentos de segurança em aplicações baseadas em modelos de linguagem (LLMs).

## 🎯 Objetivos do projeto

- Desenvolver um assistente virtual integrado à inteligência artificial.
- Consultar informações de um catálogo de produtos.
- Evitar respostas comerciais sem respaldo nos dados disponíveis.
- Aplicar instruções de segurança ao comportamento do modelo.
- Explorar testes de qualidade e segurança em aplicações com IA.

## 🛠️ Tecnologias utilizadas

- Python
- Streamlit
- Google Gemini API
- Google Gen AI SDK
- Python-dotenv

## ⚙️ Funcionalidades

- Atendimento por meio de interface conversacional.
- Consulta de preços e disponibilidade.
- Respostas baseadas em catálogo de produtos.
- Histórico de conversas durante a sessão.
- Instruções de comportamento e segurança para o assistente.
- Tratamento de informações não disponíveis no catálogo.

## 🧪 Testes funcionais e de segurança

Foram realizados oito casos de teste para avaliar o comportamento do assistente diante de perguntas comerciais e tentativas de manipulação.

| Nº | Cenário | Resultado observado |
|---|---|---|
| 01 | Consulta de preço | Aprovado |
| 02 | Consulta de estoque | Aprovado |
| 03 | Solicitação de desconto indevido | Aprovado |
| 04 | Falsa autoridade de gerente | Aprovado |
| 05 | Tentativa de extração de instruções internas | Aprovado |
| 06 | Instrução maliciosa em conteúdo citado | Aprovado |
| 07 | Tentativa de manipulação do catálogo | Aprovado |
| 08 | Solicitação de informações inexistentes | Aprovado |

### Principais aspectos avaliados

- Prompt Injection
- Prompt Extraction
- Confiabilidade das informações comerciais
- Resistência a instruções conflitantes
- Tratamento de informações ausentes

**Observação:** os resultados representam o comportamento observado nos oito testes realizados. Eles não constituem uma auditoria completa nem comprovam a segurança integral da aplicação.

## 📦 Catálogo de demonstração

O projeto utiliza um catálogo fictício contendo:

- Samsung Galaxy A54
- Samsung Galaxy S24 Ultra
- iPhone 15
- Motorola Edge 50

Os dados são utilizados para simular consultas comerciais e verificar se o assistente respeita as informações fornecidas.

## 🚀 Como executar o projeto

### 1. Clonar o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

### 2. Entrar na pasta

```bash
cd StoreIA
```

### 3. Criar ambiente virtual

```bash
python -m venv .venv
```

### 4. Ativar o ambiente virtual

Windows PowerShell:

```powershell
.venv\Scripts\Activate
```

### 5. Instalar dependências

```bash
pip install -r requirements.txt
```

### 6. Configurar a API

Crie um arquivo chamado `.env` na raiz do projeto:

```env
GEMINI_API_KEY=sua_chave_aqui
```

Não compartilhe sua chave de API nem a envie ao GitHub.

### 7. Executar

```bash
streamlit run app.py
```

## 📚 Aprendizados

Durante o desenvolvimento, foram explorados conceitos de:

- Desenvolvimento de aplicações com Python.
- Integração com APIs de inteligência artificial.
- Engenharia de prompts.
- Testes funcionais.
- Fundamentos de Quality Assurance (QA).
- Segurança em aplicações baseadas em LLMs.
- OWASP Top 10 for LLM Applications.

## 👩‍💻 Sobre o desenvolvimento

Projeto desenvolvido como parte da minha jornada de aprendizado em programação, Quality Assurance e cibersegurança.

O objetivo é aplicar conhecimentos na prática, compreender o comportamento de aplicações com inteligência artificial e desenvolver soluções considerando qualidade, confiabilidade e segurança.

---

**StoreAI — Inteligência artificial aplicada ao atendimento.**
