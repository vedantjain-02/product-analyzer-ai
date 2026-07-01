import streamlit as st
import requests

st.set_page_config(
    page_title="Product Analyzer AI",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Product Analyzer AI")

uploaded_file = st.file_uploader(
    "Upload Product Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    st.image(uploaded_file, width=300)

    if st.button("Analyze Product"):

        with st.spinner("Analyzing Product..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type
                )
            }

            response = requests.post(
                "http://127.0.0.1:8000/api/v1/analyze",
                files=files
            )

            if response.status_code == 200:

                data = response.json()

                st.success("Analysis Completed")

                # OCR TEXT
                st.subheader("📄 Extracted Text")

                st.text_area(
                    "OCR Result",
                    data["extracted_text"],
                    height=200
                )

                # Harmful Ingredients
                st.subheader("⚠ Harmful Ingredients")

                harmful = data.get(
                    "harmful_ingredients",
                    []
                )

                if harmful:

                    for item in harmful:

                        st.error(
                            f"{item['ingredient']} "
                            f"({item['risk']})"
                        )

                else:

                    st.success(
                        "No harmful ingredients found"
                    )

                # AI Analysis
                ai = data["ai_analysis"]

                st.subheader("🤖 AI Analysis")

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(
                        "Category",
                        ai["category"]
                    )

                with col2:
                    st.metric(
                        "Health Score",
                        ai["health_score"]
                    )

                with col3:
                    st.metric(
                        "Risk Level",
                        ai["risk_level"]
                    )

                st.subheader("✅ Pros")

                for item in ai["pros"]:
                    st.write("•", item)

                st.subheader("❌ Cons")

                for item in ai["cons"]:
                    st.write("•", item)

                st.subheader("💡 Recommendation")

                st.info(
                    ai["recommendation"]
                )

                st.subheader(
                    "🥗 Better Alternatives"
                )

                for alt in ai["alternatives"]:
                    st.write("•", alt)

            else:

                st.error(
                    f"API Error: {response.text}"
                )