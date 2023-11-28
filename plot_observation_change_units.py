from heroes.eprem.observers import Stream


directory = '/media/matthew/easystore/stat1-sr-unh-edu/data1/psi/corhel_run/ut200007140000-custom/cme20000714_v173/sep/eprem'
stream = Stream(351, directory=directory)
vr = stream['Vr']
obs = vr(time=(0.1, 'day'))
obs.plot(savepath='~/Downloads/vr-cm.png')
obs.units.to('m/s')
obs.plot(savepath='~/Downloads/vr-m.png')

