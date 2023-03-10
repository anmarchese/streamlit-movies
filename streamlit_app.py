import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

df = pd.read_csv('movie_ratings.csv')
df = df.sort_values(['IMDB_Rating','Audience_Rating','Title'],ascending=[False,False,True])
df['Audience_Rating'] = df['Audience_Rating'].astype(pd.Int64Dtype())
df['Tomato_Rating'] = df['Tomato_Rating'].astype(pd.Int64Dtype())
df['IMDB Vote Count'] = df['IMDB Vote Count'].astype(pd.Int64Dtype())
for i in df.columns:
    if 'Genre_' in i:
        df[i] = df[i].fillna(0)
        df[i] = df[i].astype(int)
df['IMDB Vote Count'] = df['IMDB Vote Count'].fillna(0)
df.drop('IMDB Matched Movie',axis=1,inplace=True)
df.reset_index(drop=True,inplace=True)
types = df.Type.unique().tolist()
genres = [i.split('Genre_')[1] for i in df.columns if 'Genre_' in i]
add_selectbox = st.multiselect(
    'Movie Type?',
    types,types)
genre_box = st.multiselect(
    'Any of these genres',genres,['documentary','sport','music','biography'])
must_genre = st.multiselect(
    'Must be all of these of these genres',genres,[])
min_votes = st.slider(
    "Minimum IMDB Votes",
    value=100, min_value=0, max_value=10000, step=10)
st.title('Peacock Ratings')
#show is any of the selected genre coklumns are 1
selected_genres = [f'Genre_{i}' for i in genre_box]
show_df = df[df[selected_genres].sum(axis=1) > 0]
if must_genre:
    must_genres = [f'Genre_{i}' for i in must_genre]
    show_df = show_df[show_df[must_genres].sum(axis=1) == len(must_genre)]
if add_selectbox is None:
    st.table(show_df[show_df.columns[:8]])
else:
    st.table(show_df[(show_df['Type'].isin(add_selectbox)) & (show_df['IMDB Vote Count'] >= min_votes)][df.columns[:8]])
