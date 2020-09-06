#########
# Run pubfig.py if ready to print

import pickle
import numpy as np
import os
# Need to creat the same data time used to pickle the info
'''
class Object(object):
    pass
'''
# OR
from bag2p import *

from plot_vrx_utils import parse_bagname

data = {}


# Note - data for these figures is on teams - https://nps01.sharepoint.com/:f:/s/FieldRoboticsLaboratory/EvhPhkP0rWBFrHNoL44iYKkBfpukUBrKjpvRfRwhS8hXHA?e=ze1r
# Use same data for either head_seas or beam_seas
logdir = '/home/bsb/data/2020_08_25_head_seas_001'
title_str = 'Head Seas'
#logdir = '/home/bsb/data/2020_08_25_beam_seas_001'
title_str = 'Beam Seas'
title_str = None



for f in os.listdir(logdir):
    if f.endswith(".p"):
        print ("Loading <%s>"%f)
        data[f] = pickle.load(open(os.path.join(logdir,f),"r"))

whattoplot = [('wamv_position','z'),
              ('wamv_euler','pitch'),
              ('wamv_euler','roll')]
# Amplitudes
N = 10000
amp = Object()
for wtp in whattoplot:
    setattr(amp,wtp[1],[])
setattr(amp,'file',[])
setattr(amp,'amplitude',[])
setattr(amp,'period',[])

for wtp in whattoplot:
    figure(wtp[1])
    clf()

for k in data.keys():
    getattr(amp,'file').append(k)
    a, p, l, r = parse_bagname(k)
    getattr(amp,'amplitude').append(a)
    getattr(amp,'period').append(p)
        
    
    for wtp in whattoplot:
        figure(wtp[1])
        t0 = getattr(getattr(data[k],wtp[0]),'t0')
        vals = getattr(getattr(data[k],wtp[0]),wtp[1])
        last_vals = vals[-N:]
        a = (max(last_vals) - min(last_vals)) / 2.0
        print "%s, %s, %.2f"%(k,wtp[1],a)
        getattr(amp,wtp[1]).append(a)

        plot(t0, vals, label=k)

    xlabel('Time [s]')
    ylabel(wtp[1])         
    legend()

figure('amp')
clf()
# Wave height
wh = 2.0 * array(amp.amplitude)

# Sort by wave height
zipped_list = zip(wh, amp.z, amp.pitch, amp.roll)
sorted_pairs = sorted(zipped_list)
tuples = zip(*sorted_pairs)
WH, HEAVE, PITCH, ROLL = [ list(tuple) for tuple in  tuples]



ax1 = subplot(1,1,1)
color = 'red'
ph = ax1.plot(WH, HEAVE, 'ro-', color=color, label='Heave')

#legend()
xlabel('Wave Height [m]')
ax1.set_ylabel('Heave [m]', color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax1.set_ylim([0, ax1.get_ylim()[1]*1.1])
ax1.set_xlim([0, ax1.get_xlim()[1]*1.0])
grid(True)


#ax1.set_title(os.path.split(logdir)[1])

if not (title_str is None):
    ax1.set_title(title_str)

color = 'blue'
ax2 = ax1.twinx()
ax2.set_ylabel('Euler angle [deg]', color='blue')

pp = ax2.plot(WH, 180.0/pi*array(PITCH), 'go-', label='Pitch')
pr = ax2.plot(WH, 180.0/pi*array(ROLL), 'bo-', label='Roll')

ax2.set_ylabel('Euler angles [degrees]', color=color)
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim([0, ax2.get_ylim()[1]*1.0])

# Legend for twin y axes
lns = ph+pp+pr
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc='upper left')


show()


#savefig(os.path.split(logdir)[1])
