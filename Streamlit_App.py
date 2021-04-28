
"""
Name: Alex Chau
CS230: Section SN1
Data: Colleges and Universities in the United States
URL: Link to your web application online (see extra credit)

Description: This program takes a look at the CBSA rating of different colleges across the US
and hosts multiple interactive aspects for the user to experience and learn more about.


"""
import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

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
st.title("An Analytical Look at the CBSA Rating of Universities and Colleges in America\n\n\n")
st.sidebar.header("Breakdown by State")

pics = {
    "Panoramic View of Bentley University": "https://www.bentley.edu/sites/default/files/inline-images/panorama%20for%20strategic%20planning_0.jpg",
    "Arial View of Bentley University": "https://www.bentley.edu/sites/default/files/styles/media_image/public/2020-04/Copy%20of%20Bentley%20Fall%20Dawn%20%28no%20watermark%29.jpeg?h=56ecf050&itok=b4YS0U5l",
    "Bentley University's Library": "https://www.bentley.edu/sites/default/files/2018/09/10/US%20News_Sidi_Campus-edit.jpg"
}
pic = st.selectbox("\n\n\n\n\n\n\n", list(pics.keys()), 0)
st.image(pics[pic], use_column_width=True, caption=pics[pic])

st.markdown("> A Core Based Statistical Area (CBSA) consists of a U.S. county or counties or equivalent entities associated with at least one urban core (urbanized area or urban cluster) with a population of at least 10,000 along with any adjacent counties having a high degree of social and economic integration with the core as measured through commuting ties with the counties containing the core. CBSAs are categorized as being either Metropolitan or Micropolitan. Each Metropolitan Statistical Area must have at least one urbanized area of 50,000 or more inhabitants. Each Micropolitan Statistical Area must have at least one urban cluster with a population of at least 10,000 but less than 50,000.\n\n—ArcGIS")

CBSA_filter = st.slider('CBSA Rating Slider', 10000, 50000, 10000)


filtered_data = df[df["CBSA"] >= CBSA_filter]
st.subheader(f'Map of all colleges with at least a CBSA rating of {CBSA_filter}')
st.map(filtered_data)
st.markdown("> A breakdown of colleges around the country filtered by their CBSA rating")

st.subheader(f'Distribution of CBSA Rating Among Colleges in the US')
plt.figure()
plt.title('CBSA Rating Distribution')
sns.set_style('darkgrid')
sns.distplot(df['CBSA'])
st.pyplot()
st.markdown("> There is a clear bimodal pattern, with the left mound having a median of about 18,000 and the right mound having a median of about 37,000 ")

st.set_option('deprecation.showPyplotGlobalUse', False)
st.header("Colleges by CBSA Type Rating ")
minimum = st.number_input("Minimum", min_value=0)
maximum = st.number_input("Maximum", min_value=0, value=2)
if minimum > maximum:
 st.error("Please enter a valid range")
else:
 df.query("@minimum<=CBSATYPE<=@maximum").sort_values("CBSATYPE", ascending=False)\
.head(10000)[["NAME", "CBSATYPE"]]

print(filtered_data)


desired_label = st.sidebar.selectbox('Filter to:', unique_states)
filtered_data = df[df["STATE"] == desired_label]
st.sidebar.subheader(f'Colleges located within {desired_label}')
st.sidebar.map(filtered_data)
st.markdown("> A breakdown of which colleges are categorized in each CBSA Type.  ")

st.sidebar.dataframe(df.query("STATE==@desired_label").sort_values("CBSA", ascending=False)\
.head(10000)[["NAME", "CBSA"]])
