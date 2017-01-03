import requests
import csv
import json
import os
import math

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
        targetFile = "./" + code + ".json"
        print(targetFile)
        data = json.loads(open((targetFile), "r").read())

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

        for i in range(0, len(teachingPeriods)):
            currentTeachingPeriod = teachingPeriods[i]
            units = currentTeachingPeriod["units"]

            try:
                year = startingYear + math.floor(i/2)
                semester = findCode(currentTeachingPeriod["teachingPeriod"]["semester"])
                unitsArray = []
                for i in range(0, len(units)):
                    targetURL = address + str(units[i])
                    r = requests.get(targetURL)
                    unitsArray.append(r.json())
                teachingPeriodOut = {"year": year, "code": semester, "units": unitsArray, "numberOfUnits": len(unitsArray)}
                output["teachingPeriods"].append(teachingPeriodOut)
            except:
                output["teachingPeriods"].append({})


        json_file.write(json.dumps(output, indent=4, sort_keys=True))




for filename in os.listdir("."):
    if filename != "python.py" and filename != "output": #converts all the file except for the Python File
        outputDir = filename.rstrip('.json')
        output = readme(outputDir, 2016)
