import streamlit as st
import pandas as pd
import numpy as np

data = 'C:\\Users\\anddr\\Downloads\\planilha_formatada.xlsx'
planilha = pd.read_excel(data) 
st.title("Tabela de notas")
df = pd.DataFrame(planilha)
st.dataframe(data=planilha, height=2000, use_container_width=True )

