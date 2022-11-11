
import datetime
import numpy as np 

#Get current time and round down the hours
dt = datetime.datetime.now()
dt = dt - datetime.timedelta(hours=dt.hour)

#list of all forcast times 
forecastlist = [] 

# add hour offset and append to list
for i in range(0,48) : 
    dt = dt + datetime.timedelta(hours = i)
    forecastlist.append(dt.strftime("%Y%m%d%H"))

textlist = np.array([])

"""
File name nomenclaure
CMC_hrdps_domain_Variable_LevelType_level_ps2.5km_YYYYMMDDHH_Phhh-mm.grib2

Variables
PRATE_SFC_0 Precipitation rate
PRES_SFC_0 Surface Pressure
TMP_TGL_2m Temperature 2m above
ARAIN_SFC_0 Accumulated Precipitation type - Rain

example CMC_hrdps_west_TCDC_SFC_0_ps2.5km_2022111100_P000-00.grib2 
"""

#open file list 
"""
with open("filelist.txt","w") as file :
    file.write("test")
"""
