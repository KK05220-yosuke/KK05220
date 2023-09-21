import streamlit as st
import random

st.title("テスト勉強")

if st.button("今日すべき教科"):

    results = ["国語","英語","数学","化学","物理","地理","公共","公共","公共","公共","公共","公共","公共","公共"]
    result = random.choice(results)
    st.write(f"結果:{result}")
