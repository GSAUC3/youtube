Have you ever wondered what would happen if you try to fit a line through this dataset????




Hey Py Lamas, welcome back! In this video, we're shifting gears to explore the RANSAC algorithm – a robust solution to outliers. Ready to unravel its mysteries? Let's dive right in.

So What's RANSAC? Well, RANSAC stanads for random sample consensus, and it's like the super hero of algorithms, when it comes to handling outliers. imagine trying to fit a line through a set of points, but some of those points are noisy outliers. So how do you get the perfect line? 

Linear regression?
UMMM... Not really!! because traditional regression considers every point and you end up with a poorly fitted line. 
so the solution? 
Of course RANSAC. so let's see how it works step by step

Imagine you are given a dataset of 100 points, of which 30% are outliers.
the steps are as follows: 
so in the first iteration, 
    randomly select k points, and fit a line using those k points only, in our case let k = 10
    in the next step, you have to calculate the distance between each and every point present in the dataset, to the fitted line
    followed by keeping a track of the number of inliers and the array of inliers itself
    
    now what are inliers, you might ask? 
    those points which lie within a distance, delta on either side of the fitted line will be classified as inliers, and the rest will be  outliers. 
