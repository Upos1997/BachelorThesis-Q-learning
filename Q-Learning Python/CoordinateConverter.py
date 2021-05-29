import math


def convert(file):
    def getDistance(lat1, lon1, lat2, lon2):
        R = 6371000 # radius of the earth
        deltaLat = abs(lat2 - lat1)
        deltaLon = abs(lon2 - lon1)
        a = math.sin(deltaLat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(deltaLon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        return round(R * c / 1000)

    def getLat(line):
        line = line.split(" ")
        return math.radians(float(line[1]))

    def getLon(line):
        line = line.split(" ")
        return math.radians(float(line[2]))

    def getName(line):
        line = line.split(" ")
        return line[3][0:-1]

    file = open(file, 'r')
    lines = file.readlines()
    matrix = []
    for line1 in lines:
        lat1 = getLat(line1)
        lon1 = getLon(line1)
        matrixLine = []
        for line2 in lines:
            lat2 = getLat(line2)
            lon2 = getLon(line2)
            if line1 == line2:
                matrixLine.append(0)
            else:
                matrixLine.append(getDistance(lat1, lon1, lat2, lon2))
        if matrix:
            matrix.append(matrixLine)
        else:
            matrix = [matrixLine]
    return matrix