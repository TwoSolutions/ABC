# ABC - Audio Book Cutter

This Project is for extracting Chapters from a single file audio book.
This Parses the Chapter Length and Name directly from Googles Audiobook Page, you only have to get the ID of the Audiobook.
For example https://play.google.com/store/audiobooks/details?id=AQAAAEAc7BasGM has id AQAAAEAc7BasGM.
 
# Usage
Download FFmpeg from https://ffmpeg.org/.

Clone this repository with 

```
git clone https://github.com/TwoSolutions/ABC
cd ABC
pip install -r requirements.txt
```
Now open main.py and change your ID , Name , Author and File_Path. Then run main.py.
*Note* that the Name and Author variable in main.py can be set to *everything*, because currently the metadata for the chapter audio files is fetch from the input audio file, so they can be safely set to None.
