from slsdet import Detector
import os 

def setup_somedet():
    os.environ['SLSDETNAME'] = 'erik'
    d = Detector()
    d.config = '~/virtual_one.config'
    return d