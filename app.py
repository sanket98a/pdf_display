import streamlit as st
from PyPDF2 import PdfReader
from pathlib import Path
import base64

def displayPDF(file):
        """
        Displays a PDF file in the browser.

        Parameters:
            file (str): The path to the PDF file.

        Returns:
            None

        """
        # Opening file from file path
        with open(file, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')

        # Embedding PDF in HTML
        #pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" ALIGN=CENTER width="700" height="1000" type="application/pdf"></iframe>'
        pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" ALIGN=CENTER width="900" height="300" type="application/pdf">'
        #pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" ALIGN=CENTER width="1000" height="300" type="application/pdf"></embed>'
        # Displaying File
        st.markdown(pdf_display, unsafe_allow_html=True)

def pdf_saver(pdf,save_folder_path):
        """
        Saves a PDF file to the specified folder.

        Parameters:
            pdf (bytes): The PDF file content as bytes.
            save_folder_path (str): The path to the folder where the PDF will be saved.

        Returns:
            save_path (Path): The path to the saved PDF file.

        """
        save_path = Path(save_folder_path, pdf.name)
        with open(save_path, mode='wb') as w:
            w.write(pdf.getvalue())
        if save_path.exists():
            st.success(f'File {pdf.name} is successfully saved!')
            return save_path
        

## slide bar 
with st.sidebar:
    # st.set_page_config(page_title="Ask your PDF")
    st.write("**Ask your Invoice**💬")
    # upload file
    pdf = st.file_uploader("**Upload your Invoice**", type="pdf")
    if pdf :
        # Document saved into storage
        save_path=pdf_saver(pdf,save_folder_path=  './saved_invoices')

if pdf is not None:
    displayPDF(save_path)