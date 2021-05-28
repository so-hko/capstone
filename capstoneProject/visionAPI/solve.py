#-*- coding: utf-8 -*-
import requests
import editdistance
from . import imageDetectionAPI
from . import accessDB
from . import getInfo

def getTextMiningResult(path):
    data = imageDetectionAPI.imagedetection()
    return data.split('\n')

#use DB
def parseDrugName():
    lt = accessDB.getDrugNameDB()
    #change to list
    if(str(type(lt)) == "<class 'tuple'>"):
        data = [item for t in lt for item in t]
        return data
    else:
        return data


def calcCorrRate(druglist, parselist):
    entireMatchingRate = []

    for drugname in druglist:
        ratelist = []
        for target in parselist:
            editdis = editdistance.eval(drugname, target)
            dflen = abs(len(target) - len(drugname))
            len1 = len(drugname)
            len2 = len(target)
            matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]
            for i in range(1, len1 + 1):
                for j in range(1, len2 + 1):
                    if drugname[i - 1] == target[j - 1]:
                        matrix[i][j] = matrix[i - 1][j - 1] + 1
                    else:
                        matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
        
            lcs = matrix[-1][-1]
            if(lcs > 2):
                ratelist.append(lcs**3 - editdis)

        entireMatchingRate.append(sum(ratelist))

    return entireMatchingRate

def extractDrugName():
    getInfo.getImage()
    path = "/home/ec2-user/capstone/capstoneProject/visionAPI/drug_image.jpg"
    druglist = parseDrugName()
    parselist = getTextMiningResult(path)
    entireMatchingRate = calcCorrRate(druglist, parselist)
    i = entireMatchingRate.index(max(entireMatchingRate))
    result = druglist[i]
    #print(entireMatchingRate[i])
    print("검색결과 : " + result)
    return result

extractDrugName()
