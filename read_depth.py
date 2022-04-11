from scipy.io import loadmat
import sys, os, cv2
import numpy as np
#(341*256)
l = os.listdir('./zip/RGB/RGB')
l.sort()
for i in l:
    ls = loadmat('./Depth/{}'.format(i.replace('_color.avi', '_depth.mat')))
    
    count = 1
    for j in range(len(ls['d_depth'][0][0])):
        image = np.array(ls['d_depth'])
        image = image.transpose(2, 0, 1)[j]
        if not os.path.exists('./depth/{}'.format(i.replace('_color.avi', '/'))):
            os.makedirs('./depth/{}'.format(i.replace('_color.avi', '/')))
        cv2.imwrite('./depth/{}'.format(i.replace('_color.avi', '/')+('{:0>5d}.jpg'.format(count))), image)
        count += 1
    
