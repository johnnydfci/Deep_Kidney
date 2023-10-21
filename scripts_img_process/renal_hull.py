import cv2 
import numpy as np
import SimpleITK as sitk

def save_hull_of_parenchyma_into_nii(nii_input_path, nii_output_path): 
   
    seg_sitk = sitk.ReadImage(nii_input_path)
    seg_array_3d  = sitk.GetArrayFromImage(seg_sitk)
    shape_x,shape_y,shape_z = seg_array_3d.shape  
    
    seg_array_lk = np.copy(seg_array_3d)
    seg_array_lk[seg_array_lk ==1 ] = 0  # left kidney is left , as left kidney is class 2
    seg_array_lk[seg_array_lk > 0] = 1
    seg_array_left_total_kidney = get_convex_hull_of_kidney_3d(seg_array_lk)   
  
    seg_array_rk = np.copy(seg_array_3d)
    seg_array_rk[seg_array_rk == 2  ] = 0 # right kidney is left, as right kidney is class 1
    seg_array_right_total_kidney = get_convex_hull_of_kidney_3d(seg_array_rk)   
    
    seg_array_total_kidney =  seg_array_left_total_kidney *2  +  seg_array_right_total_kidney 

#     seg_array_3d = 2 * seg_array_3d - seg_panrenchyma    
    
    sitk_image_object = seg_sitk
    output_spacing = sitk_image_object.GetSpacing()
    output_direction = sitk_image_object.GetDirection()
    output_origin = sitk_image_object.GetOrigin()
#     print(output_spacing ,output_direction,output_origin)

    nrrd_output = sitk.GetImageFromArray(seg_array_total_kidney)
    nrrd_output.SetSpacing(output_spacing)
    nrrd_output.SetDirection(output_direction)
    nrrd_output.SetOrigin(output_origin)

    nrrdWriter = sitk.ImageFileWriter()
    nrrdWriter.SetFileName(nii_output_path )
    nrrdWriter.SetUseCompression(True)
    nrrdWriter.Execute(nrrd_output)
    print(nii_output_path ,'saved')
    
def get_convex_hull_of_kidney_3d(seg_array):
    
    empty_mask_3d = np.copy(seg_array)
    first_slice = 0
    last_slice = seg_array.shape[0]-1
    for k in range(seg_array.shape[0]):
        if ( np.sum(seg_array[k,:,:])==0) and (np.sum(seg_array[k+1,:,:])>0):
            first_slice = k+1 
            break
    for k in range(first_slice, seg_array.shape[0]):            
        if ( np.sum(seg_array[k,:,:])==0) and (np.sum(seg_array[k-1,:,:])>0):
            last_slice = k-1
            break 
    
    for z_idx in range(first_slice+1, last_slice-1):
#         print('z_idx processing', z_idx)
        
        mid_z = int(seg_array.shape[-1]/2)
        left_kidney = np.copy(seg_array[z_idx, :, :])
        left_kidney[: , mid_z: ]=0
        right_kidney = np.copy(seg_array[z_idx, :, :])
        right_kidney[:, :mid_z]=0        

        left_hull_mask = get_convex_hull_of_kidney_2d(left_kidney)
        right_hull_mask = get_convex_hull_of_kidney_2d(right_kidney)        
        empty_mask_3d[z_idx, :, :] = left_hull_mask + right_hull_mask 

    return empty_mask_3d

def get_convex_hull_of_kidney_2d(unilateral_kidney_array):
    seg_slice = unilateral_kidney_array.astype("uint8")
    hull_mask = np.zeros(seg_slice.shape)
    _, thresh = cv2.threshold(seg_slice, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    contours, hierarchy = cv2.findContours(thresh, 3, 2)
    
    if len(contours) ==0:
        return hull_mask
    
    cnt = contours[0]
    hull = cv2.convexHull(cnt)    
    for j in range(np.min(hull[:,:]-1), np.max(hull[:,:]+1)):
        for k in range(np.min(hull[:,:]-1), np.max(hull[:,:]+1)):
            dist = cv2.pointPolygonTest(hull, (k, j), False)
            if dist >=0:
                hull_mask[j,k]=1
          
    return hull_mask