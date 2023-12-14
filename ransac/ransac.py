from typing import *
import numpy as np 
from sklearn.linear_model import LinearRegression





_type_slope = NewType('slope',float)
_type_intercept = NewType('intercept',float)



class Ransac:
    def __init__(self,
                 data,
                 *,
                 min_sample=10,
                 max_iter=100,
                 residual_threshold=0.5) -> None:
        self._n = max_iter
        self._x = data[:,0]
        self._y = data[:,1]
        self.min_sample = min_sample
        self.thresh = residual_threshold
        self.__data = data 
        self.__max_inliers = 0

    def _compute_num_inliers(self,
                             m:_type_slope,
                             c:_type_intercept
                             )->Tuple[int,np.ndarray]:

        distances = np.abs((m* self._x - self._y+c)/ np.sqrt(1+m**2))
        idx = np.where(distances<=self.thresh)
        return self.__data[idx]

    def _fit_line(self,x,
                  y)->Tuple[_type_slope,_type_intercept]:
        model = LinearRegression()
        model.fit(x.reshape(-1,1),y)
        return model.coef_[0],model.intercept_
    
    def fit(self,*args):
        best_inliers = None 

        for _ in range(self._n):
                
            random_sample_data = self.__data[np.random.choice(len(self.__data),self.min_sample,replace=False)]
            # ax.scatter(random_sample_data[:,0],random_sample_data[:,1],color='r')
            m,c = self._fit_line(random_sample_data[:,0],random_sample_data[:,1])
            f = lambda x: x*m+c
            # ax.plot([min(self._x),max(self._x)],[f(min(self._x)),f(max(self._x))],c='g')
            _inliers = self._compute_num_inliers(m,c)
            _num_inliers = len(_inliers)
            # ax.scatter(_inliers[:,0],_inliers[:,1],c='y')
            if _num_inliers>self.__max_inliers:
                self.__max_inliers = _num_inliers
                best_inliers = _inliers
        
        return best_inliers