# Vision OCR - Text Extraction Application

A Streamlit-based web application that provides multiple OCR (Optical Character Recognition) options for extracting text from images. The application supports various OCR models and methods, allowing users to choose the most suitable one for their specific needs.

## Features

- Multiple OCR Models Support:
  - Tesseract OCR
  - Tesseract OCR with Preprocessing
  - TrOCR (Printed Text)
  - TrOCR (Handwritten Text)
  - EasyOCR
  - Ollama Vision OCR

- User-friendly Interface:
  - Simple image upload
  - Model selection dropdown
  - Real-time text extraction
  - Clear result display

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/vision-ocr.git
cd vision-ocr
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Tesseract OCR:
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

5. Install Ollama:
- Download from: https://ollama.ai
- Start the Ollama service:
  ```bash
  ollama serve
  ```
- Pull the required vision model:
  ```bash
  ollama pull bakllava
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

## Project Structure

```
vision-ocr/
├── app.py              # Streamlit application file
├── model.py            # OCR model implementations
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## Requirements

- Python 3.8+
- Tesseract OCR
- Ollama
- See requirements.txt for Python package dependencies

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Tesseract OCR
- EasyOCR
- Microsoft's TrOCR
- Ollama
- Streamlit
