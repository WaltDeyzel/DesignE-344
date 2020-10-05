import numpy as np

def calibrate(time, amplitude):
        
    ######################################
    # Enter calibration code here:
    ######################################
    bpm = 0
    rise = 0
    for beat in amplitude:
        if(rise == 0 and beat > 4.5):
            print('alive')
            rise = 1
        elif(rise == 1 and beat < 0.5):
            rise = 0
        
        
    ######################################
        
    return bpm
        
