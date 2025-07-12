# Robotic_1.ipynb Documentation

## Overview

`Robotic_1.ipynb` is a Jupyter notebook that demonstrates an AI-powered workflow for automated extraction and evaluation of handwritten or scanned exam answers, primarily for physics problems. It leverages Google Gemini (Generative AI), LangChain, and Retrieval-Augmented Generation (RAG) to:

- Extract and describe text from images (e.g., scanned answer scripts)
- Parse and process PDF documents containing exam questions and answers
- Compare extracted answers with marking rubrics
- Auto-evaluate answers and generate detailed feedback

## Main Components

### 1. Text Extraction from Images
- Uses Google Gemini API to extract and describe content from uploaded images (e.g., `udvash.jpg`, `1.png`).
- The extracted text and a summary are generated for further evaluation.

### 2. PDF Processing
- Loads and splits PDF files (e.g., `1.pdf`, `2.pdf`) using `PyPDFLoader`.
- Extracts page-wise content for granular analysis and marking.

### 3. Retrieval-Augmented Evaluation
- Embeds and indexes PDF content using LangChain and Chroma for semantic search.
- Uses `RetrievalQA` to answer questions and compare student responses with the marking scheme.

### 4. Automated Marking & Feedback
- Custom system instructions allow the LLM to act as an examiner, providing marks and feedback based on a provided rubric.
- Generates a breakdown of marks and explanations for each step.

## Usage

1. **Install Dependencies**: The notebook auto-installs all required packages (Google Gemini, LangChain, ChromaDB, etc.).
2. **Upload Files**: Add your image and PDF files to the Colab environment.
3. **Run Cells**: Execute the notebook cells in order to extract, process, and evaluate answers.
4. **Customize**: Adjust the system instructions or upload your own marking schemes as needed.

## Example Workflow
- Upload an image or PDF of a student's answer.
- Extract the text and description using Gemini.
- Load and split the PDF for question/answer extraction.
- Use RAG to compare the answer with the rubric and auto-generate marks and feedback.

## Requirements
- Google Colab (recommended)
- Google Gemini API Key (set as `userdata.get('GOOGLE_API_KEY')`)
- PDF/image files of student answers

## References
- [Google Gemini](https://ai.google.dev/)
- [LangChain](https://python.langchain.com/)
- [Google Colab](https://colab.research.google.com/)

---

For more details, see the `README.md` in this directory.
