var TEAMSELECTED = null;
var TOTALPOINTS = {
    { totalPoints_teams } };
var TOTALAUTO = {
    { totalAutoPoints } };
var TOTALTELEOP = {
    { totalTeleOpPoints } };
var TOTALENDGAME = {
    { totalEndgamePoints } };
var TOTALFOULCOUNT = {
    { totalFoulCount } };
var TOTALFOULPOINTS = {
    { totalFoulPoints } };
var TOTALENEMYTO = {
    { totalEnemyTOPoints } };
var NOSTRINGTEAMINFO = {
    { noStringTeamInfo } };

function onSelection() {
    TEAMSELECTED = document.getElementById('teams').value;
    for (var x = 0; x < NOSTRINGTEAMINFO.length; x++) {
        if (NOSTRINGTEAMINFO[x][0] == TEAMSELECTED) {
            Plotly.newPlot('endgame', [{
                x: ['None', 'Low', 'Mid', 'High', 'Traversal'],
                y: [NOSTRINGTEAMINFO[x][1], NOSTRINGTEAMINFO[x][2], NOSTRINGTEAMINFO[x][3], NOSTRINGTEAMINFO[x][4], NOSTRINGTEAMINFO[x][5]],
                type: 'bar',
                title: 'Percent Endgame',
                name: name
            }]);
        }
    }
    TEAMSELECTED = null;
}


var data = [];

var xAxis = [];
var yAxis = [];
var name = [];
var dataType = null;
var graphID = null;
var dataTitle = null;
for (var x = 0; x < 7; x++) {
    if (x == 0) {
        dataType = TOTALPOINTS;
        graphID = 'totalPoints';
        graphTitle = 'Total Points'
    } else if (x == 1) {
        dataType = TOTALAUTO;
        graphID = 'totalAutoPoints';
        graphTitle = 'Total Autonomous Points'
    } else if (x == 2) {
        dataType = TOTALTELEOP;
        graphID = 'totalTeleOpPoints';
        graphTitle = 'Total TeleOp Points'
    } else if (x == 3) {
        dataType = TOTALENDGAME;
        graphID = 'totalEndgamePoints';
        graphTitle = 'Total Endgame Points'
    } else if (x == 4) {
        dataType = TOTALFOULCOUNT;
        graphID = 'totalFoulCount';
        graphTitle = 'Total Fouls Points'
    } else if (x == 5) {
        dataType = TOTALFOULPOINTS;
        graphID = 'totalFoulPoints';
        graphTitle = 'Total Foul Points'
    } else if (x == 6) {
        dataType = TOTALENEMYTO;
        graphID = 'totalEnemyTOPoints';
        graphTitle = 'Total Enemy Alliance Points'
    }

    for (var i = 0; i < dataType.length; i++) {
        var team = dataType[i];
        xAxis = team[0];
        yAxis = team[1];
        name = team[2];
        data.push({
            x: xAxis,
            y: yAxis,
            mode: 'lines',
            line: { shape: 'spline' },
            type: 'scatter',
            name: name
        });
        xAxis = [];
        yAxis = [];
    }
    Plotly.newPlot(graphID, data, { title: graphTitle });
    data = [];
    dataType = null;
    graphID = null;
    graphTitle = null;

}


onSelection();


d3.csv("{{ url_for('static', filename='data.csv') }}", function(rows) {

    function unpack(rows, key) {
        return rows.map(function(row) { return row[key]; });
    }

    var headerNames = d3.keys(rows[0]);

    var headerValues = [];
    var cellValues = [];
    var cellValue = null;
    for (i = 0; i < headerNames.length; i++) {
        headerValue = [headerNames[i]];
        headerValues[i] = headerValue;
        if ((i % 2) != 0) {
            cellValue = unpack(rows, headerNames[i]);
        } else {
            continue
        }
        cellValues[1] = cellValue;
    }



    var data = [{
        type: 'table',
        header: {
            values: headerValues,
            align: "center",
        },
        cells: {
            values: cellValues,
            align: ["center", "center"],
        }
    }]

    Plotly.newPlot('dataTable', data);

});