import os
import json
import netCDF4 as nc
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('masks') # countrymasks.nc
parser.add_argument('--out-dir', default='out')

o = parser.parse_args()

ds = nc.Dataset(o.masks)

variables = [v for v in ds.variables if v.startswith('m_')]

# load user-provided or ISIMIP-input data
input_data = load_input_data()

for v in variables:
    country_code = v[2:] # remove leading `m_`
    mask = ds[v][:] > 0  # for a binary mask (note a fractional mask is also provided)
    country_data = ... # agreggate input data on country mask

    output_dir = os.path.join(o.out_dir, country_code)
    output_file = os.path.join(output_dir, 'data.json')

    os.makedirs(output_dir, exist_ok=True)
    json.dump(country_data, open(output_file, 'w'))

ds.close()
