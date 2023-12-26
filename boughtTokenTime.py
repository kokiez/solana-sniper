import datetime

"""
Useless file, implemented it in ETH sniper but never used in SOL sniper
"""
def saveTokenTime():
    current_time = datetime.datetime.now()
    print(f"********* Bought at [{current_time}] *********")
    with open("timestamp.txt", "w") as file:
        file.write(current_time.strftime("%Y-%m-%d %H:%M:%S"))

def isTimePassed(timestr):
    timeint = 0

    if "m" in timestr:
        timestr = int(timestr.replace("m",""))
        timeint = timestr * 60 #minute x seconds
    elif "h" in timestr:
        timestr = int(timestr.replace("h",""))
        timeint = timestr * 60 * 60 # hour x minute x seconds
    elif "d" in timestr:
        timestr = int(timestr.replace("d",""))
        timeint = (timestr * 24) * 60 * 60 #(number of day x total hours in day) x minutes x seconds
    
    # Read the timestamp from the file
    with open("timestamp.txt", "r") as file:
        timestamp_str = file.read()

    # Convert the timestamp string to a datetime object
    timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")

    # Calculate the time difference between the current time and the stored timestamp
    current_time = datetime.datetime.now()
    time_difference = current_time - timestamp

    # time has been passed by that limit
    if time_difference.total_seconds() >= timeint:
        return True
    else:
        return False