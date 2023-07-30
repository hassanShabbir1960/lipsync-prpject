# Video Enhancer

The Video Enhancer folder contains utilities designed to enhance the quality of videos generated from Wav2Lip. Recognizing that the output from Wav2Lip might not always be of optimal quality, we have provided tools to ensure your videos are brought up to a higher standard.

---

## Workflow 🔄

1. **Audio Extraction & Frame Conversion**: Use `video_preprocessor.py` to extract audio from the source video and convert the video into individual frames.
   
2. **Image Enhancement**: With `Image_Enhancer.ipynb`, enhance each frame, converting them into high-definition (HD) quality.

3. **HD Video Generation**: Use `video_preprocessor.py` again to stitch the enhanced HD frames into a video. This utility also ensures the audio extracted earlier is combined with the new video, resulting in an HD video with proper lipsync.

---

## Usage 🚀

1. Start with the `video_preprocessor.py` script to process the initial video output from Wav2Lip.
   
2. Run the `Image_Enhancer.ipynb` notebook to upscale and improve the quality of individual frames.

3. Go back to the `video_preprocessor.py` script to combine the enhanced frames into a high-quality video and merge the audio.

---


