import upip

try:
    import ulogging
except ImportError:
    upip.install('pycopy-ulogging')
    pass

try:
    import utemplate
except ImportError:
    upip.install('utemplate')
    pass

try:
    import uasyncio
except ImportError:
    upip.install('uasyncio')
    # this needs to be manually installed the first time
    pass

try:
    import picoweb
except ImportError:
    upip.install('picoweb')
    pass