import streamlit as st
from pytube import YouTube
from io import BytesIO
from pathlib import Path
import time
st.set_page_config(page_title="Download Video", page_icon="🎵", layout="centered", initial_sidebar_state="collapsed")

def download_video_to_buffer(url):
    buffer = BytesIO()
    youtube_video = YouTube(url)
    video = youtube_video.streams.filter(progressive=True,file_extension="mp4").order_by('resolution').desc().first()
    video_720p=video
    default_filename = video_720p.default_filename
    video.stream_to_buffer(buffer)
    return default_filename,buffer

def main():
    downloaded=False
    st.title("Download video from Youtube")
    url = st.text_input("Insert Youtube URL:")
    if url:
        with st.spinner("Downloading video Stream from Youtube..."):
            default_filename, buffer = download_video_to_buffer(url)
        yt=YouTube(url)    
        st.image(yt.thumbnail_url, width=600)   
        st.subheader("Title")
        st.write(default_filename)
        title_vid = Path(default_filename).with_suffix(".mp4").name
        title_audio=Path(default_filename).with_suffix(".mp3").name
        # st.video(buffer, format='video/mpeg')
        st.subheader("Download File")
        st.download_button(
            label="Download audio",
            data=buffer,
            file_name=title_audio,
            mime="audio/mpeg")
        st.download_button(
            label= "Download Video",
            data=buffer,
            file_name=title_vid,
            mime="video/mpeg"
        )   
if __name__ == "__main__":
    main()
