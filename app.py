from flask import Flask, render_template, request, url_for
import pandas as pd
import json
import plotly
import plotly.express as px

from data import totalPoints_fig, eventCode, bestTeams, rankings, teamsDone, totalPoints_teams, totalAutoPoints, totalTeleOpPoints, totalEndgamePoints, totalFoulCount, totalFoulPoints, totalEnemyTOPoints, noStringTeamInfo, noStringValues

app = Flask(__name__)

# @app.route('/')
# def layout():
#     return render_template('layout.html')




df = px.data.medals_wide()
fig = px.bar(df, x = "nation", y = ['gold', 'silver', 'bronze'], title = "Wide=Form Input")

graphJSON = json.dumps(fig, cls = plotly.utils.PlotlyJSONEncoder)

@app.route('/')
def index():
    return render_template('homePage.html', rankings=rankings, bestTeams=bestTeams, eventCode=eventCode)


@app.route('/homePage')
def homePage():
    return render_template('homePage.html', rankings=rankings, bestTeams=bestTeams, eventCode=eventCode)


@app.route('/totalValues')
def totalValues():
    return render_template('totalValues.html', rankings=rankings, bestTeams=bestTeams, totalPoints_fig=totalPoints_fig, sample_barfig=fig, teamsDone=teamsDone, totalPoints_teams=totalPoints_teams, totalAutoPoints=totalAutoPoints, totalTeleOpPoints=totalTeleOpPoints, totalEndgamePoints=totalEndgamePoints, totalFoulCount=totalFoulCount, totalFoulPoints=totalFoulPoints, totalEnemyTOPoints=totalEnemyTOPoints, noStringTeamInfo=noStringTeamInfo, values=noStringValues)


@app.route('/getDropdown')
def getDropdown():
    output = request.get_json()
    result = json.dumps(output)
    # print(output)
    # print(type(output))
    # print(result)
    # print(type(result))

    return result