import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession

project="gemini-explorer"

vertexai.init(project=project)

config=generative_models.GenerationConfig(
    temperature=0.4
)

# Creating the model w/ config
model = GenerativeModel(
    "gemini-pro",
    generation_config=config
)

# Creating the chat session 
chat = model.start_chat()


#Now working with the Streamlit app
# Helper function to display & store chat messages
def llm_helper(chat: ChatSession, query):
    response = chat.send_message(query) #sending query to chat model
    output = response.candidates[0].content.parts[0].text #getting the response from the model
    
    # Displaying the response
    with st.chat_message("model"):
        st.markdown(output)
        
    st.session_state.messages.append({
        "role":"user",
        "content": query
    })
    
    st.session_state.messages.append({
        "role": "model",
        "content": output
    })
    
# Setting the title of the Streamlit app
st.title("Gemini Explorer")

# Initializing chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# Displaying & loading chat history if there are messages
for index, message in enumerate(st.session_state.messages):
    content = Content(
        role = message["role"],
        parts = [Part(text=message["content"])] #Creates a list with a single Part object containing the message text
    )
    
    # Displaying the message
    if index != 0:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    chat.history.append(content)
    
# Capturing user input
query = st.chat_input("Gemini Explorer") #chat_input displayes a chat input widget

if query:
    with st.chat_message("user"):
        st.markdown(query)
    llm_helper(chat, query)
    
if len(st.session_state.messages) == 0:
    initial_prompt = "Introduce yourself as ReX, an assistant powered by Google Gemini. You use emojis to be interactive"
    llm_helper(chat, initial_prompt)
