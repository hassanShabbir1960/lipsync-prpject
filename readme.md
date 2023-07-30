# Wav2Lip Synchronization Project

This project aims to improve the quality of videos synchronized with audio using the `wav2lip` method. It takes a pair of audio and video as input and returns a high-quality wav2lip synchronized video. Below is the complete pipeline:

Input Audio & Video 
    |
    v
Wav2Lip Synchronization
    |
    v
Low Quality Wav2Lip Video
    |
    |
    +---> Video Splitter ----------------------+
    |       (Converts video to image frames)   |
    |                                         |
    |   +---> Image Enhancer ------------------+---> Frame Combiner
    |   |       (Enhances each frame)          |       (Combines enhanced frames)
    |   |                                     | 
    +---> Audio Extractor --------------------+---> Final Video Combiner
            (Extracts audio from low quality video)   (Merges audio with high quality video)
    |
    v
Final High-Quality Wav2Lip Video




## Modules Description:

1. **Wav2Lip Synchronization:** 
   - **Input:** Audio & Video
   - **Output:** Low quality wav2lip synchronized video

2. **Video Splitter:** 
   - **Function:** Splits the low-quality video into individual frames.
   - **Input:** Low quality video
   - **Output:** Image frames

3. **Audio Extractor:** 
   - **Function:** Extracts audio from the low-quality wav2lip synchronized video.
   - **Input:** Low quality video
   - **Output:** Audio file

4. **Image Enhancer:** 
   - **Function:** Enhances the quality of each extracted frame.
   - **Input:** Image frames
   - **Output:** High-quality image frames

5. **Frame Combiner & Final Video Combiner:** 
   - **Function:** Combines the enhanced frames into a high-quality video and then merges the extracted audio with it.
   - **Input:** High-quality image frames, Audio
   - **Output:** High-quality wav2lip synchronized video



By following this pipeline, users can transform their input audio and video pairs into high-quality wav2lip synchronized videos.
![Alt text]('./flowchart.png')


