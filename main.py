import pandas as pd
import streamlit as st


#Todo:
#1. 새로운 데이터를 추가할 수 있는 기능 추가 (ex: github에 논의할 단어의 issue를 남기는 링크 버튼)
#2. 검색된 데이터 "번역문" 긴 한글 단어 잘리는것 해결 필요
#3. 사이트 배열 및 커스터마이징

# Set options
st.set_option('max_colwidth', 800)

# Title
st.title('양자컴퓨터 문서번역 용어집')

st.header('용어 검색')
# Read data
df = pd.read_csv('glossary.csv')

# Search Function
#search input

search = st.text_input('검색어를 입력하세요')

# language option
option = st.radio('언어', ('영어', '한글'), horizontal=True)

# output search result
if df['영어'].str.contains(search, case=False).any() and search != '' and option == '영어':
    st._legacy_dataframe(df[df['영어'].str.contains(search, case=False)])
elif df['번역문'].str.contains(search, case=False).any() and search != '' and option == '한글':
    st._legacy_dataframe(df[df['번역문'].str.contains(search, case=False)])
elif search == '':
    st.write('')
else:
    st.write('검색어가 없습니다.')



# Sort data
sort_df=df.sort_values(by='영어', key=lambda col: col.str.lower()) # Alphbetical order

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
with st.expander("전체 용어집"):
    st.table(sort_df)
    
with st.expander("참고"):
    st.markdown('- [Qiskit document 한글 번역](https://qiskit.org/documentation/locale/ko_KR/index.html)')
    st.markdown('- [물리학 용어집](https://www.kps.or.kr/content/voca/search.php)')
    st.markdown('- [TTA정보통신용어사전](http://word.tta.or.kr/main.do)')
    st.markdown('- [구글 머신러닝 용어집](https://developers.google.com/machine-learning/crash-course/glossary?hl=ko)')
    st.markdown('- [국립국어원](https://www.korean.go.kr/front/main.do)')
    st.markdown('- [대한수학회](http://www.kms.or.kr/mathdict/list.html?key=kname)')
    st.markdown('- [네이버 라틴어사전](https://dict.naver.com/lakodict/#/main)')
    st.markdown('- [MS Q# 공식문서](https://docs.microsoft.com/ko-kr/learn/paths/quantum-computing-fundamentals/)')
    st.markdown('- [양자위키](https://wiki.quist.or.kr/index.php/%EB%8C%80%EB%AC%B8)')
    st.markdown('- [양자컴퓨팅 기술백서(온라인 위키 버전)](https://wiki.quist.or.kr/index.php/%EC%96%91%EC%9E%90%EC%97%B0%EA%B5%AC%ED%9A%8C_%EC%9C%84%ED%82%A4:%EC%B1%85/%EC%96%91%EC%9E%90_%EA%B8%B0%EC%88%A0%EB%B0%B1%EC%84%9C)')

