# LangChain Simple Chain using LCEL

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![LangChain](https://img.shields.io/badge/Framework-LangChain-green.svg)
![Google Gemini](https://img.shields.io/badge/LLM-Google%20Gemini-4285F4.svg)
![LCEL](https://img.shields.io/badge/Workflow-LCEL-orange.svg)
![Status](https://img.shields.io/badge/Project-Learning%20Project-purple.svg)

A beginner-friendly implementation of a **Simple Chain using LangChain Expression Language (LCEL)**. This project demonstrates how to connect a prompt template, a Google Gemini chat model, and an output parser into a single, readable workflow using LangChain's pipe operator (`|`).

The goal is to understand how individual components of a Generative AI application work together instead of making an isolated model call.

## 📌 Table of Contents

- [Overview](#-overview)
- [What Is a Simple Chain?](#-what-is-a-simple-chain)
- [Key Concepts](#-key-concepts)
- [How the Chain Works](#-how-the-chain-works)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Understanding the LCEL Pipeline](#-understanding-the-lcel-pipeline)
- [Example Workflow](#-example-workflow)
- [Learning Outcomes](#-learning-outcomes)
- [Possible Extensions](#-possible-extensions)
- [Security Best Practices](#-security-best-practices)
- [References](#-references)

## 🚀 Overview

A Simple Chain is one of the fundamental building blocks of LangChain applications. It combines multiple components into a unified workflow so that data can move from one step to the next automatically.

This project explores the basic LCEL pattern:

**Prompt Template → Language Model → Output Parser**

The implementation uses LangChain to prepare the prompt, Google Gemini to generate a response, and `StrOutputParser` to convert the model response into plain text.

This pattern provides a foundation for building more advanced Generative AI applications, including question-answering systems, text-generation tools, summarizers, and multi-step AI workflows.

## 🔗 What Is a Simple Chain?

A Simple Chain connects a series of processing components into one executable pipeline.

Without a chain, a developer may need to format messages, call a model, extract the response, and handle each step separately.

With LCEL, these components can be connected using the pipe operator (`|`).

```python
chain = prompt | model | parser
```

When the chain receives an input, the output from each component is passed to the next component automatically.

This makes the code easier to read, maintain, and extend.

## 🧠 Key Concepts

### 1. LangChain Expression Language (LCEL)

LCEL is a declarative way to compose LangChain components into workflows.

Its pipe operator (`|`) connects compatible components and creates a runnable sequence.

**Why it matters:**
- Makes workflows easier to understand.
- Reduces repetitive orchestration code.
- Supports reusable and composable components.
- Provides a consistent interface for executing chains.

### 2. ChatPromptTemplate

`ChatPromptTemplate` helps define structured messages for a chat model.

It can contain system instructions and human messages, along with placeholders for dynamic input.

For example, a prompt can be designed to answer questions about a user-provided topic.

### 3. Google Gemini

Google Gemini serves as the language model in this project.

It processes the formatted prompt and generates a response. The model name is determined by the configuration used in the Python script.

### 4. StrOutputParser

`StrOutputParser` converts a compatible language-model response into a plain string.

This is useful when the application needs readable text instead of the full model-response object.

### 5. Chain Execution with `invoke()`

The `invoke()` method executes the complete chain using the supplied input.

Instead of manually calling every component, the developer provides the input to the chain and receives its final output.

## ⚙️ How the Chain Works

The pipeline follows four basic steps:

1. **Input:** The application receives the required user input.
2. **Prompt formatting:** `ChatPromptTemplate` creates the messages sent to the model.
3. **Response generation:** Google Gemini generates a response from the formatted prompt.
4. **Output parsing:** `StrOutputParser` extracts the response as plain text.

The final result can then be displayed, saved, or passed to another processing component.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain Core | Prompt templates, runnables, and output parsing |
| LangChain Google GenAI | Integration with Google Gemini |
| Google Gemini | Language-model response generation |
| python-dotenv | Loading environment variables from a `.env` file |
| LCEL | Connecting the prompt, model, and parser |

## 📁 Project Structure

The repository contains a Python implementation and its documentation.

```text
langchain-simple-chain/
├── simple_chain.py   # Simple LCEL chain implementation
├── README.md         # Project documentation
└── .env              # Local API key configuration (created by you)
```

The `.env` file should remain local and should not be committed to GitHub. If your repository uses a different Python filename, replace `simple_chain.py` in the instructions below with the actual filename.

## 💻 Getting Started

### Prerequisites

Before running the project, make sure you have:

- Python 3.9 or a compatible newer version.
- A Google AI API key with access to the selected Gemini model.
- An internet connection for API requests.
- Basic familiarity with Python and language models.

### Step 1: Clone the Repository

```bash
git clone https://github.com/mani787060/langchain-simple-chain.git
cd langchain-simple-chain
```

### Step 2: Create a Virtual Environment

Creating an isolated environment helps prevent dependency conflicts with other Python projects.

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux or macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install Dependencies

```bash
python -m pip install --upgrade pip
pip install langchain-core langchain-google-genai python-dotenv
```

These packages provide the core LCEL components, Google Gemini integration, and environment-variable loading.

### Step 4: Configure the Google API Key

Obtain an API key through [Google AI Studio](https://aistudio.google.com/).

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

Replace the placeholder with your own key.

**Important:** Never publish your real API key or commit your `.env` file to a public repository.

### Step 5: Run the Python Script

```bash
python simple_chain.py
```

The script should execute the chain and display the generated response, assuming the model configuration and API credentials are valid.

## 🔍 Understanding the LCEL Pipeline

The central idea behind this project is connecting compatible components into a single chain.

```python
chain = prompt | model | parser
```

Each component has a specific responsibility:

- `prompt` prepares the input messages.
- `model` generates the response.
- `parser` converts the response into the desired output format.

The chain can then be executed:

```python
response = chain.invoke({
    # Supply the input variables required by your prompt
})

print(response)
```

The dictionary keys must match the input variables defined in the actual prompt template. The code above illustrates the execution pattern; use the exact variable names from `simple_chain.py`.

## 🧪 Example Workflow

Suppose the prompt asks the model to explain a Generative AI concept in simple language.

The workflow would be:

**Input topic → Prompt formatting → Gemini response → Plain-text output**

The resulting text can be printed in the terminal or used by another application.

Actual output depends on the prompt, model configuration, and model response, so the repository does not assume a fixed response.

## 🎯 Learning Outcomes

By exploring this project, you can develop an understanding of:

- The fundamentals of LangChain chains.
- How LCEL connects multiple components.
- How `ChatPromptTemplate` structures model inputs.
- How to integrate Google Gemini with LangChain.
- How `StrOutputParser` handles model responses.
- How `invoke()` executes a complete runnable pipeline.
- How to configure API credentials using environment variables.
- How to structure the foundations of a larger LLM application.

## 🚀 Possible Extensions

Once the basic chain is working, it can be extended with additional functionality:

- **Prompt customization:** Add roles, instructions, and dynamic input variables.
- **Output transformation:** Add another runnable to process the generated text.
- **Sequential workflows:** Connect multiple chains so that one step feeds the next.
- **Parallel execution:** Run independent processing steps concurrently.
- **Conditional workflows:** Route inputs through different processing paths.
- **Retrieval-Augmented Generation (RAG):** Add document retrieval to ground responses in external information.

These are possible extensions, not features that the current Simple Chain necessarily implements.

## 🔐 Security Best Practices

- Keep API keys in environment variables rather than hardcoding them.
- Add `.env` to `.gitignore`.
- Never commit credentials, access tokens, or other secrets.
- Avoid sharing API keys in screenshots, logs, or public discussions.
- Review API usage and applicable billing limits before running repeated requests.

A minimal `.gitignore` entry is:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

## 📚 References

- [LangChain Documentation](https://python.langchain.com/docs/introduction/)
- [LangChain Expression Language](https://python.langchain.com/docs/concepts/lcel/)
- [LangChain Google GenAI Integration](https://python.langchain.com/docs/integrations/chat/google_generative_ai/)
- [Google AI Studio](https://aistudio.google.com/)
- [Python Documentation](https://docs.python.org/3/)
