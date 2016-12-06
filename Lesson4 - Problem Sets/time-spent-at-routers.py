#  Round trip time
rtt = 75
# The distance covered in one way
one_way_distance = 2500
# Total distance travelled 
distance = 2*2500
# Speed of light (given in km/sec)
speed_of_light_km_per_sec = 200000
# Speed of light (converted to km/msec)
speed_of_light_km_per_msec = speed_of_light_km_per_sec/1000
# Time taken to travel distance (5000)
tm = distance/speed_of_light_km_per_msec
# The rest of the time is taken by the routers
tm_taken_by_routers = rtt - tm
# Output the time taken by routers
print tm_taken_by_routers
