import streamlit as st

st.set_page_config(layout = "wide")
st.selectbox("Your document is what type of document?", ["journal article", "pamphlet", "short book", "book", "short story", "other"])
st.file_uploader("Upload the document you want summarized", type = ['pdf'], accept_multiple_files = False)
