def isPathCrossing(path):
    locations = [(0, 0)]
    current_location = 0, 0

    for s in path:
        if s == "N":
            current_location = current_location[0] + 1, current_location[1]
        elif s == "E":
            current_location = current_location[0], current_location[1] + 1
        elif s == "S":
            current_location = current_location[0] - 1, current_location[1]
        elif s == "W":
            current_location = current_location[0], current_location[1] - 1
        if current_location in locations:
            return True
        locations.append(current_location)

    return False


path = "NESWW"
print(isPathCrossing(path))
