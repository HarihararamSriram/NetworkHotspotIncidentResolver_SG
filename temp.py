import streamlit as st
from tree_inference import predict

st.title("Potential network hotposts 🔥")

# # Accept user input
# with st.container() as container:
#     if prompt := st.chat_input("What is up?"):
#         with st.chat_message("user", avatar='😄'):
#             st.markdown(prompt)
#         with st.chat_message("assistant"):
#             st.markdown(predict(prompt.strip()))
            
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        ans = predict(prompt.strip())
        full_response = st.markdown(ans)
        st.session_state.messages.append({"role": "assistant", "content": ans})