import streamlit as st
from huggingface_hub import login
import requests
from credentials import API_TOKEN
import os

# Definiciones
model_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"
#model_id = "meta-llama/Meta-Llama-3-8B"

# Variables internas
os.environ['HUGGINGFACEHUB_API_TOKEN']=API_TOKEN
HF_TOKEN = API_TOKEN
API_URL = f"https://api-inference.huggingface.co/models/{model_id}"
headers = {"Authorization": f"Bearer {API_TOKEN}"}


def query(payload:str) -> dict:
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()


def main() -> None:
    # Page title
    st.set_page_config(page_title='🦜🔗 App Generador de Textos')
    st.title('🦜🔗 App Generador de textos')
    
    # Text input
    txt_input = st.text_area('Ingrese la temática que queire hablar', '', height=200)

    # Envio del texto mediante el boton
    if st.button ('Enviar'):
        with st.spinner('Calculando...'):
            response = query({"inputs": f' Genera un texto para una noticia: {txt_input}'})
            result = response[0]['generated_text']
            st.write(result)
    
    print('Final')
                


if __name__ == '__main__':
    # Start aplicacion
    login( token=API_TOKEN)
    main()