
"""
Name: Alex Chau
CS230: Section SN1
Data: Colleges and Universities in the United States
URL: Link to your web application online (see extra credit)

Description: This program ...


"""
import streamlit as st

import pandas as pd


df = pd.read_csv(("/Users/Alex/hello/project/schools.csv"), usecols = ["NAME","LAT", "LON", "CBSATYPE", "STATE", "CBSA"])
df.dropna(subset = ["LAT"], inplace=True)
df.dropna(subset = ["LAT"], inplace=True)
df.rename(columns = {"LAT":"lat"}, inplace=True)
df.rename(columns = {"LON":"lon"}, inplace=True)
states_list = df["STATE"]
df = df[pd.to_numeric(df['CBSA'], errors='coerce').notnull()]

def get_states(states_list):
 states = []
 for x in df["STATE"]:
  if x not in states:
   states.append(x)
  states.sort()
 return states

unique_states = get_states(states_list)
print(unique_states)

df0 = df[df.CBSATYPE == 0]
df1 = df[df.CBSATYPE == 1]
df2 = df[df.CBSATYPE == 2]

print(df1)
st.title("Universities and Colleges in America")

CBSA_filter = st.sidebar.slider('CBSA', 10000, 50000, 0)

st.sidebar.header("CBSA Rating Slider")
filtered_data = df[df["CBSA"] >= CBSA_filter]
st.subheader(f'Map of all colleges with at least a CBSA rating of {CBSA_filter}')
st.map(filtered_data)
st.markdown("> A Core Based Statistical Area (CBSA) consists of a U.S. county or counties or equivalent entities associated with at least one urban core (urbanized area or urban cluster) with a population of at least 10,000 along with any adjacent counties having a high degree of social and economic integration with the core as measured through commuting ties with the counties containing the core. CBSAs are categorized as being either Metropolitan or Micropolitan. Each Metropolitan Statistical Area must have at least one urbanized area of 50,000 or more inhabitants. Each Micropolitan Statistical Area must have at least one urban cluster with a population of at least 10,000 but less than 50,000.\n\n—ArcGIS")

values = st.slider(“Price range”, float(df.price.min()), 1000., (50., 300.))
f = px.histogram(df.query(f”price.between{values}”), x=”price”, nbins=15, title=”Price distribution”)
f.update_xaxes(title=”Price”)
f.update_yaxes(title=”No. of listings”)
st.plotly_chart(f)



st.header("Colleges by CBSA Type Rating ")
st.sidebar.header("CBSA Type Viewer")
minimum = st.sidebar.number_input("Minimum", min_value=0)
maximum = st.sidebar.number_input("Maximum", min_value=0, value=2)
if minimum > maximum:
 st.error("Please enter a valid range")
else:
 df.query("@minimum<=CBSATYPE<=@maximum").sort_values("CBSATYPE", ascending=False)\
.head(10000)[["NAME", "CBSATYPE"]]

desired_label = st.sidebar.selectbox('Filter to:', unique_states)
st.sidebar.header("CBSA Rating Slider")
filtered_data = df[df["STATE"] == desired_label]
st.sidebar.subheader(f'Colleges located within {desired_label}')
st.sidebar.map(filtered_data)

