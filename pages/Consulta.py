import streamlit as st
import pandas as pd

dados = pd.read_csv("clientes.csv", sep=",")

st.title("Clientes cadastrados")

st.dataframe(dados)