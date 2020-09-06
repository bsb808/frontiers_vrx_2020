'''
import matplotlib 
matplotlib.use('TkAgg')
from matplotlib.pyplot import *
from numpy import *
'''
# See https://matplotlib.org/api/matplotlib_configuration_api.html#matplotlib.rc
matplotlib.style.use('default')



matplotlib.rc('figure', figsize=list(array([6.4, 4.8])*1.25))
#matplotlib.rc('figure', dpi=300)
#matplotlib.rc('savefig', dpi=300)

font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : 16}

matplotlib.rc('font', **font)
matplotlib.rc('xtick', labelsize='small')
matplotlib.rc('ytick', labelsize='small')
matplotlib.rc('legend', fontsize='small')

matplotlib.interactive(False)


# use this to view all params
# See https://matplotlib.org/3.3.1/tutorials/introductory/customizing.html
#matplotlib.rc_params()

#matplotlib.style.use('default')
