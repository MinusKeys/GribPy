from matplotlib import cm
import pygrib
import xarray as xr 
import xarray.plot as xplt
import numpy as np 
import cartopy.crs as ccrs 
import cartopy.feature as cfeature
import matplotlib.pyplot as plt 
import datetime 


# open grouped grib file as Xarray dataset
ds = xr.open_dataset('data/output_grib_file.grib2',engine='cfgrib')


# select current lon and lat grid point from lamwestpoints, and then convert to data array
#lat = 48.428421
#lon = -123.365646
temp = ds.isel(x=209,y=1).to_array()

#line plot 
temp.plot()    

plt.show()
