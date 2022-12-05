def haveConflict(event1, event2):
    def to_seconds(time):
        timeSplit = time.split(":")
        hours = int(timeSplit[0])
        minutes = int(timeSplit[1])
        return hours * 60 ** 2 + minutes * 60

    seconds1 = [to_seconds(time) for time in event1]
    seconds2 = [to_seconds(time) for time in event2]

    if seconds1[0] > seconds2[0]:
        temp = seconds1
        seconds1 = seconds2
        seconds2 = temp

    if seconds1[1] < seconds2[0]:
        return False
    else:
        return True


event1 = ["11:30", "12:00"]
event2 = ["10:00", "11:29"]
print(haveConflict(event1, event2))
