import streamlit as st
from PIL import Image
import easyocr
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import torch
from PIL import Image
import pytesseract
import cv2
import numpy as np
from IPython.display import display
from ollama_ocr import OCRProcessor
import requests
import base64
import json

def tesseract_ocr_extract(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        return f"Error during Tesseract OCR: {str(e)}"


def preprocess_image_for_tesseract(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    _, image = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY)
    processed_image_path = "preprocessed_image.png"
    cv2.imwrite(processed_image_path, image)
    return processed_image_path

def tesseract_ocr_extract_with_preprocessing(image_path):
    processed_image_path = preprocess_image_for_tesseract(image_path)
    return tesseract_ocr_extract(processed_image_path)

def trocr_printedText_extract(image_path):
    processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-printed")
    model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-printed")
    image = Image.open(image_path).convert("RGB")
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values)
    text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return text

def trocr_handWrittenText_extract(image_path):
    processor = TrOCRProcessor.from_pretrained("microsoft/trocr-large-handwritten")
    model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-large-handwritten")
    image = Image.open(image_path).convert("RGB")
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values)
    text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return text

def easyocr_extract(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path,detail=0) 
    return result

def ollama_ocr(image_path):
    try:
        ocr = OCRProcessor(model_name='llama3.2-vision:11b')
        result = ocr.process_image(
            image_path=image_path,
            format_type="markdown"
        )
        # Add error checking
        if result is None or result.strip() == "":
            return "No text detected by Ollama OCR"
        return result
    except Exception as e:
        return f"Error in Ollama OCR processing: {str(e)}"




