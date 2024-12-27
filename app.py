import streamlit as st
from PIL import Image
import os
from model import (
    tesseract_ocr_extract,
    tesseract_ocr_extract_with_preprocessing,
    trocr_printedText_extract,
    trocr_handWrittenText_extract,
    easyocr_extract,
    ollama_ocr
)

def main():
    st.title("🎩 Vision OCR")
    uploaded_file = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg'])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_container_width =True)
        
        with open("temp_image.png", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        model_option = st.selectbox(
            'Select OCR Model',
            [
                'Tesseract OCR',
                'Tesseract OCR with Preprocessing',
                'TrOCR (Printed Text)',
                'TrOCR (Handwritten Text)',
                'EasyOCR',
                'Ollama OCR'
            ]
        )
        
        if st.button('Extract Text'):
            with st.spinner('Extracting text...'):
                try:
                    if model_option == 'Tesseract OCR':
                        result = tesseract_ocr_extract("temp_image.png")
                    elif model_option == 'Tesseract OCR with Preprocessing':
                        result = tesseract_ocr_extract_with_preprocessing("temp_image.png")
                    elif model_option == 'TrOCR (Printed Text)':
                        result = trocr_printedText_extract("temp_image.png")
                    elif model_option == 'TrOCR (Handwritten Text)':
                        result = trocr_handWrittenText_extract("temp_image.png")
                    elif model_option == 'EasyOCR':
                        result = easyocr_extract("temp_image.png")
                        result = '\n'.join(result) if result else "No text detected"
                    else:
                        result = ollama_ocr("temp_image.png")
                        if result is None or result.strip() == "":
                            result = "No text detected or error in Ollama OCR processing"
                    
                    st.subheader("Extracted Text:")
                    if result and result.strip():
                        st.text_area("Extracted text:", value=result, height=200)
                    else:
                        st.warning("No text was detected in the image")
                
                except Exception as e:
                    st.error(f"An error occurred during text extraction: {str(e)}")
                    st.error("Please try a different OCR model or check if the image is clear and properly formatted")
                
                finally:
                    if os.path.exists("temp_image.png"):
                        os.remove("temp_image.png")

if __name__ == '__main__':
    main()
