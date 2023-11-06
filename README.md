# FacialAnalysis-IISc

# Facial Direction Analysis with OpenCV and Mediapipe

This Python script uses OpenCV and MediaPipe to estimate head pose in real-time from a webcam feed. It detects facial landmarks and calculates the head's rotation angles, which can be used to determine if the person is looking left, right, up, down, or straight.

## Table of Contents

1. Requirements
2. Installation
3. Usage
4. Output

### Requirements
To run this code, you need the following libraries and dependencies:

1. Python 3.x
2. OpenCV (cv2)
3. MediaPipe
4. NumPy
5. Pandas

- You can install the required Python libraries using pip and requirements.txt
```
pip install requirements.txt
```

### Installation
1. Clone this repository or download the script to your local machine.
```
git clone https://github.com/Manoj-2702/FacialAnalysis-IISc.git
```
2. Navigate to the project directory.
```
cd FacialAnalysis-IISc
```
3. Run the script
```
python main2.py
```


### Usage
- Execute the script as mentioned in the Installation section.

- A webcam feed will open, and the application will estimate the user's head pose in real-time.

- The script will display the direction in which the head is tilted, such as <b>looking left, right, up, down, or straight.</b>

- Press <b>'q'</b> to exit the application.


### Output
The script will display the webcam feed with head pose estimation, and it will print the following information to the console:

- The direction in which the user is looking.
- The rotation angles (X and Y) of the head.
- The percentages of time spent looking in each direction over the entire session.
