import pandas as ps
import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="Dados Meli",
                   page_icon=":bar_chart:", layout="wide")

st.sidebar.title("Dashboard")

st.sidebar.image("meli.png", width=90)
# Título da Sidebar
st.sidebar.header("Filtros")
transportadora = st.sidebar.selectbox("Selecione a transportadora:", [
    "ADO",
    "ALC",
    "BASEPEX",
    "BLD",
    "CAXIENSE",
    "COOPMETRO",
    "DECARGO",
    "DHL",
    "HAWK",
    "HELP",
    "IMEDIATO",
    "KANGU",
    "NEPOMUCENO",
    "P. SPOT",
    "RODACOOP"
])

# Configuração da página (opcional)
st.set_page_config(page_title="Filtro de Calendário", layout="wide")

# --- CONFIGURAÇÃO DO CALENDÁRIO NA SIDEBAR ---

# Definindo as datas padrão (Hoje e daqui a 7 dias)
data_hoje = datetime.today()
daqui_uma_semana = data_hoje + timedelta(days=7)

# Calendário com seleção de intervalo (passando uma tupla no 'value')
intervalo_datas = st.sidebar.date_input(
    label="Selecione o período:",
    value=(data_hoje, daqui_uma_semana),
    format="DD/MM/YYYY"  # Formato de exibição brasileiro
)

# --- TRATAMENTO DOS DADOS SELECIONADOS ---

# O Streamlit retorna uma tupla. É importante verificar se o usuário já selecionou
# ambas as datas (início e fim) para evitar erros no código enquanto ele clica.
if isinstance(intervalo_datas, tuple) and len(intervalo_datas) == 2:
    data_inicio, data_fim = intervalo_datas

else:
    # Mensagem amigável caso o usuário tenha clicado apenas na data de início e ainda não na de fim
    st.sidebar.info(
        "Por favor, selecione a data de término no calendário da barra lateral.")

st.sidebar.success("Qualidade GERA Lucratividade!")
st.sidebar.success("Detalhe DEFINE Resultado!")
st.sidebar.text("Desenvolvido por: \n\n")
st.sidebar.text("Osmo Meireles\n osmo.cmeireles@mercadolivre.com")
