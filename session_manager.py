import streamlit as st


#Initialize the session variables
def initialize_session_state():
    state_defaults = {
        "chat_session": [
            {"role": "assistant", "content": "Hi Human, Myself a Chatbot who is here to collect Your information for initial Screening"},
            {'role': "assistant", 'content': 'What is your full name?'}
        ],
        "chat_stage": 0,
        "questions": [],
        "Name": '',
        "Email": '',
        "Phone Number": '',
        "Years of Experience": "",
        "Desired Position": "",
        "Current Location": "",
        "Tech Stack": "",
        "tech":"",
        "user_response":{},
        "previous":0,
    }
    for key, value in state_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
