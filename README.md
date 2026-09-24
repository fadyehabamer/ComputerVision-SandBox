<p align='center'>
<img src='repoAssets/logo.png'>
</p>
<h1 align="center" > Computer Vision Course </h1>
<h3 align="center">
Lecture Notes & Python Code for Computer Vision Course @ Faculty of computer and information Sciences ' MU ' for the '4th Year'
</h3>

## Contents

| Folder | What's inside |
| --- | --- |
| `LECTURES/` | Lecture notes (PDF) and MCQ sheets |
| `FINAL SEC REVISION/` | Revision PDFs for the lab sections |
| `SECTIONS/BASICS/` | Python refresher: variables, strings, lists, dicts, classes, files, JSON, modules, map/filter/reduce |
| `SECTIONS/SECTION 1` | NumPy basics; reading/writing images and video with OpenCV |
| `SECTIONS/SECTION 2` | Colour spaces, thresholding, resizing, blurring, filters, Sobel/Laplacian/Canny edges |
| `SECTIONS/SECTION 3` | Contours and Hough line detection |
| `SECTIONS/SECTION 4` | Drawing: lines, rectangles, circles, ellipses, text |
| `SECTIONS/SECTION 5` | Shi-Tomasi corner detection (`goodFeaturesToTrack`) |
| `SECTIONS/SECTION 6` | FAST keypoints |
| `SECTIONS/SECTION 7` | ORB, BRIEF and SIFT features |
| `SECTIONS/SECTION 8` | Lucas-Kanade optical flow on `SECTIONS/video.mp4` |
| `SECTIONS/SECTION 9` | Stereo disparity (StereoSGBM) from `1.jpg` / `2.jpg` |

Many section files keep earlier examples commented out. Uncomment the block you want to try.

## Run the code

Requires Python 3.8+.

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python "SECTIONS/SECTION 5/main.py"
python "SECTIONS/SECTION 8/optical flow.py"   # press Esc to stop
```

The scripts open OpenCV windows (`cv2.imshow`), so run them on a machine with a display. Press any key to close an image window. Each script switches to its own folder on start, so the sample files (`SECTIONS/logo.png`, `video.mp4`, `earth.avi`, `SECTION 9/1.jpg`, `2.jpg`) are found whatever directory you run it from.

`requirements.txt` installs `opencv-contrib-python`, because `SECTION 7/BRIEF.py` needs the `cv2.xfeatures2d` contrib module.
