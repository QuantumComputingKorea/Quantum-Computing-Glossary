import pandas as pd
import streamlit as st
import csv

# Title
st.title('양자컴퓨터 문서번역 용어집')

# Read data
df = pd.read_csv('glossary.csv')
sort_df=df.sort_values('영어')
st.table(sort_df)