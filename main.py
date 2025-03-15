import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Disease Risk Analysis Dashboard", layout="wide")

# General Title and Description
st.title("Disease Risk Analysis Dashboard")
st.markdown("""
This dashboard provides an analysis of disease risk trends, relative risk mapping, and overlay analysis.
It includes data visualizations and geographic risk distributions over time over selected places in Ghana.

**Author:** [Vincent Osei](https://www.linkedin.com/in/vincent-osei-96156a256/)
            
**Use the sidebar to view specific result**
""")

# Sidebar for navigation
st.sidebar.header("Select Analysis Section")
sections = [
    "Trend in Relative Risk of Onchocerciasis",
    "Trend in Relative Risk of Lymphatic Filariasis",
    "Mapping of Relative Risk",
    "Overlay Analysis",
]
selected_section = st.sidebar.radio("Choose a section to view:", sections)

# Trend in Relative Risk of Onchocerciasis
if selected_section == "Trend in Relative Risk of Onchocerciasis":
    st.header("Trend in Relative Risk of Onchocerciasis")
    st.markdown("This section visualizes the trend in relative risk of onchocerciasis over different time periods.")
    
    data_oncho = pd.DataFrame({
        "Date": ["Before 2001", "2001-2005", "2006-2010", "2011-2016"],
        "Relative Risk": [95.82, 117.92, 286.35, 126.33]
    })
    fig_oncho = px.line(data_oncho, x="Date", y="Relative Risk", markers=True, title="Trend in Onchocerciasis")
    st.plotly_chart(fig_oncho)

# Trend in Relative Risk of Lymphatic Filariasis
elif selected_section == "Trend in Relative Risk of Lymphatic Filariasis":
    st.header("Trend in Relative Risk of Lymphatic Filariasis")
    st.markdown("This section presents the trend in relative risk of lymphatic filariasis across different periods.")

    data_lf = pd.DataFrame({
        "Date": ["Before 2001", "2001-2006", "After 2006"],
        "Relative Risk": [70.68, 194.99, 288.18]
    })
    fig_lf = px.line(data_lf, x="Date", y="Relative Risk", markers=True, title="Trend in Lymphatic Filariasis")
    st.plotly_chart(fig_lf)

# Mapping of Relative Risk
elif selected_section == "Mapping of Relative Risk":
    st.header("Mapping of Relative Risk")
    st.markdown("These maps illustrate the relative risk distribution of lymphatic filariasis and onchocerciasis over time.")

    st.image("maps/LF/LF(before-2001).jpg", caption="Relative risk Map of LF (before-2001)")
    st.image("maps/LF/LF(2001-2005).jpg", caption="Relative risk Map of LF (2001-2005)")
    st.image("maps/LF/LF(after-2005).jpg", caption="Relative risk Map of LF (after 2005)")

    st.image("maps/ONCHO/onch(before-2001).jpg", caption="Relative risk Map of Onchocerciasis (before 2001)")
    st.image("maps/ONCHO/onch(2001-2005).jpg", caption="Relative risk Map of Onchocerciasis (2001-2005)")
    st.image("maps/ONCHO/onch(2006-2010).jpg", caption="Relative risk Map of Onchocerciasis (2006-2010)")
    st.image("maps/ONCHO/onch(2011-2016).jpg", caption="Relative risk Map of Onchocerciasis (2011-2016)")

# Overlay Analysis
elif selected_section == "Overlay Analysis":
    st.header("Overlay Analysis")
    st.markdown("These maps show the co-endemic regions of lymphatic filariasis and onchocerciasis.")

    st.image("maps/coEndemic/before-2001.jpg", caption="Overlay Map (Before 2001)")
    st.image("maps/coEndemic/2001-2005.jpg", caption="Overlay Map (2001-2005)")
    st.image("maps/coEndemic/after-2005.jpg", caption="Overlay Map (After 2005)")
