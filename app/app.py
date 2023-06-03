import streamlit as st
import requests


st.title('Basic todo app')

name = st.text_input("What is your name?", "", placeholder = 'Type Here ...')

if st.button('Submit'):
    res = requests.get(f"http://api:8000/user/{name}").json()
    try:
        st.success(f"Hello {res['user_name']}")
    except:
        res = requests.post(f"http://api:8000/user/{name}").json()
        st.success(f"User {name} created, user_id = {res['user_id']}")
    st.session_state.name_id = res['user_id']

if 'name_id' in st.session_state:
    tasks = requests.get(f"http://api:8000/task/{st.session_state.name_id}").json()
    st.markdown("## Your tasks:")
    for task in tasks['tasks']:
        st.markdown(f"* {task[2]}")

if 'name_id' in st.session_state:
    new_task = st.text_input("New task", "", placeholder = 'Type Here ...')
    if(st.button('Add')):
        adding = requests.post(f"http://api:8000/task/{st.session_state.name_id}", params={'task': new_task}).json()
        st.success(f"Task created, task_id = {adding['task_id']}")