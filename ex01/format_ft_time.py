from datetime import datetime

actualTime = datetime.now()

print("Seconds since January 1, 1970: ", format(actualTime.timestamp(), ","), "or", format(actualTime.timestamp(), ".2e"), "in scientific notation")
print(actualTime.strftime("%b %d %Y"))