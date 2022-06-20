# AdaptiveTwoPassMedianFilter
In two-pass median filtering, an image contaminated by impulsive noise is processed by a median filter twice. Median filtering is a non-reversible process, i.e., useful information discarded by the filter cannot be recovered. This behavior becomes more apparent in two-pass median filtering. To correct this problem, between the two filtering processes we introduce an adaptive process to selectively replace some pixels by their original values based on the spatial distribution of estimated impulsive noise. Compared with standard median filtering and two-pass median filtering, better results are obtained in terms of visual appreciation and mean squared error.

Input: Salt and pepper noise 30%
--------------------
![noisyimg](https://user-images.githubusercontent.com/62876313/174640758-4552f93c-54a5-4b7c-8442-3c012034209c.png)


Output: 
--------------------
![twoPass](https://user-images.githubusercontent.com/62876313/174640765-2506917f-cb98-45c0-b1dc-ab2e7bed3a2b.PNG)

