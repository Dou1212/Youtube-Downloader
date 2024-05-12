# Import the YouTube class from the pytube module
from pytube import YouTube

# Define a function to download a YouTube video
def download_video(url, path="YOUR_PATH_HERE"):
    try:
        # Create a YouTube object with the provided URL
        yt = YouTube(url)
        
        # Download the video with the highest available resolution to the specified path
        yt.streams.get_highest_resolution().download(output_path=path)
        
        # Print a message indicating that the video has been successfully downloaded
        print("Video downloaded!")
        
    # Catch any exceptions that occur during the download process
    except Exception as e:
        # Print an error message along with the exception description
        print("ERROR:", e)

# Ask the user to input the URL of the YouTube video they want to download
url_youtube = input("YOUTUBE VIDEO URL: ")

# Call the function to download the video using the provided URL
download_video(url_youtube)
