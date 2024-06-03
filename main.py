import numpy as np
from skimage import data
import napari
import SimpleITK as sitk

# print(data.cells3d().shape)
# data = np.random.rand(60, 2, 256, 256)
data = sitk.GetArrayFromImage(sitk.ReadImage('0001.nii.gz'))
data = data[:,np.newaxis,:,:]

viewer = napari.view_image(data, channel_axis=1, ndisplay=3, opacity=0.8, title="HAHA", iso_threshold=0.5)
napari.run()