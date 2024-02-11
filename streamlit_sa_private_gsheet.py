import streamlit as st
from streamlit_gsheets import GSheetsConnection


# Include my css file
st.markdown('<style>' + open('style/main.css').read() + '</style>', unsafe_allow_html=True)

conn = st.connection("gsheets", type=GSheetsConnection)

# Center the heading using the css file
st.markdown("""
    <div class="centered-container">
        <h1>Excel as a Database</h1>
    </div>
""", unsafe_allow_html=True)

# Add spacing using margin to the second element
st.markdown("""
    <div style="margin-top: 20px;">
        <h2>Food By County Dataset</h2>
    </div>
""", unsafe_allow_html=True)

data = conn.read(worksheet="food_by_county")
st.dataframe(data)

# st.subheader("Looking at Top 10 GeoType of Colorado by Median_Income Desc only")

# # Existing code for executing a predefined query
# sql = '''
#     SELECT
#            "ind_id","ind_definition","reportyear","race_eth_code"
#             ,"race_eth_name","geotype","geotypevalue","geoname"
#             ,"county_name","county_fips","region_name","region_code"
#             ,"cost_yr","median_income","affordability_ratio"
#             ,"LL95_affordability_ratio","UL95_affordability_ratio"
#             ,"se_food_afford","rse_food_afford"
#     FROM
#         "Food By County"
#     WHERE
#         "geotype" IN ('CO', 'CA')
#     ORDER BY
#         "median_income" DESC
# '''

# df_food = conn.query(sql=sql)
# st.dataframe(df_food)

# User input section
st.subheader("Query Against the Dataset Above")

st.text('MySQL SQL Sample: select distinct ind_id from food_by_county limit 3')
# Text area for user to input SQL query
user_query = st.text_area("Enter your SQL query here:")

# Button to execute user input query
if st.button("Run User Query"):
    if user_query:
        try:
            result_data = conn.query(sql=user_query)
            st.dataframe(result_data)
        except Exception as e:
            st.error(f"Error executing user input query: {e}")
    else:
        st.warning("Please enter a valid SQL query.")
