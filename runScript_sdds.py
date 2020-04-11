import os
import sys
import time
import numpy as np
import matplotlib.pyplot as plt
import sdds_python
import sddsload
import subprocess
subprocess.run('elegant')

os.chdir(r'D:\IHEPBox\HEPS_2020\heps_v3p0\intrabeam scattering')
# =========================================================
#                           sdds_python
# =========================================================
# Read colomn data
# single page data use the :sdds_python.col
s = sdds_python.col('heps_v3p0.twi', 's')
betax = sdds_python.col('heps_v3p0.twi', 'betax')

# https://www.jianshu.com/p/87cb1a34ecb6
fig, ax = plt.subplots()
ax.plot(s, betax)
ax.set_xlabel('s(m)')
ax.set_ylabel(r'$\beta_x$')
ax.set_xlim(0, np.max(s)/24)
plt.show()
# =========================================================
# multipage data use the :sdds_python.col_page
s = sdds_python.col_page('heps_v3p0.twi', 's')
betax = sdds_python.col_page('heps_v3p0.twi', 'betax')
# https://www.jianshu.com/p/87cb1a34ecb6
fig, ax = plt.subplots()
ax.plot(s, betax)
ax.set_xlabel('s(m)')
ax.set_ylabel(r'$\beta_x$')
ax.set_xlim(0, np.max(s)/24)
plt.show()

# =========================================================
# read parameter data
# single page data
nux = sdds_python.par('heps_v3p0.twi', 'nux')
print(nux)

# multipage data
nux = sdds_python.par_page('heps_v3p0.twi', 'nux')
print(nux)

# =========================================================
#                           sddsload
# =========================================================


os.chdir(r'D:\IHEPBox\HEPS_2020\heps_v3p0\intrabeam scattering')
sdds = sddsload.file('heps_v3p0.twi')
s = sdds.col('s')
betax = sdds.col('betax')

fig, ax = plt.subplots()
ax.plot(s, betax)
ax.set_xlabel('s(m)')
ax.set_ylabel(r'$\beta_x$')
ax.set_xlim(0, np.max(s)/24)
plt.show()

#%%
# =========================================================
#                           import data
# =========================================================
import os
import numpy as np
import subprocess
os.chdir(r'D:\IHEPBox\HEPS_2020\heps_v3p0\intrabeam scattering')
subprocess.run('sddsprintout -col=s -wid=1000 heps_v3p0.twi twi.col')

p = np.loadtxt('twi.col',delimiter='', skiprows=5)
print(p)


# %%