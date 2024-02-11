import os
import streamlit as st
from streamlit_gsheets import GSheetsConnection
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve environment variables
gsheets_worksheet = os.environ.get("GSHEETS_WORKSHEET")
gsheets_spreadsheet = os.environ.get("spreadsheet")
gsheets_type = os.environ.get("type")
gsheets_project_id = os.environ.get("project_id")
gsheets_private_key_id = os.environ.get("private_key_id")
gsheets_private_key = os.environ.get("private_key")
gsheets_client_email = os.environ.get("client_email")
gsheets_client_id = os.environ.get("client_id")
gsheets_auth_uri = os.environ.get("auth_uri")
gsheets_token_uri = os.environ.get("token_uri")
gsheets_auth_provider_x509_cert_url = os.environ.get("auth_provider_x509_cert_url")
gsheets_client_x509_cert_url = os.environ.get("client_x509_cert_url")

# Initialize GSheetsConnection
conn = st.connection(
    "gsheets",
    type=GSheetsConnection,
    worksheet=gsheets_worksheet,
    spreadsheet=gsheets_spreadsheet,
    type=gsheets_type,
    project_id=gsheets_project_id,
    private_key_id=gsheets_private_key_id,
    private_key=gsheets_private_key,
    client_email=gsheets_client_email,
    client_id=gsheets_client_id,
    auth_uri=gsheets_auth_uri,
    token_uri=gsheets_token_uri,
    auth_provider_x509_cert_url=gsheets_auth_provider_x509_cert_url,
    client_x509_cert_url=gsheets_client_x509_cert_url
)

# Include your CSS file
st.markdown('<style>' + open('style/main.css').read() + '</style>', unsafe_allow_html=True)

# Center the heading using the CSS file
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

# Read data from the specified worksheet
data = conn.read(worksheet=gsheets_worksheet)
st.dataframe(data)

st.subheader("Looking at Top 10 GeoType of Colorado by Median_Income Desc only")


# Existing code for executing a predefined query
# sql = '''
#     SELECT
#         "ind_id","ind_definition","reportyear","race_eth_code"
#         ,"race_eth_name","geotype","geotypevalue","geoname"
#         ,"county_name","county_fips","region_name","region_code"
#         ,"cost_yr","median_income","affordability_ratio"
#         ,"LL95_affordability_ratio","UL95_affordability_ratio"
#         ,"se_food_afford","rse_food_afford"
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
