'''
Colorsphere shown on points in 3D.
'''

import colorsphere
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d 


vectors = np.random.standard_normal(size=(1000,3))
coloring = colorsphere.Ico() 
colors = coloring(vectors)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(vectors[:,0], vectors[:,1], vectors[:,2], color=colors)


#%%
'''
Using z_direction to orient colorsphere.
'''

z_dirs = [[0, 0.1, 0.9], [0.5, 0.5, 0], [0.3, 0.4, 0.5]]

colorings = [colorsphere.Duo(z_direction = z_dir) for z_dir in z_dirs]  

s = 7.5

fig = plt.figure()

for i in range(3):
    
    ax = fig.add_subplot(1, 3, i+1, projection='3d')                      
    colors = colorings[i](vectors)
    ax.scatter(vectors[:,0], vectors[:,1], vectors[:,2], color=colors)
    
    ax.plot([-s*z_dirs[i][0], s*z_dirs[i][0]], 
            [-s*z_dirs[i][1], s*z_dirs[i][1]], 
            [-s*z_dirs[i][2], s*z_dirs[i][2]], 
            'k', linewidth=2)
    
#%%
'''
Using ordering to permute axis.
'''

ords = [[2, 0, 1], [0, 2, 1], [1, 0, 2]] 
colorings = [colorsphere.Uno(ordering = o) for o in ords]  

fig = plt.figure()

for i in range(3):
    
    ax = fig.add_subplot(1, 3, i+1, projection='3d')                      
    colors = colorings[i](vectors)
    ax.scatter(vectors[:,0], vectors[:,1], vectors[:,2], color=colors)
    


#%%
'''
Colorsphere shown on icosphere.
''' 

from icosphere import icosphere

nu = 15
vertices, faces = icosphere(nu)
face_vectors = vertices[faces].sum(axis=1)
face_vectors /= np.sqrt((face_vectors**2).sum(axis=1, keepdims=True))


fig = plt.figure()


colorings = [colorsphere.Uno(), 
             colorsphere.Duo(),
             colorsphere.Tre(),
             colorsphere.Ico()]

names = ['Uno', 'Duo', 'Tre', 'Ico']

for i in range(4):
    
    ax = fig.add_subplot(2, 2, i+1, projection='3d')                  
    
    face_colors = colorings[i](face_vectors)
    
    poly = mpl_toolkits.mplot3d.art3d.Poly3DCollection(vertices[faces])
    poly.set_facecolor(face_colors) 
    poly.set_edgecolor(None)
    poly.set_linewidth(0.25)
    
    ax.add_collection3d(poly)
        
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.set_zlim(-1,1)
    
    ax.azim = 40
    ax.dist = 10
    ax.elev = 35
    
    ax.set_xticks([-1,0,1])
    ax.set_yticks([-1,0,1])
    ax.set_zticks([-1,0,1])
    
    ax.set_title(names[i], x=0.1, y =0.9)
    
plt.show()



