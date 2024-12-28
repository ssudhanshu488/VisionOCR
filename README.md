# 🎩 Vision OCR 

A Streamlit-based web application that provides multiple OCR (Optical Character Recognition) options for extracting text from images. The application supports various OCR models and methods, allowing users to choose the most suitable one for their specific needs.

## Features

- Multiple OCR Models Support:
  - Tesseract OCR
  - Tesseract OCR with Preprocessing
  - TrOCR (Printed Text)
  - TrOCR (Handwritten Text)
  - EasyOCR
  - Ollama Vision OCR


## Installation

1. Clone the repository:
```bash
git clone https://github.com/ssudhanshu488/vision-ocr.git
cd vision-ocr
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install Tesseract OCR:
- For Ubuntu/Debian:
  ```bash
  sudo apt-get install tesseract-ocr
  ```
- For macOS:
  ```bash
  brew install tesseract
  ```
- For Windows:
  Download and install from: https://github.com/UB-Mannheim/tesseract/wiki

4. Install Ollama:
- Download from: https://ollama.ai
- Start the Ollama service:
  ```bash
  ollama serve
  ```
- Pull the required vision model:
  ```bash
  ollama pull llama3.2-vision:11b
  ```

## Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to http://localhost:8501

3. Upload an image containing text

4. Select your preferred OCR model

5. Click "Extract Text" to process the image
