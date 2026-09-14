import streamlit as st
import pandas as pd

# 1. Dashboard Header
st.title("🧬 Advanced Genomic Variant Dashboard")
st.subheader("Client: BioGen Tech (Dr. Aris Thorne)")
st.write("Secure portal: Please upload the raw mutation report to generate live visualizations.")

# 2. File Uploader Widget
uploaded_file = st.file_uploader("Upload CSV File", type="csv")

# 3. Dynamic Data Processing
if uploaded_file is not None:
    st.success("Data securely loaded! System ready for analysis.")
    df = pd.read_csv(uploaded_file)
    
    # --- NEW FEATURE: Dynamic Sidebar Controls ---
    st.sidebar.header("⚙️ Dashboard Controls")
    
    # Automatically read whatever columns are in the CSV and create a dropdown
    filter_column = st.sidebar.selectbox("1. Select a column to filter by:", df.columns)
    
    # Create checkboxes based on the client's chosen column
    unique_values = df[filter_column].unique()
    selected_values = st.sidebar.multiselect(f"2. Select values for {filter_column}:", unique_values, default=unique_values)
    
    # Filter the dataset
    filtered_df = df[df[filter_column].isin(selected_values)]
    
    # --- NEW FEATURE: Live Metric Cards ---
    st.write("### 📈 Quick Insights")
    st.metric(label="Total Rows Remaining", value=len(filtered_df))
    
    # Display the filtered Data Table
    st.write("### 🗄️ Filtered Database")
    st.dataframe(filtered_df)
    
    # --- Dynamic Chart Engine ---
    st.write("### 📊 Customizable Data Chart")
    
    # Find only the columns that contain numbers (to prevent chart crashing)
    numeric_columns = df.select_dtypes(include='number').columns.tolist()
    
    if len(numeric_columns) > 0:
        y_axis_col = st.sidebar.selectbox("3. Select metric for Chart Height (Y-Axis):", numeric_columns)
        # Draw the chart using the chosen numeric column
        st.bar_chart(data=filtered_df, y=y_axis_col, color="#ff4b4b")
    else:
        st.info("No numeric data found in this CSV to create a chart.")