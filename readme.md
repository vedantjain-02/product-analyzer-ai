🥗 Product Analyzer AI

An AI-powered food product analyzer that helps users understand packaged-food ingredients, health considerations, potential risks, pros, cons, and healthier alternatives.

The application combines a Streamlit frontend, FastAPI backend, and Google Gemini for AI-powered ingredient analysis.

✨ Features

📷 Upload a product/ingredient image through the Streamlit UI

🔍 Extract and analyze ingredient information

🤖 AI-powered food-safety and ingredient analysis using Google Gemini

❤️ Health score and risk-level assessment

✅ Pros and ⚠️ cons of the product

💡 Personalized recommendation

🔄 Suggested healthier alternatives

📦 REST API powered by FastAPI

🧩 Modular backend structure for easy extension

Disclaimer: Product Analyzer AI is an informational tool and is not a substitute for professional medical, nutritional, or dietary advice.

🏗️ Architecture

┌──────────────────────┐
│   Streamlit Frontend │
│      frontend.py     │
└──────────┬───────────┘
           │
           │ HTTP POST
           ▼
┌──────────────────────┐
│     FastAPI Backend  │
│       app/main.py    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Analyze API Route  │
│ app/api/analyze.py   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    AI Service        │
│ app/services/        │
│     ai_service.py    │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    Google Gemini     │
└──────────────────────┘

📁 Project Structure

product-analyzer-ai/
│
├── app/
│   ├── api/
│   │   └── analyze.py
│   ├── database/
│   ├── schemas/
│   ├── services/
│   │   └── ai_service.py
│   └── main.py
│
├── uploads/
├── frontend.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md

🛠️ Tech Stack

Technology

Purpose

Python

Core application language

Streamlit

Frontend / UI

FastAPI

Backend REST API

Uvicorn

ASGI server

Google Gemini

AI-powered product analysis

Requests

Frontend → backend HTTP communication

python-dotenv

Environment variable management

🚀 Getting Started

1. Clone the repository

git clone <your-github-repository-url>
cd product-analyzer-ai

2. Create a virtual environment

Windows:

python -m venv venv

Activate it:

venv\Scripts\activate

macOS / Linux:

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

If requirements.txt is not available yet:

pip install streamlit fastapi uvicorn requests python-dotenv google-generativeai

4. Configure Gemini API

Create a .env file in the project root:

GEMINI_API_KEY=your_gemini_api_key

Never commit your real API key to GitHub.

Make sure .env is included in .gitignore:

.env
venv/
__pycache__/
*.pyc

▶️ Running the Application

The project has two processes: the FastAPI backend and the Streamlit frontend.

Terminal 1 — Start FastAPI

From the project root:

uvicorn app.main:app --reload

Backend:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs

Terminal 2 — Start Streamlit

Open another terminal in the project directory and activate the virtual environment:

venv\Scripts\activate

Then run:

streamlit run frontend.py

Streamlit will normally be available at:

http://localhost:8501

🔌 API

Analyze Product

POST /api/v1/analyze

The endpoint accepts the product information/image sent by the frontend and returns an AI-generated analysis.

Example response:

{
  "category": "Packaged Snack",
  "health_score": "7/10",
  "risk_level": "Moderate",
  "pros": [
    "Contains some useful ingredients"
  ],
  "cons": [
    "May contain added sugar",
    "Relatively high sodium"
  ],
  "recommendation": "Consume occasionally as part of a balanced diet.",
  "alternatives": [
    "Lower-sodium alternatives",
    "Products with fewer added sugars"
  ]
}

You can test the API interactively using the FastAPI Swagger UI:

http://127.0.0.1:8000/docs

🔐 Environment Variables

Variable

Required

Description

GEMINI_API_KEY

Yes

Google Gemini API key

🧪 Development

To run the backend with automatic reload:

uvicorn app.main:app --reload

To run Streamlit:

streamlit run frontend.py

Before opening a bug report, verify that:

The virtual environment is activated.

Dependencies are installed.

.env contains a valid GEMINI_API_KEY.

FastAPI is running on port 8000.

Streamlit is running on port 8501.

🐛 Common Issues

Connection refused on port 8000

Make sure the FastAPI backend is running:

uvicorn app.main:app --reload

No API_KEY or ADC found

Check that .env contains:

GEMINI_API_KEY=your_gemini_api_key

Also make sure the .env file is in the project root.

GEMINI_API_KEY returns None

Check that the file is named exactly:

.env

and not:

.env.txt

Also ensure python-dotenv is installed:

pip install python-dotenv

🔮 Future Improvements

Better OCR and ingredient extraction

Nutrition-label analysis

Barcode scanning

User accounts and analysis history

Product comparison

Personalized dietary preferences

Improved food-allergen detection

Automated tests

Docker support

Cloud deployment

Migration to the current Google Gemini Python SDK

🤝 Contributing

Contributions are welcome!

Fork the repository

Create a feature branch

git checkout -b feature/my-feature

Commit your changes

git commit -m "Add my feature"

Push the branch

git push origin feature/my-feature

Open a Pull Request

📄 License

This project is licensed under the MIT License.

See LICENSE for details.

👨‍💻 Author

vedant jain

If you find this project useful, consider giving the repository a ⭐ on GitHub.

Built with Python, FastAPI, Streamlit, and Google Gemini.