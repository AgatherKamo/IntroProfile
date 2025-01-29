
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 11:32:25 2025

@author: canka
"""

import streamlit as st
import pandas as pd

# Title of the app
st.title("Optimizing Quality of User Experience in Mobile Edge Computing Environments")

# Collect basic information
name = "Kamogelo Seema"
field = "Computer Science"
institution = "University of Limpopo"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Abstract")
st.write("The Multi-Access Edge Computing server extends the capabilities of cloud computing to the edge environment so that it processes data from mobile end devices. The End User Equipment’s Quality of Service has degraded, increasing the latency between edge devices and the MEC server. Literature has shown that utilizing the Fog Computing or Multi-Access edge increases the quality of User experience but exposes the data stored to attackers, whereas when optimizing the QoE, the cached data becomes less secure. This paper aims to optimize the Quality of User Experience for better security performance in data delivery and achieve low latency. With the use of MATLAB software and adjusting the time it takes which is Time to Live (TTL) to store and release cached data in the MEC environment the data was analysed using different devices in a network. The cached data ratio mechanism displayed those certain devices still had low latency, by analysis we observed that devices specifications (Random Access Memory) also have an impact on latency. The core use of our resolution is the CAPIC Algorithm, Cache Based on Popularity and Class (CAPIC) algorithm is a caching algorithm that uses two steps to determine where to store content and how much cache storage to use .Keeping our High priority data at below a 2 level of access time as to strengthen quality of Experience and maximising  the Low priority access level time to satisfy User daily request. Our results classified our data in proactive and tiered content, with this classification we now use optimize our results by comparing different RAM sizes as one of the factors. Now the popularity of data demands frequent travel to the Edge and user device but to ensure Quality User satisfaction their data is classified and in priority and tier level. Results have shown significant expansion of TTL in data frequently used and security in High priority, this research now combines user satisfaction and data security.")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
st.header("Contact Information")
email = "cankamogelo17@gmail.com"
st.write(f"You can reach {name} at {email}.")
