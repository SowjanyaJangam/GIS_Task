#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import required libraries
import rasterio
from rasterio import plot
import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline
#import bands as separate 1 band raster
band4 = rasterio.open('C:/Users/sowjanya jangam/Desktop/Seaweed/Atmoscorrection/LC08_L1TP_148046_20230115_20230130_02_T1_B4_REF.TIF') #red
band5 = rasterio.open('C:/Users/sowjanya jangam/Desktop/Seaweed/Atmoscorrection/LC08_L1TP_148046_20230115_20230130_02_T1_B5_REF.TIF') #nir
band6 = rasterio.open('C:/Users/sowjanya jangam/Desktop/Seaweed/Atmoscorrection/LC08_L1TP_148046_20230115_20230130_02_T1_B6_REF.TIF') #swir
#generate nir and red objects as arrays in float64 format
red = band4.read(1).astype('float64')
nir = band5.read(1).astype('float64')
swir= band6.read(1).astype('float64')

#ndvi calculation, empty cells or nodata cells are reported as 0
ndvi=np.where((nir+red)==0., 0, (nir-red)/(nir+red))
#export ndvi image
ndviImage = rasterio.open('C:/Users/sowjanya jangam/Desktop/Seaweed/Atmoscorrection/ndviImage.tiff','w',driver='Gtiff',
                          width=band4.width, 
                          height = band4.height, 
                          count=1, crs=band4.crs, 
                          transform=band4.transform, 
                          dtype='float64')
ndviImage.write(ndvi,1)
ndviImage.close()
#plot ndvi
ndvi_2 = rasterio.open('C:/Users/sowjanya jangam/Desktop/Seaweed/Atmoscorrection/ndviImage.tiff')
fig = plt.figure(figsize=(18,12))
plot.show(ndvi)

#SEI calculation, empty cells or nodata cells are reported as 0
sei=np.where((nir+swir)==0., 0, (nir-swir)/(nir+swir))
#export sei image
seiImage = rasterio.open('C:/Users/sowjanya jangam/Desktop/Seaweed/Atmoscorrection/seiImage.tiff','w',driver='Gtiff',
                          width=band4.width, 
                          height = band4.height, 
                          count=1, crs=band4.crs, 
                          transform=band4.transform, 
                          dtype='float64')
seiImage.write(sei,1)
seiImage.close()
#plot sei
sei_2 = rasterio.open('C:/Users/sowjanya jangam/Desktop/Seaweed/Atmoscorrection/seiImage.tiff')
fig = plt.figure(figsize=(18,12))
plot.show(sei)

#fai calculation, empty cells or nodata cells are reported as 0
fai_v2=red+(swir-red)*210/(1609-655)
fai_v3=nir-fai_v2
fai=np.where((nir+red)==0., 0,fai_v3)
#export fai image
faiImage = rasterio.open('C:/Users/sowjanya jangam/Desktop/Seaweed/Atmoscorrection/faiImage.tiff','w',driver='Gtiff',
                          width=band4.width, 
                          height = band4.height, 
                          count=1, crs=band4.crs, 
                          transform=band4.transform, 
                          dtype='float64')
faiImage.write(fai,1)
faiImage.close()
#plot fai
fai_2 = rasterio.open('C:/Users/sowjanya jangam/Desktop/Seaweed/Atmoscorrection/faiImage.tiff')
fig = plt.figure(figsize=(18,12))
plot.show(fai)

