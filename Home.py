from os import path
from os import path      as ospath
from os import walk
from PIL import Image
from shutil import move
import click
import getpass
import numpy             as np
import os                as os
import pandas            as pd
import streamlit         as st
import sys
import time

im = Image.open("images/SoulLogo.jpg")
st.set_page_config(
                   page_title="SoULProject: Home",
                   page_icon=im,
                   layout="wide",
                   initial_sidebar_state="expanded"
                  )

st.sidebar.image("images/Ethos_Pathos_Logos.png")
st.session_state.mac_username = getpass.getuser()
st.session_state.current_home = ospath.expanduser('~')
st.session_state.current_dirr = ospath.expanduser(os.getcwd())


st.title("Welcome To The SoUL Project!")

colA1, colB1 = st.columns(2)
colA1.title("Leadership")
colA1.image("images/leadership.png", width=700)
colB1.title("Brains In Congress")
colB1.image("images/2brainsincongress-1.png", width=700)

st.subheader("SoUL Mission Statement")
st.markdown("""

Creating the 2nd Enlightenment which will heal our National Conversation and Team Problem Solving capabilities in all areas of life. We do this by:

- Using all information, logic, philosophy, ideas and principles from the 1st Enlightenment and add what is missing and change any flaws.

- Fairness is defined as just and reasonable treatment in accordance with accepted rules and/or principles.

- Showing our Nation, we need and can have healthy structures of Hierarchy and Meritocracy in all areas of life with Leadership that has PIECES; Prudence, Integrity, Empathy, Courage, Excellence, Sensibility.

- Explaining very well how we as individuals, small and large communities conserve and progress code; views, idioms, principles, logic, rules, etc.

- We are creating a living document, so there is one source that contains all critical thinking methods(virtues), human pitfalls(weaknesses).  Those controlling this document will fully engage in all criticism from whoever has any and show our work for how said criticism was engaged in.

""")
