import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
	
st.title('Data Science Job')
	
DATA_URL = ('https://raw.githubusercontent.com/macandcheeseyummy/datajobs_dash/main/data_science_jobs_indeed_usa.csv')
	
@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")
	
col1, col2 = st.columns(2)

with col1:
    st.header('Job Title')
    
    data_val = data['title'].value_counts()
    
    fig, ax = plt.subplots()
    
    ax.pie(data_val.values, labels=data_val.index)
    st.pyplot(fig)
    # st.table(data_val)
    # ax.data_val.plot.pie()
    # st.pyplot(fig)
    # # data['title'].value_counts().plot.pie(ax=ax)

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    # labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    # sizes = [15, 30, 45, 10]
    # explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    # fig1, ax1 = plt.subplots()
    # ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
    #         shadow=True, startangle=90)
    # ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    # plt.show()

with col2:
    st.header('Salary')
