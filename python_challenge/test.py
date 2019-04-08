import gameoflife as GOF
import numpy as np

pattern = np.array([[0,0,0,0,0,0],
                        [0,0,0,0,0,0],
                        [0,0,1,1,1,0],
                        [0,1,1,1,0,0],
                        [0,0,0,0,0,0],
                        [0,0,0,0,0,0]])

for snap in GOF.next(4, pattern):
    print(snap)