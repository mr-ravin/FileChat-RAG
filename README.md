# FileChat-RAG

FileChat-RAG is a simple Retrieval-Augmented Generation (RAG) system that allows users to ask questions about the contents of various file formats. It extracts text from PDFs, JSON, text files(.txt, .doc, .docx, .md), and code files, then enables interactive conversations using an LLM powered by Ollama.

## Project Structure
```
📂 FileChat-RAG
 ├── main.py          # Main script for document interaction
 ├── README.md        # Project documentation
 ├── requirements.txt # Details of required libraries and their version
```

## 🔧 Development Details
- **👨‍💻 Developer:** [Ravin Kumar](https://mr-ravin.github.io)
- **📂 GitHub Repository:** [https://github.com/mr-ravin/FileChat-RAG](https://github.com/mr-ravin/FileChat-RAG)

## Features
- Supports text extraction from:
  - **PDFs** (.pdf)
  - **Text files** (.txt, .doc, .docx, .md)
  - **JSON files** (.json)
  - **Code files** (.py, .cpp, .java)
- Uses FAISS for efficient text retrieval
- Enables conversational interaction with documents
- Works with Ollama LLM (Gemma 3:1B by default)

## Installation
### Prerequisites
- Python 3.8+
- Ollama installed ([installation guide](https://ollama.com/))
- Required Python packages:
  
  ```sh
  pip install -r requirements.txt
  ```
  
  *(For GPU acceleration, install `faiss-gpu` instead of `faiss-cpu`)*

## Usage
### Installing and running Ollama Server
- Install Ollama Server:
```sh
curl -fsSL https://ollama.com/install.sh | sh
```
- Ensure the LLM is present inside the Ollama Server:
```sh
ollama pull gemma3:1b
```
- Ensure the Embedding Model is present inside the Ollama Server:
```sh
ollama pull all-minilm
```
- Ensure that the Ollama server is running:

```sh
ollama serve &
```

### Run FileChat-RAG
To interact with a specific file, use:

```sh
python main.py --path /path/to/your/file.pdf
```

Example:

```sh
python main.py --path ./sample.pdf
```
```sh
python main.py --path ./sample.json
```
```sh
python main.py --path ./sample.txt
```
```sh
python main.py --path ./sample.py
```

### Interactive Chat
```sh
python main.py --path Book_TheEngineersPlan.pdf
```
Once the script starts, you can ask questions about the file content:

```
Ask me anything! (Type /quit to exit) >>> What is the summary of the book- The Engineer's Plan ?
>>> [AI-generated response]
```
----

## License
```
Copyright (c) 2025 Ravin Kumar
Website: https://mr-ravin.github.io

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation 
files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, 
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the 
Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
