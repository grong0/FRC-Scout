# from keep_alive import keep_alive
from csv import writer
from lib2to3.pgen2.token import NEWLINE
from os import name, system
import sys
from urllib import response
import requests
import pprint
from colorama import *
import numpy as np
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
from googleapiclient.discovery import build
from google.oauth2 import service_account

eventYear = "2022"
eventCode = "NYLI2"

username = "Grongo"
api_key = "wgGPuZZdB2nVqEiVXIYe"
# chart_studio.set_credentials_file(username=username, api_key=api_key)s

def clear(): 
  
    if name == 'nt': 
        _ = system('cls')

def biggest(none, low, mid, high, traversal):
    biggest = 0
    identity = ""
    multi = []
    num = []
    num.append(none)
    num.append(low)
    num.append(mid)
    num.append(high)
    num.append(traversal)
    for count, x in enumerate(num):
        if x > biggest:
            biggest = x
            if count == 0:
                identity = "None"
            elif count == 1:
                identity = "Low"
            elif count == 2:
                identity = "Mid"
            elif count == 3:
                identity = "High"
            elif count == 4:
                identity = "Traversal"
        elif x == biggest:
            if count == 0:
                multi.append("None")
            elif count == 1:
                multi.append("Low")
            elif count == 2:
                multi.append("Mid")
            elif count == 3:
                multi.append("High")
            elif count == 4:
                multi.append("Traversal")
    if len(multi) < 1:
        return identity
    together = ""
    for x in multi:
        together += (str(x) + " ")
    return together

def mostCommon(list):
    burger = list
    for x in burger:
        x.pop(0)
    highest = 0
    identity = None
    for x in list:
        if list.count(x) > highest:
            highest = list.count(x)
            identity = x
    return identity[0]

def getAverage(teamNumber, match = None, category = None):
    if category == None:
        if match == None:
            for team in teamInfo:
                if team['teamNumber'] == teamNumber:
                    return team
        else:
            for team in teamInfoByMatch:
                if team['teamNumber'] == teamNumber:
                    if team['matchNumber'] == match:
                        return team
    else:
        if match == None:
            for team in teamInfo:
                if team['teamNumber'] == teamNumber:
                    return team[category]
        else:
            for team in teamInfoByMatch:
                if team['teamNumber'] == teamNumber:
                    if team['matchNumber'] == match:
                        return team[category]

def Sort(sub_li):
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of 
    # sublist lambda has been used
    sub_li.sort(key = lambda x: x['teamNumber'])
    return sub_li

            
score_url = None
match_url = f"https://frc-api.firstinspires.org/v3.0/{eventYear}/matches/{eventCode}/qual"
teams_url = f"https://frc-api.firstinspires.org/v3.0/{eventYear}/teams?eventCode={eventCode}"
ranking_url = f"https://frc-api.firstinspires.org/v3.0/{eventYear}/rankings/{eventCode}"

payload={}
headers = {
  'Authorization': f'Basic {"cnNldGlhMjM6NmQxODM3NmEtNjYxMy00Y2FhLWFmY2UtYmNmZWE5MmI0OWJk"}',
  'If-Modified-Since': ''
}
score_response = None
match_response = requests.request("GET", match_url, headers=headers, data=payload)
teams_response = requests.request("GET", teams_url, headers=headers, data=payload)
ranking_response = requests.request("GET", ranking_url, headers=headers, data=payload)
score_data = None
match_data = dict(match_response.json())
teams_data = dict(teams_response.json())
ranking_data = dict(ranking_response.json())
matchesData = match_data["Matches"]
matchesScore = None
rankingData = ranking_data['Rankings']
teamsData = teams_data


# ranking_url = "https://frc-api.firstinspires.org/v3.0/2022/rankings/NYTR"
# ranking_response = requests.request("GET", ranking_url, headers=headers, data=payload)
# ranking_data = dict(ranking_response.json())
# rankingData = ranking_data['Rankings']

totalPoints_fig = None
subplots_fig = None

matchWithTotalPoints = {}


redTeams = []
blueTeams = []

redOrBlue = None
position = None

