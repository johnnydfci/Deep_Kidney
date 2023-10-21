from skimage import measure
import numpy as np
import cv2
import SimpleITK as sitk
import os

def curate_2_class_array(kidney_mask_array): 
    
    shape_x,shape_y,shape_z = kidney_mask_array.shape 
    
    mask_array_1 = np.copy(kidney_mask_array)
    mask_array_2 = np.copy(mask_array_1)
    
    mask_array_1[mask_array_1!=1]=0 
    mask_array_2[mask_array_2!=2]=0
    mask_array_2[mask_array_2==2]=1
    
    print('np.sum(mask_array_1)',np.sum(mask_array_1))
    print('np.sum(mask_array_2)',np.sum(mask_array_2))
    
    tb_return_array = kidney_mask_array * 0    
    mask_array_1 = get_biggst_mask_array(mask_array_1)
    mask_array_2 = get_biggst_mask_array(mask_array_2)   
    
    tb_return_array = mask_array_1  + mask_array_2 *2

    return (tb_return_array)
    

def get_biggst_mask_array(mask_array):
    
    all_labels, noduleCount = measure.label(mask_array, connectivity=2, return_num=True)
    props = measure.regionprops(all_labels)
    areas = []
    for iii in range(len(props)):
        areas.append(props[iii].area)
    areas = sorted(areas, reverse=True)
    #     print( 'nodulecount:------------'+str(noduleCount), '[:10]:', areas[:10])
    #
    copyMaskData = mask_array
    # get blobs
    all_labels = measure.label(copyMaskData)

    # get number of blobs ( inlcuding background as zero
    noduleCount = all_labels.max()
    voxel_all_num = all_labels.sum()
    threshold = voxel_all_num * 0.03

    # list to populate
    maskDataList = []
    maskDataListVolume = []
    biggest_mask_array = mask_array
    # supress one mask and leave the others
    # 0 is the background - so dont deal with it
    for label in range(1, noduleCount + 1):

        # make an array of zeros
        tempMaskData = np.zeros((copyMaskData.shape[0], copyMaskData.shape[1], copyMaskData.shape[2]), dtype=np.int64)
        #
        arrays = np.where(all_labels == label)
        # just loop through lenght of one of the 3 arrays - they are all the same
        for k in range(len(arrays[0])):
            tempMaskData[arrays[0][k]][arrays[1][k]][arrays[2][k]] = 1.0

        # when array done

        volume_num = tempMaskData.sum()

        if volume_num > threshold:
            biggest_mask_array = tempMaskData
            threshold = volume_num
    return biggest_mask_array
