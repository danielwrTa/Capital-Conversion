
import streamlit as st
import requests

st.set_page_config(page_title="Meu simulador financeiro",
                   page_icon="💰")

st.title("Meu simulador financeiro")

@st.cache_data(ttl=60)
def buscar_dolar():
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"

    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()

    dados = resposta.json()
    return dados["BRLUSD"]

try:
    dolar = buscar_dolar()

    cotacao = float(dolar["bid"])
    variacao = float(dolar["pctChange"])

    st.metric(
        label="Dólar comercial (USD/BRL)",
        value=f"R$ {cotacao:.4f}",
        delta=f"{variacao:.2f}%"
    )

    st.caption(
        f"Última atualização: {dolar['create_date']}"
    )

except (requests.RequestException, KeyError, ValueError) as erro:
    st.error("Não foi possível consultar a cotação agora.")
