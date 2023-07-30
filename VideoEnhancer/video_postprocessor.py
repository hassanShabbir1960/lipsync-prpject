import os
import moviepy
import moviepy.editor as mp
import moviepy.video.io.ImageSequenceClip

class VideoMaker:
    def __init__(self, image_dir, output_path, fps=30):
        self.image_dir = image_dir
        self.output_path = output_path
        self.fps = fps

    def images_to_video(self):
        """
        Convert a directory of images into a video.
        """
        # List all files in the directory and sort them
        image_files = sorted(
            [os.path.join(self.image_dir, img) for img in os.listdir(self.image_dir) if img.endswith(('.png', '.jpg', '.jpeg'))]
        )

        # Use moviepy to convert images into a video clip
        clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=self.fps)
        
        # Write the clip to a video file
        clip.write_videofile(self.output_path)

    def combine_with_audio(self, audio_path, final_output_path):
        """
        Combine the generated video with an audio file.

        Args:
        - audio_path (str): Path to the audio file.
        - final_output_path (str): Path where the combined video should be saved.
        """
        video = mp.VideoFileClip(self.output_path)
        audio = mp.AudioFileClip(audio_path)
        final_clip = video.set_audio(audio)
        final_clip.write_videofile(final_output_path)

if __name__ == "__main__":
    image_directory = "enhancedframes/"
    output_video_path = "resultant_without_audio.mp4"
    audio_path = "audio.wav"
    final_output_path = "resultant_with_audio.mp4"
    
    maker = VideoMaker(image_directory, output_video_path)
    maker.images_to_video()
    maker.combine_with_audio(audio_path, final_output_path)
