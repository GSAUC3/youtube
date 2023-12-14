from manimlib import * 
import numpy as np

            
class PlotPoints(Scene):
    def construct(self):
        # Your array of 2D points

        num_inliers = 20
        inlier_slope = 2
        inlier_intercept = 5
        inlier_noise = 0.5
        inliers_x = np.random.uniform(-10, 10, num_inliers)
        inliers_y = inlier_slope * inliers_x + inlier_intercept + np.random.normal(0, inlier_noise, num_inliers)

        # Generate outlier data points
        num_outliers = 10
        outlier_x = np.random.uniform(-10, 10, num_outliers)
        outlier_y = np.random.uniform(-10, 20, num_outliers)

        # Combine inliers and outliers
        x_data = np.concatenate((inliers_x, outlier_x))
        y_data = np.concatenate((inliers_y, outlier_y))
        zeros = np.zeros(len(x_data))
        points_data = np.c_[x_data,y_data,zeros]
        points_data/=(np.max(points_data)/5)
        # points_data = [(1, 2.0, 0), (2, 3.5, 0), (3, 1.5, 0), (4, 4, 0)] # points are 
        # always written in 3d fashion in manim
        # print(points_data)
        # how to add axis 
        # axes = Axes((-1.5, 1.5), (-1.5, 1.5)) this is how you set axes limits
        axes = Axes()
        self.add(axes)
        # Create dots at each point
        # dots = VGroup(*[Dot(point) for point in points_data])
        dots = VGroup(*[Dot(np.array(point)) for point in points_data])

        # Display the dots
        self.play(ShowCreation(dots))
        self.wait(2)

        inlier_dots = [Flash(dot, color=GREEN) for dot in dots[:num_inliers]]
        self.play(*inlier_dots)

        self.wait(2)
        
        outlier_dots = [Flash(dot, color=RED) for dot in dots[num_inliers:]]
        self.play(*outlier_dots)
      
      
        indices_to_turn_red = np.random.choice(len(dots), 5, replace=False)
        print(points_data[indices_to_turn_red])  
        for index in indices_to_turn_red:
            dots[index].set_color(RED)
        # ============ THIS IS HOW YOU CREATE A ROTATED RECTANGLE ANIMATION ==============
        # rect = Polygon(*[axes.c2p(*i)
        #                  for i in self.get_rectangle_corners( (PI/2,0),(-PI/2,-1))
        #                 ], 
        #                color=RED)
        
        # self.play(ShowCreation(rect))
        # self.wait(1)
        # self.play(Rotate(rect, angle=PI/3, about_point=rect.get_center()))
        # self.play(rect.animate.shift(UP))
        # ============ THIS IS HOW YOU CREATE A ROTATED RECTANGLE ANIMATION ==============
        

    def get_rectangle_corners(self,  top_right,bottom_left):
        return [
            (top_right[0], top_right[1]),
            (bottom_left[0], top_right[1]),
            (bottom_left[0], bottom_left[1]),
            (top_right[0], bottom_left[1]),
        ]
    

