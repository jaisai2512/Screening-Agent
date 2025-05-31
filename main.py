import streamlit as st
from session_manager import initialize_session_state
from flow import Flow

# Page Configuration
st.set_page_config(
    page_title="Talent Scout Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Full-Page Black Background and Title Animation
st.markdown("""
    <style>
    html, body, #root, .stApp {
    background-color: #000000 !important;
    color: #FFFFFF !important;

}

    /* Animation Keyframes */
    @keyframes slideFadeIn {
        0% {
            opacity: 0;
            transform: translateX(-50px);
        }
        100% {
            opacity: 1;
            transform: translateX(0);
        }
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    /* Chat title with animation */
    .chat-title {
        text-align: center;
        font-size: 2em;
        color: #f2f2f2;
        margin-top: 20px;
        margin-bottom: 30px;
        font-weight: bold;
        animation: slideFadeIn 1.2s ease-out;
    }

    /* Chat bubbles with fade-in animation */
    .chat-message {
        padding: 12px 18px;
        margin-bottom: 12px;
        border-radius: 15px;
        max-width: 80%;
        word-wrap: break-word;
        animation: fadeIn 1.5s ease forwards;    }

    .assistant {
        background-color: crimson;
        color: #fff;
        align-self: flex-start;
    }

    .user {
        background-color: #14A0DC;
        color: #fff;
        align-self: flex-end;
        margin-left: auto;
    }

    /* Chat container */
    .chat-container {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
    

.chat-title {
    text-align: center;
    font-size: 2em;
    color: white;
    font-weight: bold;
    margin: 0;
    animation: slideFadeIn 1.2s ease-out;
}
    </style>
""", unsafe_allow_html=True)

#Initialize Session
initialize_session_state()

# Chat UI Wrapper
st.markdown('<div class="chat-wrapper">', unsafe_allow_html=True)

#Animated Chat Title
st.markdown('<div class="chat-title">Screening Agent</div>', unsafe_allow_html=True)

#Render chat messages
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for message in st.session_state.chat_session:
    role = "assistant" if message["role"] == "assistant" else "user"
    bubble_class = f"chat-message {role}"
    st.markdown(f'<div class="{bubble_class}">{message["content"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)  # Close chat-container

#Run Chatbot Logic
if __name__ == '__main__':
    Flow()

st.markdown('</div>', unsafe_allow_html=True)  # Close chat-wrapper
