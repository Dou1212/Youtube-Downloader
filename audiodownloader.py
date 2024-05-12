# Importing the YouTube class from the pytube module
from pytube import YouTube

# Defining a function to download a YouTube video
def download_video(url, path="YOUR PATH"):
    try:
        # Creating a YouTube object with the provided URL
        yt = YouTube(url)
        
        # Downloading the audio of the video to the specified path
        yt.streams.get_audio_only().download(output_path=path)
        
        # Printing a message indicating that the audio has been successfully downloaded
        print("Audio downloaded!")
        
    # Catching any exceptions that occur during the download process
    except Exception as e:
        # Printing an error message along with the exception description
        print("ERROR:", e)

# Asking the user to input the URL of the YouTube video they want to download
url_youtube = input("YouTube Video URL: ")

# Calling the function to download the video using the provided URL
download_video(url_youtube)