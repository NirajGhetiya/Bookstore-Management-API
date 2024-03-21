import pandas as pd
import streamlit as st


# from sample import data as sample_data

st.set_page_config(page_title='Trackwizz Connect', page_icon='📊', layout='wide')
df= None
uploaded_file= st.file_uploader("Upload xecel or csv file", type=[".xlsx",".csv"]) 
if uploaded_file is  not None:
    try:
            df = pd.read_csv(uploaded_file)  # For CSV files
    except Exception as e:
         error = "Error reading file: {0}".format(e)
    try:
                df = pd.read_excel(uploaded_file)  # For XLSX files
    except Exception as e:
                st.error("Error: Unable to read file. Please upload a valid CSV or XLSX file.")
def generate_image1_path(row): 
    return f'<img src="http://127.0.0.1:5500/{row["img1_path"]}" width="100px">'
def generate_image2_path(row):
    return f'<img src="http://127.0.0.1:5500/{row["img2_path"]}" width="300px">'
if df is not None:
    st.sidebar.header("Filters")
    success = st.sidebar.selectbox(
        "Select success: ",
       options=df["success"].unique(),
      
    )
    sdf= df.query("success == @success ")
    
    match= st.sidebar.selectbox(
        "Select match: ",
       options=sdf["match"].unique()
    )
    human = st.sidebar.selectbox(
        "Select human: ",
       options=sdf["human"].unique(),
    )
    message = st.sidebar.selectbox(
        "Select message: ",
       options=sdf["message"].unique()
    )
    # match_percentage = None
    if success == True:
         match_percentage =  st.sidebar.slider(
         'Match Percentage',
          min_value=0.,
          max_value=1.,
          value=(0.,1.)
        )
         sdf= sdf.query("match_percentage>=@match_percentage[0] & match_percentage <= @match_percentage[1] & match== @match")
    
    sdf= sdf.query("human==@human & message == @message")
    sdf["img1_path"] =  sdf.apply(generate_image1_path, axis=1)
    sdf["img2_path"] =  sdf.apply(generate_image2_path, axis=1)
    img1 = sdf.pop( "img1_path" )
    img2 = sdf.pop( "img2_path" )
    sdf.insert(1,"Image_1",img1)
    sdf.insert(2,"Image_2",img2)
    st.write(sdf.to_html(escape=False), unsafe_allow_html=True)
