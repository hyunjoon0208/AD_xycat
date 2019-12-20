def GetAngleOfSensor(sensorId):
    sensorFrontAngle = 20
    if sensorId == 0:
        return 90 + sensorFrontAngle
    if sensorId == 1:
        return 90
    if sensorId == 2:
        return 90 - sensorFrontAngle
    if sensorId == 3:
        return 270 - sensorFrontAngle
    if sensorId == 4:
        return 270
    if sensorId == 5:
        return 270 + sensorFrontAngle
    if sensorId == 6:
        return 0
    if sensorId == 7:
        return 180

def GetAngleSpeed(rawAngleDistanceList):        
    result = {'angle' : 90, 'speed' : 90}
    if max(rawAngleDistanceList) <= 30:
        result["angle"] = -1
        result["speed"] = -1
    minDistance = 999
    thatAngle = 90
    frontMin = min(rawAngleDistanceList[0:3])
    backMin = min(rawAngleDistanceList[3:6])
    for i in range(len(rawAngleDistanceList)):
        if minDistance > rawAngleDistanceList[i]:
            minDistance = rawAngleDistanceList[i]
            thatAngle = GetAngleOfSensor(i)
    if minDistance > 50:
        result["angle"] = thatAngle
        result["speed"] = 90
        return result
    thatAngle = (thatAngle + 180) % 360
    if thatAngle == 0:
        if frontMin >= backMin:
            result['angle'] = 140
            result['speed'] = 125
        else:
            result["angle"] = 140
            result["speed"] = 60
    elif thatAngle == 180:
        if frontMin >= backMin:
            result["angle"] = 40
            result["speed"] = 125
        else:
            result["angle"] = 40
            result["speed"] = 60
    elif thatAngle < 180:
        result["angle"] = (thatAngle - 90) * -1 + 90
        result["speed"] = 125
    else:
        result['angle'] = thatAngle
        result['speed'] = 60
    return result;