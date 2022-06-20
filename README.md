# AdaptiveTwoPassMedianFilter
In two-pass median filtering, an image contaminated by impulsive noise is processed by a median filter twice. Median filtering is a non-reversible process, i.e., useful information discarded by the filter cannot be recovered. This behavior becomes more apparent in two-pass median filtering. To correct this problem, between the two filtering processes we introduce an adaptive process to selectively replace some pixels by their original values based on the spatial distribution of estimated impulsive noise. Compared with standard median filtering and two-pass median filtering, better results are obtained in terms of visual appreciation and mean squared error.

Input:
--------------------
![noisyimg](https://user-images.githubusercontent.com/62876313/174634557-f74edbff-0338-4b83-9dd2-95e0855cad3d.png)


Output:
--------------------
![twoPass](https://user-images.githubusercontent.com/62876313/174634907-a8868b40-be82-47e2-9483-a4bb0f63de3e.PNG)
