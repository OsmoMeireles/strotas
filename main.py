import pandas as ps
import streamlit as st

st.set_page_config(page_title="Dados Meli",
                   page_icon=":bar_chart:", layout="wide")

st.sidebar.title("Dashboard")

st.sidebar.image("meli.png", width=100)
st.sidebar.title("Filtros")
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
