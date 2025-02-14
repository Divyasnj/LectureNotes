import cv2
import os

# Input video file
video_path = "nptel.mp4"
output_folder = "screenshots"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Open video file
cap = cv2.VideoCapture(video_path)

# Get video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))  # Frames per second
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # Total frames
duration = total_frames // fps  # Duration of video in seconds

# Interval in seconds
interval = 20
frame_interval = fps * interval  # Convert interval to frame count

frame_count = 0
last_frame_saved = False  # Track if last frame is saved

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break  # Stop if video ends

    # Save frame every 'frame_interval' frames
    if frame_count % frame_interval == 0 or frame_count == total_frames - 1:
        # Calculate timestamp (hh:mm:ss format)
        timestamp_seconds = frame_count // fps
        hours = timestamp_seconds // 3600
        minutes = (timestamp_seconds % 3600) // 60
        seconds = timestamp_seconds % 60
        timestamp = f"{hours:02d}-{minutes:02d}-{seconds:02d}"

        # Save image with timestamp
        screenshot_path = os.path.join(output_folder, f"screenshot_{timestamp}.jpg")
        cv2.imwrite(screenshot_path, frame)
        print(f"Saved: {screenshot_path}")

        if frame_count == total_frames - 1:
            last_frame_saved = True  # Mark last frame as saved

    frame_count += 1

# If last frame wasn't saved, manually capture it
if not last_frame_saved:
    cap.set(cv2.CAP_PROP_POS_FRAMES, total_frames - 1)
    ret, frame = cap.read()
    if ret:
        timestamp = f"{duration // 3600:02d}-{(duration % 3600) // 60:02d}-{duration % 60:02d}"
        screenshot_path = os.path.join(output_folder, f"screenshot_{timestamp}.jpg")
        cv2.imwrite(screenshot_path, frame)
        print(f"Saved Last Frame: {screenshot_path}")

cap.release()
cv2.destroyAllWindows()
