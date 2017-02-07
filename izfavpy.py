import os
import time
import random

def iz_range(start, end, step):
  while start <= end:
    yield start
    start += step
        
        
def mapval(value, leftMin, leftMax, rightMin, rightMax):
  # Figure out how 'wide' each range is
  leftSpan = leftMax - leftMin
  rightSpan = rightMax - rightMin

  # Convert the left range into a 0-1 range (float)
  valueScaled = float(value - leftMin) / float(leftSpan)

  # Convert the 0-1 range into a value in the right range.
  return rightMin + (valueScaled * rightSpan)

