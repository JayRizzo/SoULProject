from os import path
from os import path      as ospath
from os import walk
from shutil import move
import click
import getpass
import numpy             as np
import os                as os
import pandas            as pd
import streamlit         as st
import sys
import time

st.session_state.mac_username = getpass.getuser()
st.session_state.current_home = ospath.expanduser('~')
st.session_state.current_dirr = ospath.expanduser(os.getcwd())

st.set_page_config(
    page_title="SoULProject: Home",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.SoULProject.us/help',
        'Report a bug': "https://www.SoULProject.us/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title ("Welcome To The SoUL Project!")
st.image("images/SoulLogo.jpg")
