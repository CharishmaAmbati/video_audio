import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello *world!*
""")

df = pd.DataFrame([1, 4, 6, 8])
print(df)
st.line_chart(df)
