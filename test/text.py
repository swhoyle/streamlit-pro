import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import streamlit_pro as stpro

stpro.text("Text", size = 20, color = "blue", underline = True, alignment="center")
st.write("Text")