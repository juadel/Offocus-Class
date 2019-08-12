**INTRODUCTION**

Within time, cameras can become out of focus due to a different reasons. This program allows user to scan for IP cameras (over an IP range) and determine the shoot image state, what could be “CLEAR” or “BLURRY”. It also provides an alternative method to check images located in a folder.

The user have the possibility to  decide if he wants to see the image or just read a final report.

In this repository (as part of my learning process) I am including the program using classes. 

**HOW IT WORKS**

After a long research,  I decide to work with 3 features obtained from images, Laplacian, Gaussian and Scharr.

* Laplacian : The Laplacian is a 2-D measure of the 2nd spatial derivative of an image. The Laplacian of an image highlights regions of rapid intensity change and is therefore often used for edge detection . A well focus images is expected to have well defined edges. To obtain a Laplacian value, a skimage.filter Laplace is used. 
https://scikit-image.org/docs/dev/api/skimage.filters.html#skimage.filters.laplace and then the variance is calculated.
Also, during the process, the maximum value of Laplacian is calculated in order to have more features to compare.


* Gaussian-Noise Standard Desviation: Principal sources of Gaussian noise in digital images arise during acquisition e.g. sensor noise caused by poor illumination and/or high temperature, and/or transmission e.g. electronic circuit noise. In digital image processing Gaussian noise can be reduced using a spatial filter, though when smoothing an image, an undesirable outcome may result in the blurring of fine-scaled image edges and details because they also correspond to blocked high frequencies. 
To calculate the noise, the skimage.restoration estimate_sigma is used  
https://scikit-image.org/docs/dev/api/skimage.restoration.html#skimage.restoration.estimate_sigma


* Scharr Filter :  This is a filtering method used to identify and highlight gradient edges/features using the 1st derivative. Typically used to identify gradients along the x-axis (dx = 1, dy = 0) and y-axis (dx = 0, dy = 1) independently. Performance is quite similar to Sobel filter. Used to detect edges / changes in pixel intensity. Base on the same principle of clear images must have well defined edges, this filter was choose to have additional features to compare.
To calculate the Sharr of the image, Skimage.filters Scharr function was used, and then the variance was obtained.
https://scikit-image.org/docs/dev/api/skimage.filters.html#skimage.filters.scharr



With this features a Supervise learning model was created using 6000 images (half blurry, half clear). The process of this model creation is in the jupyter notebook file offocus_model.ipynb

**SERVER API**

A AWS instance is running a Gunicorn server with the model, a client can request a prediction using a JSON format


**NEXT STEPS:**
1. windows version in C#
2. Include more range of Cameras brands (now only works on 3xlogic-HIK)
3. Error management.
4. increase model accuracy.
5. Model using reinforcement learning
