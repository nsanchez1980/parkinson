import math

# The candles format should be "timestamp,open,high,low,close,volume". Adjust if necessary.

def parkinson(candles):
    logsquared = [math.log(float(x[2])/float(x[3]))**2 for x in candles]
    avg = sum(logsquared)/len(logsquared)
    return math.sqrt(avg/(4*math.log(2)))