import pandas as pd
import streamlit as st
import csv

# Title
st.title('양자컴퓨터 문서번역 용어집')

# Read data
df = pd.read_csv('glossary.csv')
sort_df=df.sort_values('영어') # 영어순으로 정렬
sort_df=sort_df.style.hide_index() # 인덱스 숨기기
st.table(sort_df)