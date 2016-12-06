# Write a procedure, convert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#

def convert_seconds(seconds):
    hr = " hour"
    mins = " minute"
    sec = " second"
    
    # Get number of hours, minutes and seconds
    h = int(seconds/(60*60))
    m = int((seconds/60)%60)
    s = seconds%60      # Not converting to int to preserve the decimal
    
    # print plural e.g. hours, minutes, seconds for values other than 1
    if h != 1:
        hr = hr + "s"
    if m != 1:
        mins = mins + "s"
    if s != 1:
        sec = sec + "s"
        
    # Return the result as a string
    return str(h) + hr + ", " + str(m) + mins + ", " + str(s) + sec  


print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds

print convert_seconds(3600)
#>>> 1 hour, 0 minutes, 0 seconds