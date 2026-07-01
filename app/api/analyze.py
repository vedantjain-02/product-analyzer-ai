from fastapi import APIRouter, UploadFile, File
from app.services.ocr_service import extract_text
from app.services.ingredient_service import analyze_ingredients
from app.services.ai_service import analyze_product

router = APIRouter()

@router.post("/analyze")
async def analyze_product_api(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text(file_path)

    harmful = analyze_ingredients(text)

    # Gemini Analysis
    ai_analysis = analyze_product(text)

    return {
        "extracted_text": text,
        "harmful_ingredients": harmful,
        "ai_analysis": ai_analysis
    }