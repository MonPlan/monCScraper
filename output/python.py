import requests
import csv
import json
import os

address = "http://api.monplan.tech:3000/units/"


def findCode(targetString):
    if(targetString == 'Sem 1'):
        targetString = "Semester 1"
    elif (targetString == 'Sem 2'):
        targetString = "Semester 2"
    teachingPeriods = [['Semester 1', "S1-01"],['Semester 2', "S2-01"], ['Full Year', 'FY-01'],['Summer Semester A', 'SSA-02'],['Summer Semester A', 'SSB-01'],['Winter Semester B', 'WS-01']]
    for i in range(0, len(teachingPeriods)):
        if(teachingPeriods[i][0] == targetString):
            return teachingPeriods[i][1]
    print("Error Finding Teaching Period")
    return False

def readme(code, startingYear):
    file_name = "./updated/" + code + ".json"
    with open(file_name, "w") as json_file:
        targetFile = code + ".json"
        f = open(targetFile, "r")

        data = json.loads(f.read())

        teachingPeriods = data['teachingPeriods']
        code = data['courseCode']
        courseName = data['courseName']
        courseType = data['courseType']

        output = {"courseCode": code, "courseName": courseName, "courseType": courseType, "teachingPeriods": []}

        moreData = data["script"]
        moreData = (moreData.strip('\n')).split()
        jsonstring = ""
        for i in range(0, len(moreData)):
            jsonstring += moreData[i]
        
        print(jsonstring)
        for i in range(0, len(teachingPeriods)):
            currentTeachingPeriod = teachingPeriods[i]
            units = currentTeachingPeriod["units"]

            try:
                year = startingYear + i
                semester = findCode(currentTeachingPeriod["teachingPeriod"]["semester"])
                unitsArray = []
                for i in range(0, len(units)):
                    targetURL = address + str(units[i])
                    r = requests.get(targetURL)
                    unitsArray.append(r.json())
                teachingPeriodOut = {"year": year, "code": semester, "units": unitsArray, "numberOfUnits": len(unitsArray)}
                output["teachingPeriods"].append(teachingPeriodOut)
            except:
                print(" Error in " + code)


        print(output)




readme('C2001-0',2016)
