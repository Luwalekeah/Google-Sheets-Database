# Lets write SQL we us Limit...probably MySQL Syntax """
# Querying the Dataframe Output using SQL 
# For streamlit_gsheets I had to pip install st-gsheets-connection

import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1JDy9md2VZPz4JbYtRPJLs81_3jUK47nx6GYQjgU8qNY/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

st.subheader("Querying Births on a Date")

st.subheader("The Birth Google Sheet")
data = conn.read(spreadsheet=url, worksheet="Example 1")
st.dataframe(data)

st.subheader("Birth in 2005")
sql = '''
    SELECT
          "date" as Date
        , sum("births") as Births
    FROM
        "Example 1"
    WHERE
        "date" = '1/1/2005'
    GROUP BY "date", "births"
    ORDER BY
        "date" DESC
    LIMIT 10
'''

df_births = conn.query(spreadsheet=url, sql=sql)
st.dataframe(df_births)