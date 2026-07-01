from fastapi import FastAPI
from app.api.analyze import router as analyze_router

app = FastAPI(title="AI Product Analyzer")

app.include_router(
    analyze_router,
    prefix="/api/v1",
    tags=["Product Analysis"]
)


@app.get("/")
def root():
    return {"message": "AI Product Analyzer Running"}