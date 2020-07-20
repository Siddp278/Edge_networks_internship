#This is a file containing basuic fucntion which eases my work, hopefully.

import streamlit as st
def easy(s,n):
    """
    :param s:anything that has to be printed
    :param n: choice of what type of font is needed(is an integer)
    :return: nothing
    """

    text = s
    if n == 1:
        st.title(text)
    if n == 2:
        st.text(text)
    if n == 3:
        st.header(text)
    if n == 4:
        st.subheader(text)
    if n == 5:
        st.write(text)