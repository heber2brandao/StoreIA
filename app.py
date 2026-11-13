import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv(encoding="utf-8-sig")

st.set_page_config(page_title="StoreAI", page_icon="🛍️")
st.title("🛍️ StoreAI")
st.markdown(
    "Um atendimento virtual para ajudar você com produtos, pedidos e dúvidas da nossa loja."
)

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("Configure a variável OPENAI_API_KEY no arquivo .env.")
    st.stop()

client = OpenAI(api_key=api_key)

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "system",
            "content": (
                "Você é o StoreAI, um assistente de uma loja online. "
                "Responda com clareza e simpatia, ajudando clientes com produtos, "
                "pedidos, entregas, trocas e outras dúvidas sobre a loja."
            ),
        }
    ]

for message in st.session_state["messages"]:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("Como posso ajudar?"):
    st.session_state["messages"].append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=st.session_state["messages"],
            )

            answer = response.choices[0].message.content
            st.markdown(answer)

    st.session_state["messages"].append(
        {"role": "assistant", "content": answer}
    )
