import tkinter
import customtkinter
from pytube import YouTube
import os

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")

        # Get the user's home directory
        home_dir = os.path.expanduser("~")
        download_folder = os.path.join(home_dir, "Downloads")

        video.download(output_path=download_folder)

        finishLabel.configure(text="Downloaded", text_color="green")
    except Exception as e:
        finishLabel.configure(text=f"Download Error: {str(e)}", text_color="red")

    
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_dowloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_dowloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    # Update Progress Bar
    progressBar.set(float(percentage_of_completion) / 100 )


# system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#App frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

#UI elements
title = customtkinter.CTkLabel(app, text="Insert a YT link")
title.pack(padx=10, pady= 10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var) 
link.pack()

# Finished
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download btn
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

#Run app
app.mainloop()
