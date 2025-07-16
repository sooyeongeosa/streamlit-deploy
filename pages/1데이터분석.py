import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Obesity Classification.csv') 

st.set_page_config(page_title='데이터분석',page_icon='💐')
st.sidebar.header('💐비만도 데이터 분석')

st.header('데이터 분석',divider='rainbow')

st.markdown('''
- **Age**: 나이
    
- **Gender**: 성별

- **Height**: 키

- **Weight**: 몸무게

- **BMI**: 체질량지수

- **Label**: 각 개인의 비만 여부
''')


t1,t2,t3,t4=st.tabs(['상위데이터','데이터통계','컬럼데이터','조건데이터'])
with t1:
    dh=df.head(10)
    st.write(dh)
with t2:
    dd=df.describe()
    st.write(dd)
with t3:
    col=df.columns.tolist()
    col=col[0: ]
    se_col=st.multiselect('select col',col)
    new_df = df.loc[:, se_col]
    st.write(new_df)
with t4:
    c=st.selectbox('💕**select Label**💕',('Normal Weight','Overweight','Underweight'))
    cl=df['Label']==c
    c_df=df.loc[cl]
    st.write(c_df)