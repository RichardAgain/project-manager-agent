import streamlit as st
import shelve

from src.deepseek import call_deepseek_api

st.title("Tali Chatbot")

USER_AVATAR = "👤"
BOT_AVATAR = "🔥"

# Load chat history from shelve file
def load_chat_history():
    with shelve.open("chat_history") as db:
        return db.get("messages", [])


# Save chat history to shelve file
def save_chat_history(messages):
    with shelve.open("chat_history") as db:
        db["messages"] = messages


# Initialize or load chat history
if "messages" not in st.session_state:
    st.session_state.messages = load_chat_history()

# Sidebar with a button to delete chat history
with st.sidebar:
    if st.button("Borrar historial"):
        st.session_state.messages = []
        save_chat_history([])

# Display chat messages
for message in st.session_state.messages:
    avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Main chat interface
if prompt := st.chat_input("Escribe algo..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(prompt)

    # Generate bot response using bigram model
    bot_response = call_deepseek_api(prompt)
    with st.chat_message("assistant", avatar=BOT_AVATAR):
        st.markdown(bot_response)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    

    # with st.chat_message("assistant", avatar=BOT_AVATAR):
    #     message_placeholder = st.empty()
    #     full_response = ""
    #     for response in client.chat.completions.create(
    #         model=st.session_state["openai_model"],
    #         messages=st.session_state["messages"],
    #         stream=True,
    #     ):
    #         full_response += response.choices[0].delta.content or ""
    #         message_placeholder.markdown(full_response + "|")
    #     message_placeholder.markdown(full_response)
    # st.session_state.messages.append({"role": "assistant", "content": full_response})

# Save chat history after each interaction
save_chat_history(st.session_state.messages)
