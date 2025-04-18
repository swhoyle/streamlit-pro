"""
Module for stp.text()
"""

import streamlit as st
from typing import Literal

def text(
  text: str,
  size: int = None,
  font: str = None,
  color: str = None,
  bold: bool = None,
  italic: bool = None,
  underline: bool = None,
  alignment: Literal["left", "right", "middle"] = None
) -> None:
    """
    Render styled text to a streamlit app.

    Parameters
    ----------
    text: str
        The text that will be displayed
    size: int
        The font size of the text
    font: str or None
        The font family of the text
    color: str
        The font color of the text
    bold: bool
        Whether or not the text is bold
    italic: bool
        Whether or not the text is italicized
    underline: bool
        Whether or not the text is underlined
    alignment: Literal["left", "right", "middle"]
        The text alignment

    Example
    -------
    >>> import streamlit as st
    >>>
    >>> text("Title", size = 40, bold = True, alignment = "center")
    >>> text("Subtitle", size = 20, color = "#D3D3D3", alignment = "center"))
    >>> text("Body text that has lots of words", size = 12, font = "Arial", italic = True, underline = True)
    >>> text("More helper Text", color = "blue")
    """
    styles = []

    if size:
        styles.append(f"font-size: {size}px;")
    if font:
        styles.append(f"font-family: {font};")
    if color:
        styles.append(f"color: {color};")
    if bold:
        styles.append("font-weight: bold;")
    if italic:
        styles.append("font-style: italic;")
    if underline:
        styles.append("text-decoration: underline;")
    if alignment:
        styles.append(f"text-align: {alignment};")

    style_string = " ".join(styles)
    html = f'<p style="{style_string}">{text}</p>'

    st.markdown(html, unsafe_allow_html=True)