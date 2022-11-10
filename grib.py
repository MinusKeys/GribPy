from matplotlib import cm
import pygrib
import xarray as xr 
import xarray.plot as xplt
import numpy as np 
import cartopy.crs as ccrs 
import cartopy.feature as cfeature
import matplotlib.pyplot as plt 
import datetime 

ds = xr.open_dataset('data/output_grib_file.grib2',engine='cfgrib')

#print(ds)
temp = ds.isel(x=209,y=1)
temp1 = temp.to_array()
#print(temp)
#lat = 48.428421
#lon = -123.365646
#t0_ds = ds.isel(step=0)
temp1.plot()    
plt.show()
#xplt.line(temp1,)