function onSelection() {
    TEAMSELECTED = document.getElementById('teams').value;
    for (var x = 0; x < NOSTRINGTEAMINFO.length; x++) {
        if (NOSTRINGTEAMINFO[x][0] == TEAMSELECTED) {
            Plotly.newPlot('endgame', [{
                x: ['None', 'Low', 'Mid', 'High', 'Traversal'],
                y: [NOSTRINGTEAMINFO[x][1], NOSTRINGTEAMINFO[x][2], NOSTRINGTEAMINFO[x][3], NOSTRINGTEAMINFO[x][4], NOSTRINGTEAMINFO[x][5]],
                type: 'bar',
                title: 'Percent Endgame'
            }], {yaxis: {range: [0, 100]}});
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
        dataName = team[2];
        data.push({
            x: xAxis,
            y: yAxis,
            mode: 'lines',
            line: { shape: 'spline' },
            type: 'scatter',
            name: dataName
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


d3.csv(DATAFILEPATH, function(rows) {

    function unpack(rows, key) {
        return rows.map(function(row) { return row[key]; });
    }
    


    var headerNames = d3.keys(rows[0]);
    console.log("headerNames" + " = " + headerNames);

    var cellValues = [];
    var cellValue = null;
    // for (i = 1; i < rows.length; i++) {
    //     cellValue = unpack(rows, headerNames[i]);
    //     cellValues.push(cellValue);
    // }

    // for (i = 0; i < rows.length; i++) {
    //     if ((i % 2) == 0) {
    //         continue
    //     } else {
    //         cellValues.push(rows[i]);
    //         console.log("row " + i);
    //         console.log(rows[i]["Ranking"]);
    //     }
    // }

    for (i = 0; i < headerNames.length; i++) {
        // if ((i % 2) != 0) {
        //     cellValue = unpack(rows, headerNames[i]);
        // } else {
        //     continue
        // }

        cellValue = unpack(rows, headerNames[i]);
        cellValues[i] = cellValue;
    }

    tempList = [];
    for (x = 0; x < cellValues.length; x++) {
        for (i = 0; i < cellValues[x].length; i++) {
            if ((i % 2) != 0) {
                tempList.push(cellValues[x][i]);
            } else {
                continue
            }
        }
        cellValues[x] = tempList;
        tempList = [];
    }

    console.log(cellValues);

    var data = [{
        type: 'table',
        header: {
            values: headerNames,
            align: "center",
        },
        cells: {
            values: cellValues,
            align: ["center", "center"],
        }
    }]

    Plotly.newPlot('dataTable', data);

});