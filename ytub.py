import mysql.connector as sql
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine


#database
engine = create_engine('mysql+pymysql://root:YES@localhost:3306/yout')

#  retrieve channel data from MySQL
def get_channel_data():
    query = "SELECT * FROM channels"
    df = pd.read_sql(query, engine)
    return df

#  retrieve video data from MySQL
def get_video_data():
    query = "SELECT * FROM videos"
    df = pd.read_sql(query, engine)
    return df

#  retrieve comment data from MySQL
def get_comment_data():
    query = "SELECT * FROM comments"
    df = pd.read_sql(query, engine)
    return df


def main():
    st.title("YouTube Data Harvesting and Warehousing")

    # Option to select a channel and migrate data to SQL
    channel_df = get_channel_data()
    channel_name = st.selectbox("Select a channel", channel_df['channel_name'])
    if st.button("Migrate to SQL"):
        channel_data = channel_df[channel_df['channel_name'] == channel_name]
        channel_data.to_sql('selected_channel', engine, if_exists='replace', index=False)
        st.success(f"Data for channel '{channel_name}' migrated to SQL successfully.")

    # Option to search and retrieve data from SQL
    search_option = st.selectbox("Search option", ["Videos"])
    if search_option == "Videos":
        video_df = get_video_data()
        st.subheader("Video Data")
        st.dataframe(video_df)
    

# Run the Streamlit app
if __name__ == '__main__':
    main()