games = None
total_autoScore = 0
total_toScore = 0
total_egScore = 0
total_foulCount = 0
total_foulPoints = 0
total_toScoreNoMulti = 0
total_totalPoints = 0
total_enemyToScore = 0
total_taxi = 0
total_none = 0
total_low = 0
total_mid = 0
total_high = 0
total_traversal = 0
av_autoScore = None
av_toScore = None
av_egScore = None
av_foulCount = None
av_foulPoints = None
av_totalPoints = None
av_enemyToScore = None
percent_taxi = None
percent_none = None
percent_low = None
percent_mid = None
percent_high = None
percent_traversal = None
mostCommonEndgame = None

teamsDone = []
teamInfo = []

# matchList = [[1,"Blue3",None], [9,"Red1",None], [18,"Red2",None], [22,"Blue3",None], [33,"Red2",None], [41,"Red3",None], [45,"Red2","Low"], [49,"Blue1",None]]
# matchScore = None
# matchScore_response = None
# matchesScore = None
# scoreURL = f"https://frc-api.firstinspires.org/v3.0/2022/scores/NYTR/qual?teamNumber=6806"
# for x in matchList:
#     matchScoreURL = f"https://frc-api.firstinspires.org/v3.0/2022/matches/NYTR/qual?matchNumber={x[0]}"
#     matchScore_response = requests.request("GET", scoreURL, headers=headers, data=payload)
#     matchesScore = dict(matchScore_response.json())['MatchScores']
#     for y in matchesScore:
#         if "Blue" in x[1]:
#             pprint(x[1][])
#     if matchesScore[]
#     pprint(matchesScore)
#     pprint()
#     print("\n\n\n\n")
# exit()
currentTeam = None
keepGoing = True
station = None
count = 1
teamInfoByMatch = []

# keep_alive()

