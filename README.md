# Automated segmentation for measuring kidney volume and length in CT images: A cross-national evaluation study

Welcome to our GitHub repository for the DL-Kidney system: a nnunet for kidney segmentation, the script to measure volume and lengths using DL auto-segmentation, as well as the dataset used for development and test. [Method details.md](documentation/Method_introduction.md)

### Implementation steps

1. nnU-Net for parenchymal kidney segmentation: [nnU-Net Implementation.md](documentation/Implementation_steps.md)

2. A gift-wrapping algorithm to get total kidney segmentation from parenchymal auto-segmentation [DL_seg_to_select_parenchyma.ipynb](DL_seg_to_select_parenchyma.ipynb)

2. use auto-segmentation to calculate voxel-count volume and pole-to-pole lengths: [DL_seg_to_select_parenchyma.ipynb](DL_seg_to_select_parenchyma.ipynb)

4. plot figures of all results: ```dir: stats_to_figure/ ```

Our deep learning system was developed and externally validated on a total of 1,153 CT images from cross-national databases. All CT images were reformatted to the NIfTI format and resampled to a consistent voxel spacing of 1.0 x 1.0 x 5.0 mm/pixel. Curated CT images and kidney segmentations can be freely downloaded by Google Drive tbd or Baidu Wangpan tbd.  Right kidney: class 1; left kidney: class 2.

## Publication

Peer-reviewed article: to be updated

## License

Apache License, Version 2.0
