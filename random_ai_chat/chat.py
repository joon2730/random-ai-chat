from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

from langchain.memory import ConversationBufferMemory
# from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationChain

from random_ai_chat.prompt import generate_prompt
from random_ai_chat.persona import Persona
from random_ai_chat.config import Config
from random_ai_chat.utils.notifier import notify

import streamlit as st
from threading import Thread
import time

class ChatAgent(Thread):
    def __init__(self):
        super().__init__()
        self.config = Config()

        self.llm = ChatOllama(
            model=self.config.ollama_model_name,
            temperature=self.config.model_temperature,
            # max_tokens=self.config.model_max_tokens,
            streaming=True,
        )
        self.memory = ConversationBufferMemory(
            human_prefix="user",
            ai_prefix="me"
        )
        self.persona = Persona() # generate a random persona
        self.prompt = generate_prompt(self.persona) # generate a prompt template

        # define conversation chain
        self.conversation = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            prompt=self.prompt,
            verbose=True
        )

        # buffer for user messages
        self.user_message_buffer = list()

    def push_user_message(self, user_message):
        self.user_message_buffer.append(user_message)

    def run(self):
        while True:
            if self.user_message_buffer:
                with st.chat_message("assistant"): 
                    response = self._generate_response()
                    st.write(response)
                    notify()
            else:
                time.sleep(0.3)

    def _generate_response(self):
        input_message = "\n".join(self.user_message_buffer)
        self.user_message_buffer.clear()
        response = self.conversation.invoke(input_message)["response"]
        st.session_state.messages.append({"role": "assistant", "content": response})
        print("Response:", response)
        return response