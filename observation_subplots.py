from pathlib import Path

import matplotlib.pyplot as plt

from heroes.eprem.observers import Stream


directory = '/media/matthew/easystore/stat1-sr-unh-edu/data1/psi/corhel_run/ut200007140000-custom/cme20000714_v173/sep/eprem'
stream = Stream(351, directory=directory)
vr = stream['Vr']
times = [0.05, 0.1, 0.5]

savepath = f'~/Downloads/Vr-times.png'
fig, axs = plt.subplots(
    nrows=len(times),
    ncols=1,
    sharex=True,
    subplot_kw={'ylim': [0, 2e8]},
    figsize=(5, 10),
)
for ax, time in zip(axs, times):
    obs = vr(time=(time, 'day'))
    obs.plot(xaxis='shell', ax=ax)
plt.savefig(Path(savepath).expanduser().resolve())
