import streamlit as st

def init(key: str, value):
    """Initialize a key in session state if it doesn't exist."""
    if key not in st.session_state:
        st.session_state[key] = value

def set(key: str, value):
    """Set or update a key in session state."""
    st.session_state[key] = value

def get(key: str, default=None):
    """Get a key from session state, return default if not found."""
    return st.session_state.get(key, default)

def delete(key: str):
    """Delete a key from session state if it exists."""
    if key in st.session_state:
        del st.session_state[key]