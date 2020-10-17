import numpy as np

def calibrate(time, amplitude):
        
    bpm = 0
    time_1 = 0
    time_2 = 0
    rising_edge = False
    temp = 0
    rising_period = []
    rising_period1 = []

    for x in range(len(amplitude)-1):
        delta = amplitude[x+1]-amplitude[x]
        if( delta > 4):
            if(time[x] > 2):
                time_2 = time_1
                time_1 = time[x]
                if(rising_edge == True):
                    temp = time_1 - time_2 
                    rising_period.append(temp) 
                    #print('Rising period', temp)
                rising_edge = True
            
    avg = sum(rising_period)/len(rising_period)
    #print('Average', avg)

    for i in range(len(rising_period)):
        dev = (rising_period[i] - avg) / avg
        if((dev < 0.1) & (dev > - 0.1)): 
            temp = rising_period[i]
            rising_period1.append(temp)
            #print('New Rising period', temp)
 
    temp = 60*len(rising_period1)/sum(rising_period1)
    bpm = round(temp)
    return bpm
