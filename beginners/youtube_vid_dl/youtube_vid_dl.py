from pytube import YouTube

# Path to save youtube file to
SAVE_PATH = '/home/frank_quoc/forty_two_python_projects/beginners/youtube_vid_dl'

def dl_youtube_vid(link):
    """Takes in youtube link and downloads to the path file directory above."""

    try:
        yt = YouTube(link)
    except:
        print("The link did not work for some reason.")

    # Gets the first stream
    stream = yt.streams.first()

    # Shortens the youtube filename
    filename = stream.title[:25] + "..."
    try:
        stream.download(SAVE_PATH, filename=filename)
    except:
        print("Could not download.")

    print("Download Completed.")

if __name__ == '__main__':
    link = input("Paste your youtube link here: ")
    dl_youtube_vid(link)