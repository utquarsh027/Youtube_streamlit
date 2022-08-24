import streamlit as st
import time
from plyer import notification
from pytube import YouTube
import os
st.title("Youtube Video Downloader")
st.text("")

#Url input
url=st.text_input(label="Enter url of the video you want to download",placeholder="YouTube url")
if url!="":
    yt=YouTube(url)
    #getting thumbnail of the given url
    st.image(yt.thumbnail_url, width=600)
    st.subheader(f'''{yt.title}''')

    video=yt.streams
    if len(video)>0:
        downloaded,download_audio=False,False
        st.text("Enter a destination on your system to download")
        destination1=st.text_input(label="",placeholder="Directory/Location on your computer")
        download_video = st.button("Download Video")
        if yt.streams.filter(only_audio=True):
            download_audio = st.button("Download Audio Only")
        if download_video:
            download_file=video.get_highest_resolution().download()
            base,ext=os.path.splitext(download_file)
            new_file=base
            os.rename(download_file,new_file)
            downloaded = True    
            
        if download_audio:
            download_file1= video.filter(only_audio=True).first().download()
            base,ext=os.path.splitext(download_file1)
            new_file=base+'.mp3'
            os.rename(download_file1,new_file)
            downloaded = True
        if downloaded:
            #result
#             notification.notify(title=yt.title[0:40]+"...",
#                     message="has been successfully downloaded",
#                     timeout=2)
#             time.sleep(10)
            st.subheader("Download Complete")
    else:
        st.subheader("Sorry, this video can not be downloaded")   
