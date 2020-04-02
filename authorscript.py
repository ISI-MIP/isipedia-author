import os
import json
import numpy as np
import netCDF4 as nc
import argparse

# countrymasks.nc or countrymasks_fractional.nc
COUNTRYMASKS = 'data/countrymasks.nc'

# output directory 
OUTPUTDIR = 'output'

# read countrymasks.nc or countrymasks_fractional.nc
ds = nc.Dataset(COUNTRYMASKS)

# load user-provided or ISIMIP-input data
# ... here a dummy example
lon = ds['lon'][:]
lat = ds['lat'][:]
dummydata1, dummydata2 = np.meshgrid(lon, lat)

for v in ds.variables:
  
    # do not loop over coordinate variables -- country mask variables start with 'm_'
    if not v.startswith('m_'):
        continue  
    
    # aggregate data based on country mask
    country_code = v[2:] # remove leading `m_`
    mask = ds[v][:] > 0  # for a binary mask (note a fractional mask is also provided)
    
    # agreggate input data on country mask
    # TODO: provide proper example with area weighting
    #       possibly spatial_average function in isipedia library
    # ... here a dummy example
    dummy1 = dummydata1[mask].mean()  
    dummy2 = dummydata2[mask].mean()
    country_data = {'lon': dummy1, 'lat': dummy2}
                      
    # create country-specific output directory and save as 'data.json'
    output_dir = os.path.join(OUTPUTDIR, country_code)
    output_file = os.path.join(output_dir, 'data.json')
    os.makedirs(output_dir, exist_ok=True)
    json.dump(country_data, open(output_file, 'w'))

ds.close()
