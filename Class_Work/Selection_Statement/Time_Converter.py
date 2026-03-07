#Input Time in seconds and converted in corresponding hour minute and seconds
# example : input : 3665
# output : 1 hour 1 minute 5 seconds

# Get time in seconds from user
time_in_seconds = int(input("Enter time in seconds: "))
# initialize hours, minutes as 0
hours = 0
minutes = 0
#calculate number of hours in given seconds
if time_in_seconds >= 3600:
    hours = time_in_seconds // 3600
    time_in_seconds = time_in_seconds % 3600
# calculate number of minutes in remaining seconds
if time_in_seconds >= 60:
    minutes = time_in_seconds // 60
    time_in_seconds = time_in_seconds % 60
# remaining seconds
seconds = time_in_seconds
# display the result
print("Time : ", hours, "hour", minutes, "minute", seconds, "seconds"
      )