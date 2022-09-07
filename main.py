import pandas as pd
import streamlit as st

"""
Todo:
1. 새로운 데이터를 추가할 수 있는 기능 (ex: github에 논의할 단어의 issue를 남기는 링크 버튼)
2. 
3. 사이트 꾸미기
"""

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


# Title
st.title('양자컴퓨터 문서번역 용어집')

st.header('용어 검색')
# Read data
df = pd.read_csv('glossary.csv')

# Search Function
# language option
### option = st.selectbox('검색할 대상을 선택하세요', ('영어', '한글'))
container = st.empty()
button_A = container.button('영어')
option = '영어'

if button_A and option == '영어':
    container.empty()
    option = '한글'
    button_A = container.button('한글')
elif button_A and option == '한글':
    container.empty()
    option = '영어'
    button_A = container.button('영어')

#search input
search = st.text_input('검색어를 입력하세요')
container2 = st.empty()
if df['영어'].str.contains(search, case=False).any() and search != '' and option == '영어':
    container2.empty() # reset dataframe size
    container2.dataframe(df[df['영어'].str.contains(search, case=False)])
elif df['번역문'].str.contains(search, case=False).any() and search != '' and option == '한글':
    container2.empty() # reset dataframe size
    container2.dataframe(df[df['번역문'].str.contains(search, case=False)])

elif search == '':
    container2.write('')
else:
    container2.write('검색어가 없습니다.')

# Sort data
sort_df=df.sort_values('영어') # Alphbetical order

# Display a static table
with st.expander("전체 용어집"):
    st.table(sort_df)
