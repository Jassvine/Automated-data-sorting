import streamlit as st
import pandas as pd

# Read in the first dataset
df1 = pd.read_excel(r'C:\Users\JeyabalaSund\Desktop\JassDocs\INTERN_JJ\PROJECTS\APC_Alarm_Oee_SRM\Alarm_CompileAll_ApcTrendsuit\APCTrendsuitAlarm_renamed.xlsx')

# Read in the second dataset
df2 = pd.read_excel(r'C:\Users\JeyabalaSund\Desktop\JassDocs\INTERN_JJ\PROJECTS\APC_Alarm_Oee_SRM\Alarm_CompileAll_ApcTrendsuit\AlarmCompileAll_SIT006_renamed.xlsx')

# Identify the common columns between the two datasets
common_columns = list(set(df1.columns).intersection(df2.columns))

# Add a radio button widget to allow the user to choose the type of merge
st.sidebar.markdown("Choose the type of merge:")
merge_type = st.sidebar.radio("", ("Union", "Inner Join", "Left Join"))

if merge_type == "Union":
    # Ask the user whether they want to retain duplicate rows
    retain_duplicates = st.sidebar.checkbox("Retain duplicate rows?")

    if retain_duplicates:
        # Perform a union using pd.concat
        merged_df = pd.concat([df1, df2])
    else:
        # Perform a union using pd.concat and drop_duplicates
        merged_df = pd.concat([df1, df2]).drop_duplicates()

elif merge_type == "Inner Join":
    # Ask the user which column they want to join on
    join_column = st.sidebar.selectbox("Choose a column to join on:", common_columns)

    # Perform an inner join using pd.merge
    merged_df = pd.merge(df1, df2, on=join_column, how="inner")

elif merge_type == "Left Join":
    # Ask the user which column they want to join on
    join_column = st.sidebar.selectbox("Choose a column to join on:", common_columns)

    # Perform a left join using pd.merge
    merged_df = pd.merge(df1, df2, on=join_column, how="left")

# Display the merged dataframe
st.write(merged_df)
