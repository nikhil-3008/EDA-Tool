# Core Pkgs
import streamlit as st 
import openai
# EDA Pkgs
import pandas as pd 
import numpy as np 

# Data Viz Pkg
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("Agg")
import seaborn as sns 

openai.api_key = "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"

def main():
    """Semi Automated ML App with Streamlit """

    activities = ["EDA","Plots"]    
    choice = st.sidebar.selectbox("Select Activities",activities)

    if choice == 'EDA':
        st.subheader("Exploratory Data Analysis Tool")

        data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])
        if data is not None:
            df = pd.read_csv(data)
            st.dataframe(df.head())
            
            # ... other EDA operations ...

    elif choice == 'Plots':
        st.subheader("Data Visualization")
        data = st.file_uploader("Upload a Dataset", type=["csv", "txt", "xlsx"])
        if data is not None:
            df = pd.read_csv(data)
            st.dataframe(df.head())

            # ... other plotting operations ...

if __name__ == '__main__':
    main()
