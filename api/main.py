from langchain_groq import ChatGroq
import streamlit as st
import os
from langchain.schema import HumanMessage

# Initialize the LLM with your credentials and model
llm = ChatGroq(api_key="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", model="llama3-70b-8192")

st.title('Ask Real360')

# Initialize session state for chat messages if it doesn't already exist
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])
domain_context = """
You are a real estate AI assistant. Your knowledge covers the real estate market, property values, investment strategies, home buying and selling processes, mortgages, and other related real estate topics. Please provide informative, helpful, and clear responses based only on real estate topics. Do not provide information outside the real estate domain.
"""

# Input for new user prompt
prompt = st.chat_input('Pass Your Prompt here')

if prompt:
    # Add user message to the session and display it
    full_prompt = domain_context + " " + prompt
    st.chat_message('user').markdown(prompt)
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    # Generate response using the LLM
    response = llm.invoke([HumanMessage(content=full_prompt)], max_tokens=400, temperature=0.7)
    # Display the assistant's response and add it to the session state
    st.chat_message('assistant').markdown(response.content)
    st.session_state.messages.append({'role': 'assistant', 'content': response.content})

    
    

    

    
    