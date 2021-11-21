from pytube import YouTube
link=input("Enter your youtube video link")
print("Downloading...")
YouTube(link).streamsfirst().dowenload()
print("Video downloaded Successfully")
