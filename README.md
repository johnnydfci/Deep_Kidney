# Automated segmentation for measuring kidney volume and length in CT images: A cross-national evaluation study

Welcome to our GitHub repository for the DL-Kidney system: a nnunet for kidney segmentation, the script to measure volume and lengths using DL auto-segmentation, as well as the dataset used for development and test.

### Implementation steps

1. nnU-Net for parenchymal kidney segmentation: [nnU-Net Implementation.md](documentation/Implementation_steps.md)

2. Post-precssing scripts to withhold top1 mask from each class of parenchymal [nnunet_seg_postprocess.ipynb](nnunet_seg_postprocess.ipynb)

3. Get voxel-count volume from parenchymal kidney segmentation: [kidney_parenchymal_seg_to_vol.ipynb](kidney_parenchymal_seg_to_vol.ipynb)

4. A gift-wrapping algorithm to get total kidney segmentation from parenchymal segmentation [seg_gift_wrapping.ipynb](seg_gift_wrapping.ipynb)

5. Get voxel-count volume and pole-to-pole lengths from total kidney segmentation: [kidney_total_seg_to_vol_and_len.ipynb](kidney_seg_to_vol_and_len.ipynb)

6. plot figures of all results: ```dir: stats_to_figure/ ```

Our deep learning system was developed and externally validated on a total of 1,153 CT images from cross-national databases. All CT images were reformatted to the NIfTI format and resampled to a consistent voxel spacing of 1.0 x 1.0 x 5.0 mm/pixel. Well-trained model can be downloaded here: https://drive.google.com/file/d/1No6qpviwyO-WyRBqjFdm8sQjlrUIiY2E/view?usp=sharing

Right kidney: class 1; left kidney: class 2.

## Publication

Peer-reviewed article: to be updated

## License

Apache License, Version 2.0
