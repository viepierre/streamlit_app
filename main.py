import streamlit as st
import pandas as pd

data = {
    'Series_1' : [1, 3, 4, 7],
    'Series_2' : [10, 40, 100, 250]
}
df = pd.DataFrame(data)

st.title('Our First streamlit app')
st.subheader('Introducing Streamlit in Automate everything with python')
st.write(''' This is our
first web app.
Enjoy it !
''')
st.write(df)
st.line_chart(df)