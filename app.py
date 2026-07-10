import streamlit as st

st.set_page_config(
    page_title="AI Medical Diagnostic System",
    page_icon="🩺",
    layout="wide"
)

# Sidebar
st.sidebar.title("🩺 AI Medical Panel")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Upload X-Ray",
        "AI Analysis",
        "Reports",
        "About"
    ]
)

# Custom CSS
st.markdown("""
<style>

.stApp{
background: linear-gradient(
135deg,
#f4fbff,
#e6f3ff,
#d7eeff
);
}

.card{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 4px 15px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# Header
st.title("🏥 AI Medical Diagnostic System")
st.markdown("""
<div class='card'>
<h3>AI Powered Chest X-Ray Analysis</h3>
<p>Professional Medical Diagnostic Dashboard</p>
</div>
""", unsafe_allow_html=True)

