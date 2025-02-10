## CS5670 PROJECT 1: HYBRID IMAGES

This directory contains the code for CS5670 Hybrid Images project. The code is provided in the hybrid.py script. The code was tested using the sample RGB images provided and using user selected Black and White images.
The images used for black and white hybrid testing are as follows

<p float="left">
  <img src="https://github.com/sharmasiddhartha231/CS5670_Project_1_Artifact/blob/main/Artifact/left.jpg" width="400" title="Left Image" />
  <img src="https://github.com/sharmasiddhartha231/CS5670_Project_1_Artifact/blob/main/Artifact/right.jpg" width="400" title = "Right Image"/> 
</p>

For hybrid image testing, 4 different sets of hyper parameters were used. All parameter files are provided as jsons alongside the resulting image based on each parameter. There are 8 resulting hybrid images and parameter files. This is due to testing 4 sets of parameters and using high and low pass alternatively on both images. For all testing purposes, the image order does not change.

| Image Set     | Left Sigma    | Left Kernel Size | Right Sigma   | Right Kernel Size | Left Image Pass | Right Image Pass |  
| ------------- | ------------- | ---------------- | ------------- | ----------------- | --------------- | ---------------- |
| Set 1 | 4.1  | 8 | 7.0 | 13 | Low | High |
| Set 2 | 4.1  | 8 | 7.0 | 13 | High | Low |
| Set 3 | 7.0  | 13 | 4.1 | 8 | Low | High |
| Set 4 | 7.0  | 13 | 4.1 | 8 | High | Low |
| Set 5 | 5.0  | 10 | 5.0 | 10 | Low | High |
| Set 6 | 5.0  | 10 | 5.0 | 10 | High | Low |
| Set 7 | 10.0  | 25 | 10.0 | 25 | Low | High |
| Set 8 | 10.0  | 25 | 10.0 | 25 | High | Low |

Images for Set 1 and 2
<p float="left">
  <img src="https://github.com/sharmasiddhartha231/CS5670_Project_1_Artifact/blob/main/Artifact/Hybrid_1.jpg" width="400" title="Hybrid Image 1" />
  <img src="https://github.com/sharmasiddhartha231/CS5670_Project_1_Artifact/blob/main/Artifact/hybrid_2.jpg" width="400" title = "Hybrid Image 2"/> 
</p>

Images for Set 3 and 4
<p float="left">
  <img src="https://github.com/sharmasiddhartha231/CS5670_Project_1_Artifact/blob/main/Artifact/hybrid_3.jpg" width="400" title="Hybrid Image 3" />
  <img src="https://github.com/sharmasiddhartha231/CS5670_Project_1_Artifact/blob/main/Artifact/hybrid_4.jpg" width="400" title = "Hybrid Image 4"/> 
</p>

Images for Set 5 and 6
<p float="left">
  <img src="https://github.com/sharmasiddhartha231/CS5670_Project_1_Artifact/blob/main/Artifact/hybrid_5.jpg" width="400" title="Hybrid Image 5" />
  <img src="https://github.com/sharmasiddhartha231/CS5670_Project_1_Artifact/blob/main/Artifact/hybrid_6.jpg" width="400" title = "Hybrid Image 6"/> 
</p>

Images for Set 7 and 8
<p float="left">
  <img src="https://github.com/sharmasiddhartha231/CS5670_Project_1_Artifact/blob/main/Artifact/hybrid_7.jpg" width="400" title="Hybrid Image 7" />
  <img src="https://github.com/sharmasiddhartha231/CS5670_Project_1_Artifact/blob/main/Artifact/hybrid_8.jpg" width="400" title = "Hybrid Image 8"/> 
</p>
