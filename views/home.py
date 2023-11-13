import streamlit as st
from pathlib import Path
from PIL import Image

def load_view():
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    resume_file =  current_dir / "assets" /"CV.pdf"
    profile_pic =  current_dir / "assets" /"photo.jpg"

    NAME = "Charishma Ambati"
    DESCRIPTION = """
    Results-driven Software Engineer 3+ years hands-on experience with a strong technical foundation in data science, computer science, machine learning, and artificial intelligence with expertise in Python and Java. Seeking opportunity as Machine Learning Engineer with a company I can grow with.

    """
    EMAIL = "charishma.a610@gmail.com"
    SOCIAL_MEDIA = {
        "LinkedIn": "https://www.linkedin.com/in/charishma-ambati-ba377513b/",
        "GitHub": "https://github.com/CharishmaAmbati",
    }

    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)


    # --- HERO SECTION ---
    # col1, col2 = st.columns(2, gap="small")
    # with col1:
    #     st.image(profile_pic, width=230)

    # with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


    # --- SOCIAL LINKS ---
    st.write('\n')
    cols = st.columns(5)
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")


    
