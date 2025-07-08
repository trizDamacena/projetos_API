import requests
import json
import streamlit as st


def buscar_usuario(ID):
    endpoint = (f'https://aprendendoapi-2b6f3-default-rtdb.firebaseio.com/{ID}/.json')
    response = requests.get(endpoint)
    dados = f'Nome: {response.json()["Nome"]}\nSobrenome: {response.json()["Sobrenome"]}\nIdade: {response.json()["Idade"]} anos' if response.status_code == 200 else ""
    return dados 

def cadastrar_usuario(cdNome, cdSobrenome, cdIdade):
    informacoes = {}
    informacoes['Nome'] = f'{cdNome}'
    informacoes['Sobrenome'] = f'{cdSobrenome}'
    informacoes['Idade'] = f'{cdIdade}'

    headers = {'Content-Type': 'application/json'}
    endpoint = ('https://aprendendoapi-2b6f3-default-rtdb.firebaseio.com/.json')

    response= requests.post(endpoint, data = json.dumps(informacoes), headers=headers)
    print(response.json())
    return response

st.title("Bem vindo!")



st.title("BUSCAR USUÁRIO")
ID = st.text_input("Digite ID do usuário: ", key="ID")
buscar = st.button("Buscar")

if buscar:
    busca = buscar_usuario(ID)
    if busca:
        st.success("Encontramos")
        st.text("INFORMAÇÔES DO USUÁRIO")
        st.text(busca)
    else:
        st.error("Não encontramos")



st.text("CADASTRAR NOVO USUÁRIO")
cdNome = st.text_input("Digite o valor: ", key= "cdNome")
cdSobrenome = st.text_input("Digite o valor do campo:", key="cdSobrenome")
cdIdade = st.text_input("Digite o valor do campo:", key="cdIdade")
cadastrar = st.button("CADASTRAR")

if cadastrar:
    cadastro = cadastrar_usuario(cdNome, cdSobrenome, cdIdade)
    if cadastro:
        st.success("Cadastramos o usuário!")
        
    else:
        st.error("Não conseguimos cadastrar o usuário")