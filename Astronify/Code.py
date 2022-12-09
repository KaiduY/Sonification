from astropy.io import fits
from astropy.table import Table
from astronify import simulator, series

lc_data = simulator.simulated_lc("flat", lc_length=500, lc_noise=0.1, visualize=True, lc_yoffset=100.)
soni_obj = series.SoniSeries(lc_data)
soni_obj.sonify()
soni_obj.write('./Astronify/test.wav')
