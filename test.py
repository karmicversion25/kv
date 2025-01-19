import subprocess
import os


def cut_last_5_seconds(input_path, output_path):
    try:
        # Get the total duration of the video
        result = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", input_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        duration = float(result.stdout.strip())
        new_duration = duration - 5

        if new_duration <= 0:
            print("Error: Video duration is less than or equal to 5 seconds.")
            return

        # Use FFmpeg to cut the video
        subprocess.run(
            ["ffmpeg", "-i", input_path, "-t", str(new_duration), "-c", "copy", output_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        print(f"Video saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
input_video = "hero-video-input.mp4"  # Replace with your input video file
output_video = "hero-video.mp4"  # Replace with your desired output file
cut_last_5_seconds(input_video, output_video)
