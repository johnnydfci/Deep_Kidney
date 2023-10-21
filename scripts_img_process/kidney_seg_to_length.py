import os, glob, random
import SimpleITK as sitk
import numpy as np

from scipy.spatial import ConvexHull, distance


def get_lateral_length_from_mask(mskCube_lateral):
    
    coordinates = np.nonzero(mskCube_lateral)
    points = np.random.rand(len(coordinates[0]), 3) 
    for k in range(len(coordinates[0])):
        points[k] = [coordinates[2][k],coordinates[1][k],coordinates[0][k]]
    hull = ConvexHull(points)

    # Extract the points forming the hull
    hullpoints = points[hull.vertices,:]
    z_min =  np.min(hullpoints[:,2])

    hullpoints_resampled = np.copy(hullpoints)

    hullpoints_resampled[:,2] =(hullpoints[:,2]- z_min)*5 + z_min
    distances = distance.cdist(hullpoints_resampled, hullpoints_resampled, 'euclidean')

    maxarg = np.unravel_index(distances.argmax(), distances.shape)

#     print('Matrix indices of the two farthest points: %s' % (maxarg,))
    print(distances.max())

#     print('Farthest point #1 (coords): %s' % hullpoints[maxarg[0]])
#     print('Farthest point #2 (coords): %s' % hullpoints[maxarg[1]])
    
    return (distances.max(),hullpoints[maxarg[0]], hullpoints[maxarg[1]] )

def get_image_path_by_id(patient_id, image_dir):
    
    file_name = [os.path.relpath(os.path.join(image_dir, x)) \
                    for x in os.listdir(image_dir) \
                    if os.path.isfile(os.path.join(image_dir, x)) and patient_id in x]
    if len(file_name)>0:
        return file_name[0]
    else:
        return ''