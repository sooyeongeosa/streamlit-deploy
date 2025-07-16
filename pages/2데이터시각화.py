import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title='데이터시각화',page_icon='💐')
df = pd.read_csv('Obesity Classification.csv') 
st.sidebar.header('💐데이터 시각화')
st.header('데이터 시각화', divider='rainbow')


t1,t2,t3=st.tabs(['히스토그램','박스그래프','막대그래프'])
with t1:
    st.markdown('''
            **BMI 분포 히스토그램**
        ''')
    fig = plt.figure(figsize=(10, 5))
    sns.histplot(data=df, x='BMI', hue='Label')
    st.pyplot(fig)

with t2:
    st.markdown('''
                **성별에 따른 BMI 박스그래프**
            ''')
    fig = plt.figure(figsize=(10, 6))
    sns.boxplot(x='Gender', y='BMI', hue='Label', data=df)
    st.pyplot(fig)

with t3:
    st.markdown(''' 
                **나이에 따른 Label 막대그래프**
            ''')
    fig = plt.figure(figsize=(10,5))
    sns.barplot(data=df, x='Age', y='Label')
    st.pyplot(fig)



