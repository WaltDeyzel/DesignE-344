import numpy as np

def calibrate(time, amplitude):

    calibration_number = 4.77 # average of max analog reading at 42 degrees
    minTemp = 34             # min temp for testing
    div = 8                  # div between min and max temp 

    # average analog value
    analog = sum(amplitude)/len(amplitude)
    # convertion formula
    temperature = minTemp+analog*div/calibration_number


    print(analog, temperature)
        
    return temperature
        
