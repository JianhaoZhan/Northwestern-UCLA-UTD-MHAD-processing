from scipy.io import loadmat
import sys, os, cv2
import numpy as np
#(341*256)
l = os.listdir('./zip/RGB/RGB')
l.sort()
for i in l:
    ls = loadmat('./Skeleton/{}'.format(i.replace('_color.avi', '_skeleton.mat')))
    vs = [(1,2), (2,3), (3,4), (5,2), (5,6), (6,7), (7,8), (9,2), (9,10), (10,11), (11,12), (4,13), (13,14), (14,15), (15,16), (4,17), (17,18), (18,19), (19,20)]
    
    count = 1
    for j in range(len(ls['d_skel'][0][0])):
        res = []
        image = np.zeros((256, 341, 3),  np.uint8)
        for k in range(20):
            
            try:
                x, y = (ls['d_skel'][k][0][j]+0.8)/1.6*341, (ls['d_skel'][k][1][j]+1.2)/2.2*256
                res.append((x, y))
            except:
                res.append((float('inf'), float('inf')))
        
        for j in vs:
            x1, y1 = res[j[0]-1]
            x2, y2 = res[j[1]-1]
            if x1 < 1e5 and x2 < 1e5 and y1 < 1e5 and y2 < 1e5:
                cv2.line(image,(int(x1),int(y1)),(int(x2),int(y2)),(0,0,255),1)
        for j in range(20):
            if res[j][0] < 1e5 and res[j][1] < 1e5:
                cv2.circle(image, (int(res[j][0]), int(res[j][1])), 1, (0, 255, 0), thickness=-1)
        image = cv2.flip(image, 0) 
        if not os.path.exists('./skeleton/{}'.format(i.replace('_color.avi', '/'))):
            os.makedirs('./skeleton/{}'.format(i.replace('_color.avi', '/')))
        cv2.imwrite('./skeleton/{}'.format(i.replace('_color.avi', '/')+('{:0>5d}.jpg'.format(count))), image)
        count += 1
    
