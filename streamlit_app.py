import streamlit as st

st.set_page_config(
    page_title="ASD Prediction System",
    page_icon="B",
    layout="wide"
)

st.title("ASD Prediction System")
st.write(
    "Welcome to the ASD Prediction System. Please use the sidebar to navigate through the application."
)

st.sidebar.success("Select a page above.")

if st.button("Run AI Analysis"):
    st.info("AI Analysis started...")
    # Add your logic here
