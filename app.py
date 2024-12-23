import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the app
st.title("Movie Data Analysis App")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV file
    data = pd.read_csv(uploaded_file)
    
    # Show dataframe
    st.write("### Data Preview:")
    st.write(data.head())

    # Show basic info
    st.write("### Basic Information:")
    st.write(data.info())

    # Show summary statistics
    st.write("### Summary Statistics:")
    st.write(data.describe())

    # Sidebar for user inputs
    st.sidebar.header("Analysis Options")
    
    # Dropdown to select column for visualization
    column = st.sidebar.selectbox("Select column to visualize", data.columns)

    # Plot distribution
    st.write(f"### Distribution of {column}")
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], kde=True)
    st.pyplot(plt)

   

    # Top N movies based on rating or other numerical column
    st.sidebar.subheader("Top N Movies")
    top_n = st.sidebar.slider("Select N", min_value=1, max_value=50, value=10)
    sort_by = st.sidebar.selectbox("Sort by", data.select_dtypes(include=["float", "int"]).columns)

    st.write(f"### Top {top_n} Movies by {sort_by}")
    st.write(data.nlargest(top_n, sort_by))

    # Filter by genre
    st.sidebar.subheader("Filter by Genre")
    genres = st.sidebar.multiselect("Select genres", data['Genre'].unique())

    if genres:
        filtered_data = data[data['Genre'].isin(genres)]
        st.write(f"### Movies in {', '.join(genres)} Genre")
        st.write(filtered_data)

