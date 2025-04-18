"""
Module for stp.table()
"""

import streamlit as st
from typing import Literal

def table(
    data
):
    st.dataframe(data)