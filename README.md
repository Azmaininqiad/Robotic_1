Robotic_1: Automated Physics Solution Evaluation & Text Extraction
This project demonstrates an AI-powered workflow for:

Extracting and understanding handwritten or scanned text/images (e.g., exam scripts, physics problems)
Comparing extracted solutions with sample answers/rubrics
Auto-evaluating exam-style answers using Retrieval-Augmented Generation (RAG) and LLMs
Supporting PDF and image uploads for flexible document processing
Features
Text Extraction from Images: Utilizes Google Gemini API to extract and describe handwritten or printed content from images.
Automated Answer Evaluation: Uses LangChain and Gemini to compare student solutions against marking rubrics and provide detailed marking breakdowns.
PDF Processing: Extracts and splits PDF-based questions and solutions for granular analysis.
Flexible Marking: Customizes feedback and scoring based on provided marks distribution and answer structure.
Usage Outline
Install Requirements The notebook auto-installs all dependencies, including:

google-generativeai
google-cloud-aiplatform
langchain, langchain-community, langchain-google-genai
chromadb, pypdf, sentence_transformers, llama-index
Image-to-Text Extraction

Upload a handwritten/scanned image (e.g., udvash.jpg, 1.png)
Extract the text and a descriptive summary using Gemini
PDF Question/Answer Extraction

Load and split exam PDFs (e.g., 1.pdf, 2.pdf) using PyPDFLoader
Display parsed question/answer content, including marking schemes
Retrieval-Augmented Evaluation

Index and embed the PDF content for semantic search
Use LangChain’s RetrievalQA to answer/explain based on extracted student response and rubric
Marking/Feedback Generation

Provide a question, student answer, and marking scheme
Gemini LLM generates total marks and step-wise feedback
Example Workflow
Python
# 1. Install required packages (auto-installed in notebook)
!pip install google-generativeai --quiet
!pip install --upgrade google-cloud-aiplatform --quiet
!pip install -U langchain-community chromadb pypdf sentence_transformers

# 2. Extract text and description from image
import google.generativeai as genai
from google.colab import userdata
GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
sample_file = genai.upload_file(path="/content/udvash.jpg", display_name="Jetpack drawing")
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest")
response = model.generate_content([sample_file, "Extract the text and describe the image from this picture"])
print(response.text)

# 3. Load and split exam PDFs
from langchain.document_loaders import PyPDFLoader
pdf_loader = PyPDFLoader("/content/1.pdf")
pages = pdf_loader.load_and_split()
print(pages[0].page_content)

# 4. Run retrieval-augmented marking
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=GOOGLE_API_KEY)
texts = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100).split_text('\n\n'.join(p.page_content for p in pages))
vector_index = Chroma.from_texts(texts, embeddings).as_retriever(search_kwargs={"k":5})
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY, system_instruction="You are an examiner...")
qa_chain = RetrievalQA.from_chain_type(model, retriever=vector_index, return_source_documents=True)
result = qa_chain({"query": response.text})
print(result["result"])
Example Marking Output
Code
'The provided handwritten calculation uses an incorrect formula and values. The correct formula, as shown in the sample answer, is v = j/(ne), where j is current density, n is the number of electrons per unit volume, and e is the charge of an electron. ...'
Requirements
Python 3.10+ (Google Colab recommended)
Google Gemini API Key (set as userdata.get('GOOGLE_API_KEY') in Colab)
PDF and/or image files of student answers
File Structure
Robotic.ipynb – Main notebook with all code and workflow
/content/1.pdf, /content/2.pdf – Sample PDF exam scripts
/content/udvash.jpg, /content/1.png – Sample handwritten answer images
Customization
Adjust the system_instruction prompt to change marking criteria or feedback style.
Upload your own PDFs/images for different subjects or marking schemes.
License
This project is for academic/research/demo use. Please ensure you handle student data and API keys securely.

Acknowledgements
Google Gemini (Generative AI)
LangChain
Google Colab
