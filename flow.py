import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
from prompts import questions, prompts
from utils import extract_save_value
from ChatModel import LlmAgent
import json
import re

#Load the environment variable
load_dotenv()

#initialize the Agent
question_agent = LlmAgent()

#Creating a client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

#Main flow of the chat app
def Flow():
    #Chat stages
    if st.session_state.chat_stage < len(questions):
        key, question = questions[st.session_state.chat_stage]
        user_input = st.chat_input("Your response")
        if user_input:
            completion = client.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                messages=[
                    {"role": "assistant", "content": prompts[st.session_state.chat_stage][1]},
                    {"role": "assistant", "content": f"{question}"},
                    {"role": "user", "content": f"{user_input}"}
                ],
                temperature=0.5,
                max_completion_tokens=1024,
                top_p=1,
                stream=True,
            )
            response = ""
            for chunk in completion:
                response += chunk.choices[0].delta.content or ""


            #Saves the User information(ex. Name,desired position)
            if 'save:' in response:
                st.session_state[key] = extract_save_value(response)
                st.session_state.chat_stage += 1
                if st.session_state.chat_stage < len(questions):
                    st.session_state.chat_session.extend([
                        {"role": "user", "content": user_input},
                        {"role": "assistant", "content": questions[st.session_state.chat_stage][1]}
                    ])
                elif st.session_state.chat_stage == len(questions):
                    if not st.session_state.tech:
                        st.session_state.tech= user_input
                    st.session_state.chat_session.extend([
                        {"role": "user", "content": user_input},
                    ])

            else:
                st.session_state.chat_session.extend([
                    {"role": "user", "content": user_input},
                    {"role": "assistant", "content": response},
                ])
            st.rerun()

    else:
        # Skill based Question generation segment
        if not st.session_state.questions:
            try:

                generated_questions = question_agent.question_generation(st.session_state.tech)
                st.session_state.questions = json.loads(generated_questions)

                question_keys = list(st.session_state.questions.keys())
                question_index = st.session_state.get("question_index", 0)
                key = question_keys[question_index]
                question = st.session_state.questions[key]
                st.session_state.chat_session.extend([
                    {"role": "assistant", "content": "I like you answer the below Question"},
                    {"role": "assistant", "content": question},
                ])
                st.session_state.question_index = 1
                st.rerun()
            except (json.JSONDecodeError, KeyError):

                st.error("Failed to generate additional questions. Please check the model output.")

                return

        #Ask the skill based question and save the answer
        if st.session_state.question_index <=len(st.session_state.questions.keys()):
            user_input = st.chat_input("Your response")
            if user_input:
                if (st.session_state.question_index == len(st.session_state.questions.keys())):
                    st.session_state.chat_session.extend([

                        {"role": "user", "content": user_input},
                    ])
                    st.session_state.question_index = st.session_state.question_index +1
                    st.rerun()
                key = list(st.session_state.questions.keys())[st.session_state.question_index]
                question = st.session_state.questions[key]
                st.session_state.user_response[question] = user_input

                st.session_state.chat_session.extend([

                    {"role": "user", "content": user_input},
                    {"role": "assistant", "content": question},

                ])

                question_index = st.session_state.get("question_index", 0)
                st.session_state.question_index = question_index + 1
                st.rerun()
        #End of the Chat
        else:
            st.chat_input("ThanK you for Giving Your information", key="disabled_chat_input", disabled=True)


