import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Qdrant
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from data import get_data
import os
load_dotenv()

def get_vectorstore():
    # get the text in document form
    document = get_data()
    
    # split the document into chunks
    text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n","\n"])
    document_chunks = text_splitter.split_documents(document)
    
    # create a vectorstore from the chunks
    # vector_store = Chroma.from_documents(document_chunks, OpenAIEmbeddings())

    url = os.getenv("url")
    api_key = os.getenv("api_key")
    embeddings = OpenAIEmbeddings()
    vector_store = Qdrant.from_documents(
        document_chunks,
        embeddings,
        url=url,
        prefer_grpc=True,
        api_key=api_key,
        collection_name="CampusBot",
        force_recreate=True,
    )
    return vector_store

def get_context_retriever_chain(vector_store):
    llm = ChatOpenAI()
    
    retriever = vector_store.as_retriever(search_type="mmr")
    
    prompt = ChatPromptTemplate.from_messages([
      MessagesPlaceholder(variable_name="chat_history"),
      ("user", "{input}"),
      ("user", "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation")
    ])
    
    retriever_chain = create_history_aware_retriever(llm, retriever, prompt)
    
    return retriever_chain
    
def get_conversational_rag_chain(retriever_chain): 
    
    llm = ChatOpenAI()
    
    prompt = ChatPromptTemplate.from_messages([
      ("system", "You are a helpful question-answering chatbot for Seshadri Rao Gudlavalleru Engineering College website and IoT Branch. You will be answering the queries regarding the college and IoT branch. Answer the user's questions based only on the below context:\n\n{context}"),
      MessagesPlaceholder(variable_name="chat_history"),
      ("user", "{input}"),
    ])
    
    stuff_documents_chain = create_stuff_documents_chain(llm,prompt)
    
    return create_retrieval_chain(retriever_chain, stuff_documents_chain)

def get_response(user_input):
    retriever_chain = get_context_retriever_chain(st.session_state.vector_store)
    conversation_rag_chain = get_conversational_rag_chain(retriever_chain)
    
    response = conversation_rag_chain.invoke({
        "chat_history": st.session_state.chat_history,
        "input": user_query
    })
    
    return response['answer']

# app config
st.set_page_config(page_title="CampusBot", page_icon="🤖")
st.title("CampusBot")

# session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Welcome SRGEC CampusBot by students of IoT Department. How can I help you?"),
    ]
if "vector_store" not in st.session_state:
    st.session_state.vector_store = get_vectorstore()    

# user input
user_query = st.chat_input("Enter your question")
if user_query is not None and user_query != "":
    response = get_response(user_query)
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    st.session_state.chat_history.append(AIMessage(content=response))
        
       

# conversation
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)