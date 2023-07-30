from pytube import YouTube

'''
install pytube with: `pip install pytube`
Python script to download a YouTube video as a .mp3 file.
Run the script from the command line and enter a YouTube video URL.
The video will be downloaded to the given directory in `output_path` as .mp3 file.
'''


def download_youtube_video_as_mp3(video_url, output_path):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the audio stream with the highest quality available
        audio_stream = yt.streams.filter(
            only_audio=True, file_extension='mp4').first()

        # Download the audio stream
        print("Downloading audio...")
        audio_stream.download(output_path=output_path)

        # Rename the downloaded file to have a .mp3 extension
        mp4_file_path = audio_stream.default_filename
        mp3_file_path = mp4_file_path[:-4] + ".mp3"
        mp4_file_path = f"{output_path}/{mp4_file_path}"
        mp3_file_path = f"{output_path}/{mp3_file_path}"
        import os
        os.rename(mp4_file_path, mp3_file_path)

        print(f"Download complete: {mp3_file_path}")

    except Exception as e:
        print(f"Error: {str(e)}")


video_url = input('Enter youtube link: ')

# Replace 'YOUR_OUTPUT_PATH' with the directory where you want to save the downloaded .mp3 file
output_path = './music'

download_youtube_video_as_mp3(video_url, output_path)
