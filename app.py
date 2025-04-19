import streamlit as st
import time
import asyncio
from streamlit.runtime.scriptrunner import add_script_run_ctx, get_script_run_ctx

from random_ai_chat.chat import ChatAgent

# App title
st.set_page_config(page_title="RandAIChat", page_icon="☕", layout="wide")

# Initialize session state
if "messages" not in st.session_state.keys():
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Initialize chat_agent
if "chat_agent" not in st.session_state.keys():
    with st.spinner("Match making..."):
        st.session_state.chat_agent = ChatAgent()
        add_script_run_ctx(st.session_state.chat_agent, get_script_run_ctx())
        st.session_state.chat_agent.start()

# Get user input
if prompt := st.chat_input("Send a message"):
    st.session_state.messages.append({"role": "user", "content": prompt}) # Save user message
    with st.chat_message("user"):
        st.markdown(prompt)     # Display user message
    st.session_state.chat_agent.push_user_message(prompt) # Push user message to model



