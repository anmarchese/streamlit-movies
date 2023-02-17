import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('movie_ratings.csv')
df = df.sort_values(['IMDB_Rating','Audience_Rating','Title'],ascending=[False,False,True])
df['Audience_Rating'] = df['Audience_Rating'].astype(pd.Int64Dtype())
df['Tomato_Rating'] = df['Tomato_Rating'].astype(pd.Int64Dtype())
df['IMDB Vote Count'] = 1
df['IMDB Vote Count'] = df['IMDB Vote Count'].astype(pd.Int64Dtype())
df.drop('IMDB Matched Movie',axis=1,inplace=True)
df.reset_index(drop=True,inplace=True)
types = df.Type.unique().tolist()
add_selectbox = st.multiselect(
    'Movie Type?',
    types,types)
min_votes = st.slider(
    "Minimum IMDB Votes",
    value=100, min_value=0, max_value=10000, step=10)
st.title('Peacock Ratings')
if add_selectbox is None:
    st.table(df)
else:
    st.table(df[df['Type'].isin(add_selectbox) & (df['IMDB Vote Count'] >= min_votes)])
