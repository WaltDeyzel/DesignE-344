import numpy as np

def calibrate(time, amplitude):
        
    ######################################
    # Enter calibration code here:
    ######################################
    temperature = []
    for analog in amplitude:
        temperature.append(analog/5)
        
    ######################################
        
    return temperature
        
