# Write a procedure, speed_fraction, which takes as its inputs the result of
# a traceroute (in ms) and distance (in km) between two points. It should 
# return the speed the data travels as a decimal fraction of the speed of
# light.

speed_of_light = 300000. # km per second

def speed_fraction(time,distance):
    time_sec = time/1000.0  # convert time in ms
    rtt = distance*2        # calculate the round-trip-time
    light_time = rtt/speed_of_light*1.0     # time light would take to travel rtt
    return light_time/time_sec      # fraction of light time that the data travels at

print speed_fraction(50,5000)
#>>> 0.666666666667

print speed_fraction(50,10000)
#>>> 1.33333333333  # Any thoughts about this answer, or these inputs?