import streamlit as st
import pandas as pd

# 1. Dashboard Header
st.title("🧬 Genomic Variant Dashboard")
st.subheader("Client: BioGen Tech (Dr. Aris Thorne)")
st.write("Secure portal: Please upload the raw mutation report to generate live visualizations.")

# 2. File Uploader Widget
uploaded_file = st.file_uploader("Upload CSV File", type="csv")

# 3. Data Processing & Visualization
if uploaded_file is not None:
    st.success("Data securely loaded! System ready for analysis.")
    
    # Read the uploaded CSV file using Pandas
    df = pd.read_csv(uploaded_file)
    
    # Display an interactive Data Table
    st.write("### 🗄️ Raw Mutation Database")
    st.dataframe(df)  # This creates a table the client can scroll and sort!
    
    # Extract the top 5 highest quality mutations
    top_5 = df.head(5)
    
    # Draw a live, interactive Bar Chart
    st.write("### 📊 Top 5 Mutations by Quality Score")
    st.bar_chart(data=top_5, x="GENE", y="QUAL", color="#1f77b4")