while keepGoing:
    for x in matchesData:
        for y in x['teams']:
            if y['teamNumber'] in teamsDone:
                continue
            
            score_url = f"https://frc-api.firstinspires.org/v3.0/{eventYear}/scores/{eventCode}/qual?teamNumber={y['teamNumber']}"
            match4team_url = f"https://frc-api.firstinspires.org/v3.0/{eventYear}/matches/{eventCode}/qual?teamNumber={y['teamNumber']}"
            
            
            score_response = requests.request("GET", score_url, headers=headers, data=payload)
            score_data = dict(score_response.json())['MatchScores']
            matches_response = requests.request("GET", match4team_url, headers=headers, data=payload)
            matches_data = dict(matches_response.json())
            games = len(score_data)
            byTime = len(score_data)
            byTimePerMatch = 1
            # pprint(score_data)
            # print('\n\n\n\n')
            # pprint(matchesData)
            for index, match in enumerate(score_data):
                byTime += index
                byTimePerMatch += index
                for teamMatch in matches_data['Matches']:
                    for teamsMatch in teamMatch['teams']:
                        if teamsMatch['teamNumber'] == y['teamNumber']:
                            if teamMatch['matchNumber'] == match['matchNumber']:
                                station = teamsMatch['station']
                if "Red" in station:
                    redOrBlue = 1
                elif "Blue" in station:
                    redOrBlue = 0
                position = int(station[-1])
                total_autoScore += match['alliances'][redOrBlue]['autoPoints']
                total_toScoreNoMulti += match['alliances'][redOrBlue]['teleopPoints']
                total_toScore += match['alliances'][redOrBlue]['teleopPoints'] * (index + 1)
                total_egScore += match['alliances'][redOrBlue]['endgamePoints']
                total_foulCount += match['alliances'][redOrBlue]['foulCount']
                total_foulPoints += match['alliances'][redOrBlue]['foulPoints']
                total_totalPoints += match['alliances'][redOrBlue]['totalPoints']
                if redOrBlue == 0:
                    total_enemyToScore += match['alliances'][1]['teleopPoints'] * (index + 1)
                elif redOrBlue == 1:
                    total_enemyToScore += match['alliances'][0]['teleopPoints'] * (index + 1)
                if match['alliances'][redOrBlue][f"taxiRobot{position}"] == "Yes":
                    total_taxi += 1 * (index + 1)
                elif match['alliances'][redOrBlue][f"taxiRobot{position}"] == "No":
                    total_taxi += 0
                if match['alliances'][redOrBlue][f"endgameRobot{position}"] == "None":
                    total_none += 1 * (index + 1)
                elif match['alliances'][redOrBlue][f"endgameRobot{position}"] == "Low":
                    total_low += 1 * (index + 1)
                elif match['alliances'][redOrBlue][f"endgameRobot{position}"] == "Mid":
                    total_mid += 1 * (index + 1)
                elif match['alliances'][redOrBlue][f"endgameRobot{position}"] == "High":
                    total_high += 1 * (index + 1)
                elif match['alliances'][redOrBlue][f"endgameRobot{position}"] == "Traversal":
                    total_traversal += 1 *(index + 1)
                # print(f"team {y['teamNumber']}'s total teleop score for round {index + 1} was {total_toScore}")
                av_autoScore = round(total_autoScore / (index + 1), 2)
                av_toScore = round(total_toScore / byTimePerMatch, 2)
                # print(f"team {y['teamNumber']}'s average teleop score for round {index + 1} was {av_toScore}")
                av_egScore = round(total_egScore / (index + 1), 2)
                av_foulCount = round(total_foulCount / (index + 1), 2)
                av_foulPoints = round(total_foulPoints / (index + 1), 2)
                av_totalPoints = round(total_totalPoints / (index + 1), 2)
                av_enemyToScore = round(total_enemyToScore / byTimePerMatch, 2)
                percent_taxi = round((total_taxi / byTimePerMatch) * 100, 2)
                percent_none = round((total_none / byTimePerMatch) * 100, 2)
                percent_low = round((total_low / byTimePerMatch) * 100, 2)
                percent_mid = round((total_mid / byTimePerMatch) * 100, 2)
                percent_high = round((total_high / byTimePerMatch) * 100, 2)
                percent_traversal = round((total_traversal / byTimePerMatch) * 100, 2)
                rawNone = round((total_none / byTimePerMatch) * 100, 2)
                rawLow = round((total_low / byTimePerMatch) * 100, 2)
                rawMid = round((total_mid / byTimePerMatch) * 100, 2)
                rawHigh = round((total_high / byTimePerMatch) * 100, 2)
                rawTraversal = round((total_traversal / byTimePerMatch) * 100, 2)
                mostCommonEndgame = biggest(rawNone, rawLow, rawMid, rawHigh, rawTraversal)

                teamInfoByMatch.append({
                    'teamNumber' : y['teamNumber'],
                    'matchNumber' : index + 1,
                    'AvAutoPoints' : av_autoScore,
                    'totalAutoPoints' : total_autoScore,
                    'AvTeleOpPoints' : av_toScore,
                    'totalTeleOpPoints' : total_toScoreNoMulti,
                    'AvEndgamePoints' : av_egScore,
                    'totalEndgamePoints' : total_egScore,
                    'AvFoulCount' : av_foulCount,
                    'totalFoulCount' : total_foulCount,
                    'AvFoulPoints' : av_foulPoints,
                    'totalFoulPoints' : total_foulPoints,
                    'AvTotalPoints' : av_totalPoints,
                    'totalTotalPoints' : total_totalPoints,
                    'AvEnemyTOPoints' : av_enemyToScore,
                    'totalEnemyTOPoints' : total_enemyToScore,
                    'PercentTaxi' : percent_taxi,
                    'PercentNone' : percent_none,
                    'PercentLow' : percent_low,
                    'PercentMid' : percent_mid,
                    'PercentHigh' : percent_high,
                    'PercentTraversal' : percent_traversal,
                    'MostCommonEndgame' : mostCommonEndgame
                })
                # print(f"team {y['teamNumber']} had a total teleOp score of {total_toScore} in match {index + 1}")

                av_autoScore = None
                av_toScore = None
                av_egScore = None
                av_foulCount = None
                av_foulPoints = None
                av_totalPoints = None
                av_enemyToScore = None
                percent_taxi =  None
                percent_none =  None
                percent_low =  None
                percent_mid =  None
                percent_high =  None
                percent_traversal =  None
                mostCommonEndgame = None

                redOrBlue = None
                position = None
                station = None
                
            av_autoScore = round(total_autoScore / games, 2)
            av_toScore = round(total_toScore / byTime, 2)
            av_egScore = round(total_egScore / games, 2)
            av_foulCount = round(total_foulCount / games, 2)
            av_foulPoints = round(total_foulPoints / games, 2)
            av_totalPoints = round(total_totalPoints / games, 2)
            av_enemyToScore = round(total_enemyToScore / byTime, 2)
            percent_taxi = round((total_taxi / byTime) * 100, 2)
            percent_none = round((total_none / byTime) * 100, 2)
            percent_low = round((total_low / byTime) * 100, 2)
            percent_mid = round((total_mid / byTime) * 100, 2)
            percent_high = round((total_high / byTime) * 100, 2)
            percent_traversal = round((total_traversal / byTime) * 100, 2)
            rawNone = round((total_none / games) * 100, 2)
            rawLow = round((total_low / games) * 100, 2)
            rawMid = round((total_mid / games) * 100, 2)
            rawHigh = round((total_high / games) * 100, 2)
            rawTraversal = round((total_traversal / games) * 100, 2)
            mostCommonEndgame = biggest(rawNone, rawLow, rawMid, rawHigh, rawTraversal)
            
            
            
            teamInfo.append({
                "teamNumber" : y['teamNumber'],
                "matchCount" : len(score_data),
                "AvAutoPoints" : av_autoScore,
                "AvTeleOpPoints" : av_toScore,
                "AvEndgamePoints" : av_egScore,
                "AvFoulCount" : av_foulCount,
                "AvFoulPoints" : av_foulPoints,
                "AvTotalPoints" : av_totalPoints,
                "AvEnemyTOPoints" : av_enemyToScore, # Change to based on difference in avereage team teleop score, to that match's score.
                "PercentTaxi" : percent_taxi,
                "PercentNone" : percent_none,
                "PercentLow" : percent_low,
                "PercentMid" : percent_mid,
                "PercentHigh" : percent_high,
                "PercentTraversal" : percent_traversal,
                "MostCommonEndgame" : mostCommonEndgame
            })
    
            teamsDone.append(y['teamNumber'])
    
            games = None
            total_autoScore = 0
            total_toScore = 0
            total_egScore = 0
            total_foulCount = 0
            total_foulPoints = 0
            total_toScoreNoMulti = 0
            total_totalPoints = 0
            total_enemyToScore = 0
            total_taxi = 0
            total_none = 0
            total_low = 0
            total_mid = 0
            total_high = 0
            total_traversal = 0
            av_autoScore = None
            av_toScore = None
            av_egScore = None
            av_foulCount = None
            av_foulPoints = None
            av_totalPoints = None
            av_enemyToScore = None
            percent_taxi = None
            percent_none = None
            percent_low = None
            percent_mid = None
            percent_high = None
            percent_traversal = None
            mostCommonEndgame = None
            
            clear()
            response_done = ''
            response_left = ''
            alt = True
            for x in range(count) :
                if alt :
                    response_done += "═"
                else :
                    response_done += "─"
            for x in range(teamsData['teamCountTotal'] - count) :
                if alt :
                    response_left += "═"
                else :
                    response_left += "─"
            sys.stdout.write(Fore.WHITE + "Compiling... ")
            sys.stdout.write(Fore.RED + response_done)
            sys.stdout.write(Fore.LIGHTBLACK_EX + response_left)
            sys.stdout.write(Fore.WHITE + f" {round((count / teamsData['teamCountTotal']) * 100, 2)}%")
            print()
            count += 1
             
    print(Fore.GREEN + "Done Compiling!")
    print(Fore.WHITE)
