import time
while 1:
  value = raw_input('Press Enter to start timer':)
  if value == '':
    startTime = time.time()
    print startTime
    pass
  value1= raw_input('Press Enert to end the timer':)
  if value1 == '':
    endTime = time.time()
    print endTime
    totalTime = endTime - startTime
    print 'The total Time is',totalTime
    break
