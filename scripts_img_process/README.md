
Scripts under the folder 'src_liverseg/scripts_test/' are used to test the model only. 

*image_load_test.py*
    
    Load the images and labels (if available) under the data folder for model test.
    
*image_postprocessing_test.py*
    
    There could be some small isolaoted voxels in the model segmentation.
    
    The largest connected component in the model segmentation was retained by the connected components analysis. 
    
*image_preprocessing_test.py*
    
    Particular transforms for the model test. Not for NIFTI image curations.
    
*model_test.py*
    
    Main function for model test adopted from MONAI 0.4.0. 
    
*sitk_nifti_tools.py*
    
    The output of the MONAI model is the 3D numpy array/ tensor. This script is used to save the segmentation array in NIFTI format.
    
*test_liver_density_volume.py*
    
    Get the deep learning performances for volumetric segmentation and liver fat mesasurements
