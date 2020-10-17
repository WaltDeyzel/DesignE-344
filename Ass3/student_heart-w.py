import numpy as np

def calibrate(time, amplitude):

    bpm = 0
    #rising edge
    t_now = 0
    t_past = 0
    period = 0
    periods = []
    flag = False
    #falling edge
    t_now1 = 0
    t_past1 = 0
    period1 = 0
    periods1 = []
    flag1 = False
    for i in range(len(amplitude)-1):
        div = amplitude[i+1]-amplitude[i]
        if( div > 4):
            t_past = t_now
            t_now = time[i]
            if(flag == True):
                period = t_now - t_past
                periods.append(period)
            flag = True
            
        if(div < -4):
            t_past1 = t_now1
            t_now1 = time[i]
            if(flag1 == True):
                period1 = t_now1 - t_past1
                periods1.append(period1)
            flag1 = True

    if(period == 0):
        return -1
    bpm = round(bmpRevenge(periods, periods1))
    
    return bpm
        
#python assignment_3_heart.py 1.9 66.6 150
#work\e344\e344\ass3

def bmpRevenge(risingEdge, fallingEdge):

    #accurate for everything above 100 TESTED
    if(len(risingEdge)>1):
        risingEdge.remove(risingEdge[0])
        fallingEdge.remove(fallingEdge[0])
        
    bpmA = 60*len(risingEdge)/sum(risingEdge)
    bpmB = 60*len(fallingEdge)/sum(fallingEdge)
    bpm = (bpmA+bpmB)/2
    return bpm
    
    #rising and falling edge average
    # new_period = (sum(risingEdge)+sum(fallingEdge))/(len(risingEdge)+len(fallingEdge)) 
    # print('new', 60/new_period)
    # return 60/new_period+0.6
