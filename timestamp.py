from datetime import datetime

# current date and time
now = datetime.now()
# convert from datetime to timestamp
ts = datetime.timestamp(now)

# Convert a stringtime to datetme
dt = datetime.strptime("2023-05-03 16:09:42.214", "%Y-%m-%d %H:%M:%S.%f")
ts = datetime.timestamp(dt)

print("Timestamp =", ts)