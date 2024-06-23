import streamlit as st
import pickle
import numpy as np

books_name = pickle.load(open('books_name.pkl','rb'))
ratings = pickle.load(open('final_rating.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))
book_pivot = pickle.load(open('book_pivot.pkl','rb'))

def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for name in book_name[0]:
        ids = np.where(ratings['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = ratings.iloc[idx]['img_url']
        poster_url.append(url)

    return poster_url

def recommend(book_name):
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance,suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1),n_neighbors = 6)
    recommended_books = []

    poster_url = fetch_poster(suggestion)

    for i in range(len(suggestion)):
            books = book_pivot.index[suggestion[i]]
            for j in books:
                recommended_books.append(j)
    return recommended_books , poster_url


st.title('Book Recommender System')


selected_book_name = st.selectbox(
        'select book name',
         books_name)


if st.button('Recommend'):
    recommended_books,poster_url = recommend(selected_book_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_books[1])
        st.image(poster_url[1])
    with col2:
        st.text(recommended_books[2])
        st.image(poster_url[2])
    with col3:
        st.text(recommended_books[3])
        st.image(poster_url[3])
    with col4:
        st.text(recommended_books[4])
        st.image(poster_url[4])
    with col5:
        st.text(recommended_books[5])
        st.image(poster_url[5])


