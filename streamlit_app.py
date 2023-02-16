import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('movie_ratings.csv')
df = df.sort_values(['Ratings','Title'],ascending=[False,True])
df['Rating'] = df['Ratings'].astype(int)
df.drop('Ratings',axis=1,inplace=True)
df.reset_index(drop=True,inplace=True)
types = df.Type.unique().tolist()
add_selectbox = st.multiselect(
    'Movie Type?',
    types,types)
st.title('Peacock Ratings')
if add_selectbox is None:
    st.table(df)
else:
    st.table(df[df['Type'].isin(add_selectbox)])
