# Screening Agent 
## Project Overview
Screening Agent is a conversational AI-based hiring assistant designed to streamline the recruitment process. Built using Streamlit and Meta’s Generative AI, the chatbot guides users through a step-by-step interview process, collecting information about their skills, experience, and preferences. It dynamically generates additional questions and evaluates candidates based on their responses, providing insights for recruiters.

Installation Instructions
Clone the Repository

```bash
git clone https://github.com/your-repo/Screening-Agent.git
cd talent-scout
```
Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
Install Required Dependencies

```bash
pip install -r requirements.txt
```
Add API Keys

- Create a .env file in the project root directory.
- Add your Groq API Key:
- Groq_API_KEY=your_Groq_api_key_here
* Run the Application

```bash
streamlit run test.py
```
Access the App

- Open your browser and navigate to http://localhost:8501.


## Usage Guide
Launching the App
After running the app, you'll be greeted with a welcome message and guided through a series of questions.

# Step-by-Step Information Gathering

Enter details like your 
- full name
- email
- years of experience
- technical skills.

Respond to dynamically generated questions crafted by the AI model.

## Technical Details
### Libraries Used

#### Streamlit
- Frontend framework for interactive web apps.
#### Groq 
- API for generating questions and evaluations.
#### dotenv 
- Manages environment variables securely.
### Model Details

Utilizes Groq(meta-llama/llama-4-scout-17b-16e-instruct) for generating content and evaluating candidates.

Modular design with an Agents class to encapsulate API interactions.
Session management using st.session_state for seamless user experience.
### Prompt Design
#### Information Gathering
Prompts are designed to elicit precise and structured responses. For example:

- Prompt for name: "What is your full name?"
- Prompt for skills: "What is your tech stack (e.g., Python, Django, SQL)?"
#### Dynamic Question Generation

##### Prompt Design for Question Generation
Our approach to crafting questions is systematic and hierarchical, ensuring a smooth progression in difficulty while analyzing the candidate's expertise. Here's the step-by-step methodology

##### 1. Necessity Question
The first question focuses on the core, essential knowledge of the candidate's stated tech stack. This ensures we establish a baseline understanding of their fundamental knowledge.
Example: "Can you explain the difference between Python lists and tuples?"

##### 2. Progressively Tougher Questions
The next four questions increase in complexity, gradually testing the candidate's problem-solving skills, application of knowledge, and deep understanding of concepts.

- Question 2 (Slightly Tougher): Introduce situational or real-world use cases to test applied knowledge.
  - Example: "How would you optimize a Python program that processes a list of 10 million items?"

- Question 3 (Intermediate): Explore technical depth by requiring a more detailed response.
  - Example: "Explain how Python's GIL (Global Interpreter Lock) impacts multi-threading, and how can it be mitigated?"

- Question 4 (Advanced): Test theoretical understanding and ability to deal with edge cases.
  - Example: "What challenges would you face when integrating Python libraries like NumPy with C++ code, and how would you address them?"

- Question 5 (Expert-Level): Evaluate creativity and mastery by posing an open-ended question that requires a solution-oriented mindset.
  - Example: "Design an API in Python that supports asynchronous requests for real-time data fetching and briefly outline the architecture."

### Challenges & Solutions
#### Session State Management

##### Challenge 
- Ensuring the chatbot flow remained consistent during user interactions.
##### Solution 
- Used st.session_state to persist chat history, user data, and flow stages.
#### Dynamic Question Parsing:

##### Challenge 
- Handling JSON parsing issues with AI-generated questions.
##### Solution 
- Implemented error handling to validate and parse JSON safely.
#### Prompt Engineering

##### Challenge 
- Crafting effective prompts for diverse user inputs.
##### Solution 
- Iterated on prompts to balance specificity and adaptability for varied responses.
