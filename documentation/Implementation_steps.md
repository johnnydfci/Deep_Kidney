# Deep learning model for kidney segmentation

A nnU-Net deep learning model is developed using this repository https://github.com/MIC-DKFZ/nnUNet. The nnU-Net was implemented and tested on Linux (Ubuntu 18.04) with an RTX 3060 GPU (12GB VRAM). 

### Environment setup

```conda create -n kidu python=3.8.5``` # create a conda environment with python3.8.5; ```conda remove -n kidu --all ```if you want to delete this conda environment. 

'kidu' stands for both contrast-enhanced and non-enhanced kidney images.

```conda activate kidu ```  # activate the conda environment

```conda install nb_conda_kernels```  # Install jupyter notebook

```pip3 install -r requirements.txt``` # Once you change directories into the root path of the project

 ```pip3 install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113```# install pytorch under CUDA 11.3
 
 ```pip3 install nnunet==1.7.1```# install nnunet==1.7.1
 
 ### nnunet paths setup 
 
 - Use commandline to set up the environment path for nnunet, suppose your repo dir is '/home/zhongyi/Desktop/kidney_1202/nnUNet_kidney'
 -  
                ```                      
                export nnUNet_raw_data_base="/home/zhongyi/Desktop/nn-unet_train/nnUNet_raw_data_base"
                export nnUNet_preprocessed="/home/zhongyi/Desktop/nn-unet_train/nnUNet_preprocessed"
                export RESULTS_FOLDER="/home/zhongyi/Desktop/nn-unet_train/nnUNet_trained_models"                ```                
 
 ### Files preparation for nnunet test
 
 ```nnUNet_raw_data_base/nnUNet_test_data/test_img_in_nii_raw/ ``` # download open-source data into the dir, one image is stored in our repository as an example
 
 ```nnUNet_raw_data_base/file_op_to_infer_by_nnunet.ipynb```  # prepare data into the required file name, where each nifty image name has to end with '0000.nii.gz'
 
  ```nnUNet_trained_models/ ``` # download pre-trained model from Gdrive or baiduwangpan.  This model has 421 training and 105 tuning images. The required model path is shown in this [screenshot.png](Pre_trained_model_paths.png) The model is stored here: https://drive.google.com/file/d/1No6qpviwyO-WyRBqjFdm8sQjlrUIiY2E/view?usp=sharing
  
 ### nnunet scripts to test kidney segmentation in input CTs
 
 ```python nnunet/inference/predict_simple.py  -i $nnUNet_raw_data_base/nnUNet_test_data/test_img_in_nii/ -o  $nnUNet_raw_data_base/nnUNet_test_data/test_seg_in_nii_raw/ -t 666 -m 3d_fullres -f 1 -tr nnUNetTrainerV2_noMirroring``` # run this command line in the repo dir. -i: input images dir; -o: inference segmentation dir; -t task id; -tr trainer of nnunet



### Test performance evaluation

```nnUNet_raw_data_base/nnunet_seg_various_accuracy_compute.ipynb``` # compute segmentation performances, i.e., dsc, jc, hd


### -optional: training a brand-new model for kidney segmentation

-  ```  nnUNet_raw_data_base/nnUNet_train_data_raw/ ``` # download training data into the dir. 1 CT images can be a toy example, which can be downloaded from Gdrive or baiduwangpan ```Files_for_running_github/nnUNet_train_data_raw.zip``` dir. Required paths are shown in this [screenshot.png](Images_paths_for_training.png)

-  ``` nnUNet_raw_data_base/file_op_to_prepare_training_nnunet.ipynb```  #  prepare data into the required format of nnunet: 1/2 step

-   ```python nnunet/dataset_conversion/666_dual_kidney.py```   #   prepare data into the required format of nnunet 2/2 step

-   ```python  nnunet/experiment_planning/nnUNet_plan_and_preprocess.py -t 666 --verify_dataset_integrity```    # pre-process the data using nnunet scripts
             
-   ```nnUNet_train 3d_fullres nnUNetTrainerV2_noMirroring 666  1```  # command for training a nnunet model, the '1' stands for training 1st fold of the five-fold cross validation, 'nnUNetTrainerV2_noMirroring' means that mirroring is excluded from data augmentation.
