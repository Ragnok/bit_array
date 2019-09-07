'Demo for Sean for how to automatically population a parameter dictionary'

xlat = dict(hotwire='hw', backup='bu', runlive='rl')

def g(hotwire=None, backup=None, runlive=None):
    params = {}
    for key in ('hotwire', 'backup', 'runlive'):
        value = locals()[key]
        if value is not None:
            params[xlat[key]] = value
    return params
