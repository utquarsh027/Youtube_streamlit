import streamlit as st
import time
from plyer import notification
from pytube import YouTube,Streamquery
import os
import base64

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
        download_video = st.button("Download Video")
        if yt.streams.filter(only_audio=True):
            download_audio = st.button("Download Audio Only")
        if download_video:
            download_file=video.get_highest_resolution().download()
            base,ext=os.path.splitext(download_file)
            new_file=base
            os.rename(download_file,new_file)
            downloaded = True
            if 'DESKTOP_SESSION' not in os.environ: #and os.environ('HOSTNAME')=='streamlit':
    
                with open(new_file, 'rb') as f:
                    bytes = f.read()
                    b64 = base64.b64encode(bytes).decode()
                    href = f'<a href="data:file/zip;base64,{b64}" download=\'{new_file}\'>\
                        Here is your link \
                    </a>'
                    st.markdown(href, unsafe_allow_html=True)
                    download = st.button("Get download link", key="download")
                    if download:
                         download_file= video.get_lowest_resolution().download()
                # st.download_button(label="Download Video",file_name=download_file)   
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
