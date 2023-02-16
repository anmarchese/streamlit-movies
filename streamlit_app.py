import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('peacock_doc_ratings.csv')
df=df.sort_values(['Ratings','Title'],ascending=[False,True])
df['Rating'] = df['Ratings'].astype(int)
df.drop('Ratings',axis=1,inplace=True)
df.reset_index(drop=True,inplace=True)
st.title('Peacock Documentary Ratings')
st.table(df)