from machine import ADC, Pin

import cmath as math

adc = ADC(Pin(34))
print(adc.read())

adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

def Measure():
    global adc
    print(adc.read())

#Function that Calculate Root Mean Square
def rmsValue(arr, n):
    square = 0
    mean = 0.0
    root = 0.0
    #Calculate square
    for i in range(0,n): 
        square += (arr[i]**2)
    #Calculate Mean
    mean = (square / (float)(n))
    #Calculate Root
    root = math.sqrt(mean) 
    return root
  
#Driver code
# if __name__=='__main__': 
#     arr = [10, 4, 6, 8] 
#     n = len(arr) 
#     print(rmsValue(arr, n)) 

#This code is contributed by Shashank_Sharma 