# On a Public worksheet use the value after the gid in the url as the worksheet name

# To execute open a terminal and type:
# streamlit run streamlit_app_choose_ws.py

# A web-browser window will open with the output

import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1JDy9md2VZPz4JbYtRPJLs81_3jUK47nx6GYQjgU8qNY/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

# usecols=[0, 1]
data = conn.read(spreadsheet=url, usecols=list(range(2)), worksheet="Example 1")
st.dataframe(data)