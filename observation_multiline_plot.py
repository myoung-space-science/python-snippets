from pathlib import Path

import matplotlib.pyplot as plt

from heroes.eprem.observers import Stream


directory = '/media/matthew/easystore/stat1-sr-unh-edu/data1/psi/corhel_run/ut200007140000-custom/cme20000714_v173/sep/eprem'
stream = Stream(351, directory=directory)
vr = stream['Vr']
times = [0.05, 0.1, 0.5]
units = 'day'

savepath = f'~/Downloads/Vr-times.png'
for time in times:
    obs = vr(time=(time, units))
    obs.plot(xaxis='shell', label=f'{time} {units}')
plt.ylim([0, 2e8])
plt.legend()
plt.savefig(Path(savepath).expanduser().resolve())
