
import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os

# Haal API-key op uit Streamlit secrets
openai_api_key = st.secrets.get("OPENAI_API_KEY")
if not openai_api_key:
    st.error("⚠️ Voeg je OPENAI_API_KEY toe via Streamlit secrets")
    st.stop()
os.environ["OPENAI_API_KEY"] = openai_api_key

st.set_page_config(page_title="HRbuddy", layout="centered")
st.title("🤖 HRbuddy – jouw HR-assistent")
st.markdown("Stel hier je HR-vraag, HRbuddy luistert mee.")

# Gespreksgeschiedenis onthouden
memory = ConversationBufferMemory()

# Setup LLM
llm = ChatOpenAI(temperature=0.3, model_name="gpt-3.5-turbo")
conversation = ConversationChain(llm=llm, memory=memory)

user_input = st.text_input("💬 Typ je vraag hier:")

if user_input:
    with st.spinner("Even nadenken…"):
        response = conversation.predict(input=user_input)
    st.success(response)
