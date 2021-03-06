'''by vatsalchanana
Given a time in AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
'''

#!/bin/python3

import sys


time = input().strip("")
time = list(time)
if time[0] == '1' and time[1] == '2' and time[len(time)-2] == 'A':
    time[0] = str(int(time[0])-1)
    time[1] = str(int(time[1])-2)
if time[len(time)-2] == 'P':
    time[0] = str(int(time[0])+1)
    time[1] = str(int(time[1])+2)
del time[len(time)-1]
del time[len(time)-1]

print (''.join(time))
