import streamlit         as st
from os import path
from PIL import Image

im = Image.open("images/SoulLogo.jpg")
st.set_page_config(
                   page_title="SoULProject: Images",
                   page_icon=im,
                   layout="wide",
                   initial_sidebar_state="expanded"
                  )

Tab1, Tab2   = st.tabs(["Tab 1", "Tab 2"])

colA1, colB1 = Tab1.columns(2)
colA2, colB2 = Tab2.columns(2)

colA1.write("2brainsincongress")
colA1.title("2brainsincongress")
colA1.image("images/2brainsincongress-1.png")

colB1.write("4quadrantsofjudgement")
colB1.title("4quadrantsofjudgement")
colB1.image("images/4quadrantsofjudgement.png")


colA2.write("colA2")
colB2.write("colB2")

