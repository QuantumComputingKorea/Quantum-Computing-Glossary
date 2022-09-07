import pandas as pd
import streamlit as st
import csv

# Title
st.title('양자컴퓨터 문서번역 용어집')

# Read data
df = pd.read_csv('glossary.csv')
sort_df=df.sort_values('영어') # 영어순으로 정렬

#인덱스 숨기기
# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

# Display a static table
st.table(sort_df)
