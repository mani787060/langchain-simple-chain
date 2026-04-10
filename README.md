# LangChain Simple Chain (LCEL)
[![LangChain](https://img.shields.io/badge/Framework-LangChain-green)](https://www.langchain.com/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/Model-Google%20Gemini-4285F4)](https://ai.google.dev/)

## 🏗️ Project Overview
This repository contains the foundational implementation of a **Simple Chain** using LangChain Expression Language (LCEL). Instead of handling inputs and outputs manually, this project demonstrates how to "pipe" different components together to create a smooth, readable, and maintainable data flow. This is the industry-standard way to build modular AI applications.

---

## 🛠️ Key Technical Implementations

### 1. The LCEL Pipeline
* **Unified Syntax:** Using the `|` operator to connect the Prompt, Model, and Parser.
* **Declarative Logic:** Defining *what* the chain should do rather than writing complex imperative code for every step.

### 2. Component Breakdown
* **Prompt Template:** Using `ChatPromptTemplate` to define structured, reusable system and human messages.
* **Model Orchestration:** Interfacing with Gemini Pro for high-quality text generation.
* **Output Parsing:** Utilizing `StrOutputParser` to extract clean text from the model's response metadata.

### 3. Developer Benefits
* **Readability:** Reducing 20 lines of manual code into a single, elegant chain.
* **Extensibility:** Easily swapping models or adding extra processing steps (like translation or logging) without rewriting the entire logic.

---

## 💻 Tech Stack
* **Language:** Python 3.9+
* **Orchestration:** LangChain (`langchain-core`, `langchain-google-genai`)
* **Model:** Google Gemini Pro
* **Environment:** `python-dotenv`

---

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/langchain-simple-chain-lcel.git](https://github.com/your-username/langchain-simple-chain-lcel.git)


2. **Install Dependencies:**
   ```bash
   pip install -U langchain-core langchain-google-genai python-dotenv

3. **Setup API Key:**
   Create a .env file in the root directory:
   ```bash
   GOOGLE_API_KEY=your_gemini_key_here

4. **Run the Chain:**
   ```bash
   python simple_chain.py
