import pandas as pd
import streamlit as st

# Title
st.title('양자컴퓨터 문서번역 용어집')

# Read data
df = pd.read_csv('glossary.csv')

# Search Function
search = st.text_input('검색어를 입력하세요')
if df['영어'].str.contains(search).any():
    st.write(df[df['영어'].str.contains(search)])
else:
    st.write('검색어가 없습니다.')

# Sort data
sort_df=df.sort_values('영어') # Alphbetical order

# Hide index
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