# teamInfo.append({
#     'teamNumber' : y['teamNumber'],
#     'AvAutoPoints' : av_autoScore,
#     'AvTeleOpPoints' : av_toScore,
#     'AvEndgamePoints' : av_egScore,
#     'AvFoulCount' : av_foulCount,
#     'AvFoulPoints' : av_foulPoints,
#     'AvTotalPoints' : av_totalPoints,
#     'AvEnemyTOPoints' : av_enemyToScore,
#     'PercentTaxi' : percent_taxi,
#     'PercentNone' : percent_none,
#     'PercentLow' : percent_low,
#     'PercentMid' : percent_mid,
#     'PercentHigh' : percent_high,
#     'PercentTraversal' : percent_traversal,
#     'MostCommonEndgame' : mostCommonEndgame
# })

    teamInfo = Sort(teamInfo)

    mod_teamInfo = []
    for x in teamInfo:
        mod_teamInfo.append(x)
    bestTeam = None
    bestTeams = []
    bestScores = [['AvAutoPoints'], ['AvTeleOpPoints'], ['AvEndgamePoints'], ['AvFoulCount'], ['AvFoulPoints'], ['AvTotalPoints'], ['AvEnemyTOPoints'], ['PercentTaxi'], ['PercentEndgame']]
    biggestNum = -100
    biggestTeam = None
    smallestNum = 100
    smallestTeam = None
    endgamePoints = -100
    for z in range(len(teamInfo)):
        for y in range(9):
            if y == 0:
                for x in mod_teamInfo:
                    if x['AvTotalPoints'] > biggestNum:
                        biggestNum = x['AvTotalPoints']
                        biggestTeam = x['teamNumber']
                bestScores[0].append(biggestTeam)
                biggestNum = -100
                biggestTeam = None
            elif y == 1:
                for x in mod_teamInfo:
                    if x['AvTeleOpPoints'] > biggestNum:
                        biggestNum = x['AvTeleOpPoints']
                        biggestTeam = x['teamNumber']
                bestScores[1].append(biggestTeam)
                biggestNum = -100
                biggestTeam = None
            elif y == 2:
                for x in mod_teamInfo:
                    if x['AvEndgamePoints'] > biggestNum:
                        biggestNum = x['AvEndgamePoints']
                        biggestTeam = x['teamNumber']
                bestScores[2].append(biggestTeam)
                biggestNum = -100
                biggestTeam = None
            elif y == 3:
                for x in mod_teamInfo:
                    if x['AvFoulCount'] < smallestNum:
                        smallestNum = x['AvFoulCount']
                        smallestTeam = x['teamNumber']
                bestScores[3].append(smallestTeam)
                smallestNum = 100
                smallestTeam = None
            elif y == 4:
                for x in mod_teamInfo:
                    if x['AvFoulPoints'] < smallestNum:
                        smallestNum = x['AvFoulPoints']
                        smallestTeam = x['teamNumber']
                bestScores[4].append(smallestTeam)
                smallestNum = 100
                smallestTeam = None
            elif y == 5:
                for x in mod_teamInfo:
                    if x['AvTotalPoints'] > biggestNum:
                        biggestNum = x['AvTotalPoints']
                        biggestTeam = x['teamNumber']
                bestScores[5].append(biggestTeam)
                biggestNum = -100
                biggestTeam = None
            elif y == 6:
                for x in mod_teamInfo:
                    if x['AvEnemyTOPoints'] < smallestNum:
                        smallestNum = x['AvEnemyTOPoints']
                        smallestTeam = x['teamNumber']
                bestScores[6].append(smallestTeam)
                smallestNum = 100
                smallestTeam = None
            elif y == 7:
                for x in mod_teamInfo:
                    if x['PercentTaxi'] > biggestNum:
                        biggestNum = x['PercentTaxi']
                        biggestTeam = x['teamNumber']
                bestScores[7].append(biggestTeam)
                biggestNum = -100
                biggestTeam = None
            elif y == 8:
                for x in mod_teamInfo:
                    if (((x['PercentNone']) * 1) + ((x['PercentLow']) * 2) + ((x['PercentMid']) * 3) + ((x['PercentHigh']) * 4) + ((x['PercentTraversal']) * 5)) > endgamePoints:
                        endgamePoints = (((x['PercentNone']) * 1) + ((x['PercentLow']) * 2) + ((x['PercentMid']) * 3) + ((x['PercentHigh']) * 4) + ((x['PercentTraversal']) * 5))
                        biggestTeam = x['teamNumber']
                bestScores[8].append(biggestTeam)
                endgamePoints = -100
                biggestTeam = None
        bestTeam = mostCommon(bestScores)
        bestTeams.append(bestTeam)
        for index, x in enumerate(mod_teamInfo):
            if x['teamNumber'] == bestTeam:
                mod_teamInfo.pop(index)

    
    values = [
        ['Team Number', '', 'Av Auto Points', 'Av TO Points', 'Av EG Points', 'Av Foul Count', 'Av Foul Points', 'Av Total Points', 'Av Enemy TO', 'Taxi Robot', 'None End game', 'Low End game', 'Mid End game', 'High End game', 'Traversal EG', 'Most Common', '', 'Pos', 'Ranking', 'Best Teams']
    ]
    noStringValues = []
    rankings = []
    for x in rankingData:
        rankings.append(x['teamNumber'])


    noStringTeamInfo = []
    placeHolder = []
    for index, x in enumerate(teamInfo):
        noStringTeamInfo.append([x['teamNumber'], x['PercentNone'], x['PercentLow'], x['PercentMid'], x['PercentHigh'], x['PercentTraversal']])
        placeHolder = []
        ranking_url = f"https://frc-api.firstinspires.org/v3.0/{eventYear}/rankings/{eventCode}?{x['teamNumber']}"
        ranking_response = requests.request("GET", ranking_url, headers=headers, data=payload)
        ranking_data = dict(ranking_response.json())
        rankingData = ranking_data['Rankings']
        values.append(
            [x['teamNumber'], 
            '', 
            x['AvAutoPoints'], 
            x['AvTeleOpPoints'], 
            x['AvEndgamePoints'], 
            x['AvFoulCount'], 
            x['AvFoulPoints'], 
            x['AvTotalPoints'], 
            x['AvEnemyTOPoints'], 
            str(x['PercentTaxi']) + "%", 
            str(x['PercentNone']) + "%", 
            str(x['PercentLow']) + "%", 
            str(x['PercentMid']) + "%", 
            str(x['PercentHigh']) + "%", 
            str(x['PercentTraversal']) + "%", 
            x['MostCommonEndgame'], 
            '', 
            (index + 1), 
            rankings[index], 
            bestTeams[index]]
        )
        noStringValues.append(
            [x['teamNumber'],
            x['AvAutoPoints'], 
            x['AvTeleOpPoints'], 
            x['AvEndgamePoints'], 
            x['AvFoulCount'], 
            x['AvFoulPoints'], 
            x['AvTotalPoints'], 
            x['AvEnemyTOPoints'], 
            x['PercentTaxi'], 
            x['PercentNone'], 
            x['PercentLow'], 
            x['PercentMid'], 
            x['PercentHigh'], 
            x['PercentTraversal'], 
            x['MostCommonEndgame'],
            (index + 1), 
            rankings[index], 
            bestTeams[index]]
        )
        
    # teamInfo.append({
    #     'teamNumber' : y['teamNumber'],
    #     'AvAutoPoints' : av_autoScore,
    #     'AvTeleOpPoints' : av_toScore,
    #     'AvEndgamePoints' : av_egScore,
    #     'AvFoulCount' : av_foulCount,
    #     'AvFoulPoints' : av_foulPoints,
    #     'AvTotalPoints' : av_totalPoints,
    #     'PercentTaxi' : percent_taxi,
    #     'PercentNone' : percent_none,
    #     'PercentLow' : percent_low,
    #     'PercentMid' : percent_mid,
    #     'PercentHigh' : percent_high,
    #     'PercentTraversal' : percent_traversal,
    #     'MostCommonEndgame' : mostCommonEndgame
    # })
    
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = 'keys.env'
    
    creds = None
    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    
    
    # The spreadsheet ID.
    SPREADSHEET_ID = '13OorT1cZL3STDFSnXgcI7PfjIwNWAMtG-RuH_xchN-8'
    
    service = build('sheets', 'v4', credentials=creds)
    
    RANGE = "A2:ZZ120"
    # Call the Sheets API
    sheet = service.spreadsheets()

    f = open("templates/data.csv", "w")
    writer = writer(f)
    for x in values:
        writer.writerow(x)
    # writer.writerows(values)
    f.close

    # with open("templates\data.csv", 'w') as t:
    #     t.truncate()
    #     writer = writer(t, NEWLINE="")
    #     writer.writerows(values)
    
    
    
    body = {
        # 'requests' : [
        #     {
        #         "setDataValidation": {
        #             "range": {
        #                 "sheetId": SPREADSHEET_ID,
        #                 "startRowIndex": 1,
        #                 "endRowIndex": 1,
        #                 "startColumnIndex": 22,
        #                 "endColumnIndex": 23
        #             },
        #             "rule": {
        #                 "condition": {
        #                 "type": 'ONE_OF_LIST',
        #                 "values": [
        #                     {
        #                     "userEnteredValue": 'High - Low',
        #                     },
        #                     {
        #                     "userEnteredValue": 'Low - High',
        #                     },
        #                 ],
        #                 },
        #                 "showCustomUi": True,
        #                 "strict": True
        #             }
        #         }
        #     }
        # ],
        'values' : values
    }

    teamsDone.sort()
    
    result = service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID, 
        range=RANGE,
        valueInputOption='RAW', 
        body=body
    ).execute()

    highestMatchCount = 0
    for team in teamInfo:
        if team['matchCount']:
            highestMatchCount = team['matchCount']
    
    xValues = []
    for x in range(highestMatchCount):
        xValues.append(x)
    
    totalPointsData = []
    team = None
    teamMatch = None
    goToNext = False
    xAxis = []
    yAxis = []
    totalPoints_teams = []
    for y in teamsDone:
        team = getAverage(y)
        for x in range(team['matchCount']):
            teamMatch = getAverage(y, x + 1)
            xAxis.append(teamMatch['matchNumber'])
            yAxis.append(teamMatch['totalTotalPoints'])
            # for burger in teamInfoByMatch:
            #     if burger['teamNumber'] == y:
            #         if burger['matchNumber'] == teamMatch['matchNumber']:
            #             print(f"total points for team {y} in match {x + 1} was {teamMatch['totalTotalPoints']} \nTheir total points via teamInfoByMatch is {burger['totalTotalPoints']}")
        totalPointsData.append(
            go.Scatter(
                name = y,
                mode = 'lines',
                line_shape = 'spline',
                x = xAxis,
                y = yAxis
            )
        )

        totalPoints_teams.append([xAxis, yAxis, y])

        team = None
        teamMatch = None
        xAxis = []
        yAxis = []
    layout = go.Layout(
        xaxis=dict(
            title = "Team's Respective Match",
            linecolor = 'white',
            gridcolor = 'rgba(255, 255, 255, 50)'
        ),
        yaxis=dict(
            title = "Points",
            linecolor = 'white',
            gridcolor = 'rgba(255, 255, 255, 50)'
        ),
        height=800,
        title="Total Points",
        # paper_bgcolor='rgba(0,0,0,0)',
        # plot_bgcolor='rgba(0,0,0,0)'
    )
    totalPoints_fig = {
        'data' : totalPointsData,
        'layout' : layout
    }
    # For offline loading
    # totalPoints_fig = go.Figure(data = totalPointsData, layout = layout)
    # plotly.offline.plot(
    #     totalPoints_fig, 
    #     filename = 'curveGraph.html',
    #     config = {'displayModeBar' : False}
    # )

    y1 = np.random.randn(200) - 1
    y2 = np.random.randn(200)
    y3 = np.random.randn(200) + 1
    x = np.linspace(0, 1, 200)

    colors = ['#3f3f3f', '#00bfff', '#ff7f00']
    specs = []
    for x in range(3):
        specs.append(
            [{"type": "scatter"} , {"type": "scatter"}]
        )
    row_height = 5.0
    subplots_fig = make_subplots(
        rows=3, cols=2,


        subplot_titles=[
            'Autonomous Points',
            'Foul Count',
            'TeleOp Points',
            'Foul Points',
            'Endgame Points',
            'Enemy TeleOp Points'
        ],


        column_widths=[0.5, 0.5],
        

        # [[{"type": "scatter"}, {"type": "xy"}],
        # [{"type": "scatter"}, {"type": "xy", "rowspan": 2}],
        # [{"type": "scatter"},            None           ]]
        row_heights=[row_height, row_height, row_height],
        specs=specs
    )
    teamDataPoints = []
    totalAutoPoints = []
    totalTeleOpPoints = []
    totalEndgamePoints = []
    totalFoulCount = []
    totalFoulPoints = []
    totalTotalPointsData = []
    totalEnemyTOPoints = []
    data = []
    for z in range(6):
        for y in teamsDone:
            team = getAverage(y)
            for x in range(team['matchCount']):
                teamMatch = getAverage(y, x + 1)
                xAxis.append(teamMatch['matchNumber'])
                if z == 0:
                    yAxis.append(teamMatch['totalAutoPoints'])
                elif z == 1:
                    yAxis.append(teamMatch['totalTeleOpPoints'])
                elif z == 2:
                    yAxis.append(teamMatch['totalEndgamePoints'])
                elif z == 3:
                    yAxis.append(teamMatch['totalFoulCount'])
                elif z == 4:
                    yAxis.append(teamMatch['totalFoulPoints'])
                elif z == 5:
                    yAxis.append(teamMatch['totalEnemyTOPoints'])
            if z == 0:
                totalAutoPoints.append([xAxis, yAxis, y])
            elif z == 1:
                totalTeleOpPoints.append([xAxis, yAxis, y])
            elif z == 2:
                totalEndgamePoints.append([xAxis, yAxis, y])
            elif z == 3:
                totalFoulCount.append([xAxis, yAxis, y])
            elif z == 4:
                totalFoulPoints.append([xAxis, yAxis, y])
            elif z == 5:
                totalEnemyTOPoints.append([xAxis, yAxis, y])
            data.append(
                go.Scatter( 
                    name = y,
                    mode = 'lines',
                    line_shape = 'spline',
                    x = xAxis,
                    y = yAxis
                )
            )
            teamDataPoints.append(yAxis)
            team = None
            teamMatch = None
            xAxis = []
            yAxis = []
        if z < 3:
            subplots_fig.add_traces(data, rows = 1 + z, cols = 1)
        else:
            subplots_fig.add_traces(data, rows = -2 + z, cols = 2)
        data = []

    
    # fig.add_trace(
    #     go.Scatter(x = x, 
    #                 y = y1,
    #                 hoverinfo = 'x+y',
    #                 mode='lines',
    #                 line=dict(color='#3f3f3f',
    #                 width=1),
    #                 showlegend=False,
    #                 ),
    #     row=1, col=1
    # )

    # fig.add_trace(
    #     go.Scatter(x = x, 
    #                 y = y2,
    #                 hoverinfo = 'x+y',
    #                 mode='lines',
    #                 line=dict(color='#00bfff',
    #                 width=1),
    #                 showlegend=False,
    #                 ),
    #     row=2, col=1
    # )

    # fig.add_trace(
    #     go.Scatter(x = x, 
    #                 y = y3,
    #                 hoverinfo = 'x+y',
    #                 mode='lines',
    #                 line=dict(color='#ff7f00',
    #                 width=1),
    #                 showlegend=False,
    #                 ),
    #     row=3, col=1
    # )


    # boxfig= go.Figure(data=[go.Box(x=y1, showlegend=False, notched=True, marker_color="#3f3f3f", name='3'),
    #                         go.Box(x=y2, showlegend=False, notched=True, marker_color="#00bfff", name='2'),
    #                         go.Box(x=y3, showlegend=False, notched=True, marker_color="#ff7f00", name='1')])

    # for k in range(len(boxfig.data)):
    #     fig.add_trace(boxfig.data[k], row=1, col=2)

    group_labels = teamsDone
    hist_data = teamDataPoints

    # distplfig = ff.create_distplot(hist_data, group_labels, colors=colors,
    #                         bin_size=.2, show_rug=False)

    # for k in range(len(distplfig.data)):
    #     fig.add_trace(distplfig.data[k],
    #     row=2, col=2
    # )
    subplots_fig.update_layout(
        barmode='overlay',
        height=1000,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    # subplots_fig.update_xaxes(showline=True, linewidth=2, linecolor='white', gridcolor='rgba(255, 255, 255, 50)')
    # subplots_fig.update_yaxes(showline=True, linewidth=2, linecolor='white', gridcolor='rgba(255, 255, 255, 50)')
    # plotly.offline.plot(subplots_fig, filename='test.html')

    clear()
    print('{0} cells updated.'.format(result.get('updatedCells')))
    keepGoing = False