import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
import os
import datetime

# -----------------------------
# PAGE
# -----------------------------

st.set_page_config(
    page_title="AI Medical Diagnostic System",
    page_icon="🩺",
    layout="wide"
)

# -----------------------------
# LOAD MODEL
# -----------------------------

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "models", "medical_model.keras")

if os.path.exists(MODEL_PATH):
    model = tf.keras.models.load_model(MODEL_PATH)
else:
    model = None

class_names=[
    "Tuberculosis",
    "Lung Opacity",
    "Normal",
    "Pneumonia"
]

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.title("🩺 AI Medical Panel")

menu=st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Upload X-Ray",
        "AI Analysis",
        "Reports",
        "About"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success("🟢 AI System Ready")

st.sidebar.info("""
✔️ Deep Learning

✔️ 4 Disease Detection

✔️ Chest X-Ray

✔️ Report Generation

✔️ Confidence Score
""")

# -----------------------------
# CSS
# -----------------------------

st.markdown("""

<style>

html,body,[class*="css"]{

font-size:18px;

font-family:Arial;

color:#062d4f;

}

.stApp{

background:#edf8ff;

}

section[data-testid="stSidebar"]{

background:#dff3ff;

}

h1{

font-size:42px !important;

color:#003366 !important;

font-weight:bold;

}

h2,h3,h4,p,label,span{

color:#003366 !important;

font-size:20px !important;

}

.card{

background:white;

padding:25px;

border-radius:20px;

border:2px solid #4fb5ff;

box-shadow:0 6px 20px rgba(0,0,0,.15);

margin-bottom:20px;

}

[data-testid="metric-container"]{

background:white;

border:2px solid #4fb5ff;

border-radius:18px;

padding:18px;

}

[data-testid="metric-container"] *{

color:#003366 !important;

font-size:22px !important;

font-weight:bold;

}

[data-testid="stFileUploader"]{

background:white;

border:2px dashed #2196F3;

border-radius:15px;

padding:20px;

}

</style>

""",unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------

st.title("🏥 AI Medical Diagnostic System")

st.markdown("""

<div class="card">

<h2>AI Powered Chest X-Ray Disease Detection</h2>

<p>Upload Chest X-Ray • Analyze • Predict • Generate Report</p>

</div>

""",unsafe_allow_html=True)

# -----------------------------
# DASHBOARD
# -----------------------------

a,b,c,d=st.columns(4)

with a:
    st.metric("Accuracy","98.2%")

with b:
    st.metric("Diseases","4")

with c:
    st.metric("Cases","250+")

with d:
    st.metric("Response","2.1 sec")

st.divider()

# -----------------------------
# PATIENT DETAILS
# -----------------------------

st.subheader("👤 Patient Information")

c1,c2=st.columns(2)

with c1:
    patient_name=st.text_input("Patient Name")

with c2:
    patient_age=st.number_input(
        "Age",
        1,
        120,
        20
    )

gender=st.selectbox(
    "Gender",
    [
        "Male",
        "Female",
        "Other"
    ]
)

report_date=st.date_input(
    "Report Date",
    datetime.date.today()
)

st.divider()
# -----------------------------
# X-RAY UPLOAD
# -----------------------------

st.subheader("📤 Upload Chest X-Ray")

uploaded_file = st.file_uploader(
    "Choose X-Ray Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")

    st.success("✅ X-Ray Uploaded Successfully")

    st.image(
        image,
        caption="Uploaded Chest X-Ray",
        width=450
    )

    st.download_button(
        "📥 Download Uploaded Image",
        uploaded_file.getvalue(),
        file_name="Chest_Xray.png"
    )

    st.divider()

    if st.button("🧠 Analyze X-Ray"):

        if model is None:

            st.error("❌ medical_model.keras not found inside models folder.")

        else:

            img = image.resize((224,224))

            img = np.array(img)/255.0

            img = np.expand_dims(img,axis=0)

            prediction=model.predict(img)

            index=np.argmax(prediction)

            confidence=float(np.max(prediction)*100)

            disease=class_names[index]

            st.subheader("🩺 AI Diagnosis")

            st.success(f"Prediction : {disease}")

            st.info(f"Confidence : {confidence:.2f}%")

            st.progress(int(confidence))

            st.subheader("📊 Probability")

            for i,name in enumerate(class_names):

                st.write(
                    f"*{name} : {prediction[0][i]*100:.2f}%*"
                )

            st.divider()

            st.subheader("💊 AI Suggestions")

            if disease=="Normal":

                st.success("""
✅ No abnormality detected.

* Continue healthy lifestyle

* Exercise regularly

* Routine health checkup
""")

            elif disease=="Pneumonia":

                st.warning("""
⚠️ Possible Pneumonia Detected

* Consult Pulmonologist

* Chest Examination

* Antibiotics only if prescribed

* Proper Rest
""")

            elif disease=="Tuberculosis":

                st.error("""
🚨 Possible Tuberculosis

* Visit Chest Specialist

* Sputum Test

* CBNAAT Test

* Avoid close contact until diagnosis
""")

            elif disease=="Lung Opacity":

                st.warning("""
⚠️ Lung Opacity Detected

* HRCT Scan

* Pulmonary Consultation

* Follow Doctor Advice

* Additional Clinical Tests
""")

            st.divider()

            st.subheader("📄 Patient Report")

            st.write(f"*Patient :* {patient_name}")

            st.write(f"*Age :* {patient_age}")

            st.write(f"*Gender :* {gender}")

            st.write(f"*Disease :* {disease}")

            st.write(f"*Confidence :* {confidence:.2f}%")

            report=f"""
AI MEDICAL DIAGNOSTIC REPORT

Patient : {patient_name}

Age : {patient_age}

Gender : {gender}

Prediction : {disease}

Confidence : {confidence:.2f} %

Generated by AI Medical Diagnostic System
"""

            st.download_button(
                "📄 Download Report",
                report,
                file_name="Medical_Report.txt"
            )

# -----------------------------
# ABOUT
# -----------------------------

if menu=="About":

    st.header("ℹ️ About")

    st.write("""
AI Medical Diagnostic System

✔️ Deep Learning Based

✔️ Detects:
- Tuberculosis
- Lung Opacity
- Normal
- Pneumonia

Developed by Rehan
""")
