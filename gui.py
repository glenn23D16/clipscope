import tkinter as tk
from data_collection import get_video_data


def analyze_video():
    """
    Fetch details for a specific YouTube video based on the entered video ID and
    update the GUI with the title, views, and likes of that video.
    """
    # Retrieve the video ID from the entry field
    video_id = entry.get()

    # Use the get_video_data function to fetch data about the video
    data = get_video_data(video_id)

    # If data is found for the provided video ID
    if data:
        title = data['snippet']['title']
        views = data['statistics']['viewCount']
        likes = data['statistics']['likeCount']

        # Set the result text to display the video details
        result_text.set(f"Title: {title}\nViews: {views}\nLikes: {likes}")
    else:
        # If no data is found for the video ID, set an appropriate message
        result_text.set("No data found for this video ID.")

# Set up the main tkinter window


root = tk.Tk()
root.title("YouTube Video Analyzer")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Create and place a label prompting the user to enter a video ID
label = tk.Label(frame, text="Enter YouTube Video ID:")
label.pack(padx=10, pady=5)

# Entry field for user to input a video ID
entry = tk.Entry(frame, width=40)
entry.pack(padx=10, pady=5)

# Button to trigger the analyze_video function when clicked
button = tk.Button(frame, text="Analyze", command=analyze_video)
button.pack(padx=10, pady=10)

# Variable to hold and update the result text
result_text = tk.StringVar()
result_label = tk.Label(frame, textvariable=result_text)
result_label.pack(padx=10, pady=10)

# Start the tkinter main loop
root.mainloop()
