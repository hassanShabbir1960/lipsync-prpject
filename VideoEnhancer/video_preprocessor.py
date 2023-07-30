import cv2
import os
from multiprocessing import Pool

class VideoToFrames:
    """
    Convert a video file into individual frames saved as images.

    Attributes:
    - video_path (str): Path to the input video file.
    - output_dir (str): Directory where the output image frames will be saved.
    - frame_rate (int): Frames per second in the video.
    """

    def __init__(self, video_path, output_dir):
        """
        Initialize the VideoToFrames with video path and output directory.

        Args:
        - video_path (str): Path to the video file.
        - output_dir (str): Directory to save the output image frames.
        """
        self.video_path = video_path
        self.output_dir = output_dir
        self.frame_rate = 30  # default frame rate

        # Create output directory if it doesn't exist
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def _split_frame(self, frame_info):
        """
        Extract and save a specific frame from the video.

        Args:
        - frame_info (tuple): Contains the video path and frame number to extract.
        """
        video_path, frame_no = frame_info

        cap = cv2.VideoCapture(video_path)
        # Set the video capture to read the specific frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)

        ret, frame = cap.read()
        if ret:
            # Save the extracted frame as an image
            output_file = os.path.join(self.output_dir, f"frame_{frame_no:04d}.jpg")
            cv2.imwrite(output_file, frame)

        cap.release()

    def split_to_frames(self, processes=4):
        """
        Split the video into individual frames using multiple processes.

        Args:
        - processes (int): Number of processes to use for the conversion.
        """
        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            raise ValueError("Unable to open the video file!")

        # Determine frame rate and total frames in the video
        self.frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        cap.release()

        # Define the work for each process: which frames to extract from which videos
        frame_infos = [(self.video_path, frame_no) for frame_no in range(total_frames)]

        # Use multiprocessing to extract frames
        with Pool(processes=processes) as pool:
            pool.map(self._split_frame, frame_infos)

    def _extract_audio(self):
        """
        Extract and save the audio from the video as a WAV file.
        """
        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            raise ValueError("Unable to open the video file!")

        # Get audio properties
        audio_fps = int(cap.get(cv2.CAP_PROP_FPS))
        audio_channels = int(cap.get(cv2.CAP_PROP_CHANNEL_COUNT))
        audio_width = int(cap.get(cv2.CAP_PROP_SAMPLE_WIDTH))
        audio_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        audio_output_file = os.path.join(self.output_dir, "audio.wav")

        with wave.open(audio_output_file, 'wb') as wf:
            wf.setnchannels(audio_channels)
            wf.setsampwidth(audio_width)
            wf.setframerate(audio_fps)

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                # Get the audio data from the frame
                audio_data = frame.tobytes()
                wf.writeframes(audio_data)

        cap.release()

            
            
     

if __name__ == "__main__":
    video_path = "001.mp4"
    output_dir = "results/"

    # Initialize the converter and split video into frames
    converter = VideoToFrames(video_path, output_dir)
    converter._extract_audio()
    converter.split_to_frames(processes=4)

