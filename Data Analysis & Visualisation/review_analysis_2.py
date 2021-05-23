#Import Libraries
from datetime import datetime as dt
from pytz import utc
import justpy as jp
import pandas

#Read CSV file containing all reviews and set Timestamp column values to be of date type
df = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])

#Create a column for month (%Y makes sure that same months in different years dont get considered the same)
df["Month"] = df["Timestamp"].dt.strftime("%Y-%m") #(%m is for month value)
#Group data by month and course name thus resulting dataframe will have 2 index columns when we unstack() the data
#We then find the mean of the ratings of each course by month
crs_mon_avg = df.groupby(["Month", "Course Name"])["Rating"].mean().unstack()

#Create a new column for the days of the Week which are taken from the timestamp datetime object
#We split the timestamp using strftime to get the Weekday using %A
df["Weekday"] = df["Timestamp"].dt.strftime("%A")
#Create a new column for the day numbers for each day which are taken from the timestamp datetime object
#We split the timestamp using strftime to get the day number using %w
df["DayNumber"] = df["Timestamp"].dt.strftime("%w")
#We then group all the data by the weekday and daynumber columns and find the mean
wkdy_avg = df.groupby(["Weekday", "DayNumber"]).mean()
#We also sort the data by DayNumber
wkdy_avg = wkdy_avg.sort_values("DayNumber")

#Groups data by the course name and find the number of ratings per course
crs_rat_cnt = df.groupby(["Course Name"])["Rating"].count()

#Spline chart for average rating per course per month
spline_chart_crs_month_def = '''
 {
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average Rating Of Course By Month'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: true,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        categories: [
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ''
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
'''

#Stream chart for average rating per course per month
stream_chart_crs_month_def = '''
{
    chart: {
        type: 'streamgraph',
        marginBottom: 30,
        zoomType: 'x'
    },

    title: {
        floating: true,
        align: 'left',
        text: 'Average Rating Of Course By Month'
    },
    subtitle: {
        floating: true,
        align: 'left',
        y: 30,
        text: 'Based on reviews given by 50,000 users'
    },

    xAxis: {
        maxPadding: 0,
        type: 'category',
        crosshair: true,
        categories: [
        ],
        labels: {
            align: 'left',
            reserveSpace: false,
            rotation: 270
        },
        lineWidth: 0,
        margin: 20,
        tickWidth: 0
    },

    yAxis: {
        visible: false,
        startOnTick: false,
        endOnTick: false
    },

    legend: {
        enabled: false
    },

    plotOptions: {
        series: {
            label: {
                minFontSize: 5,
                maxFontSize: 15,
                style: {
                    color: 'rgba(255,255,255,0.75)'
                }
            }
        }
    },

    // Data parsed with olympic-medals.node.js
    series: [{
        name: "Finland",
        data: [
            0, 11, 4, 3, 6, 0, 0, 6, 9, 7, 8, 10, 5, 5, 7, 9, 13, 7, 7, 6, 12, 7, 9, 5, 5
        ]
    }, {
        name: "Austria",
        data: [
            0, 3, 4, 2, 4, 0, 0, 8, 8, 11, 6, 12, 11, 5, 6, 7, 1, 10, 21, 9, 17, 17, 23, 16, 17
        ]
    }],

    exporting: {
        sourceWidth: 800,
        sourceHeight: 600
    }
}
'''

#Spline Chart for what day of the week people are most positive
spline_chart_pos_week_def = '''
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'What Day Of The Week Are People Most Positive'
    },
    subtitle: {
        text: 'Based on ratings given by 50,000 users'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Day'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x}: {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
'''

#Pie Chart for percentage of ratings by course
pie_chart_crs_rating_cnt_def = '''
{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Percentage Of Ratings By Course'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}
'''

def app():
    #Creates a webpage and loads it in dark mode
    wp = jp.QuasarPage(dark=True)

    #Heading and Sub-Heading Tags
    h1 = jp.QDiv(a=wp, text="Analysis Of Course Reviews Pt2", classes="text-h3 text-weight-bolder text-center q-pa-md")
    h2 = jp.QDiv(a=wp, text="These graphs plot the Ratings of courses across certain timelines and intervals", 
    classes="text-h5 text-weight-bolder text-center q-pa-md")

    #Highchart (Area Spline) for average ratings by month by course
    hc1 = jp.HighCharts(a=wp, options=spline_chart_crs_month_def)
    #Access the dictionary that contains chart data using hc.options
    hc1.options.xAxis.categories = list(crs_mon_avg.index) #Sets the X-Axis value to the index of the crs_mon_avg dataframe(month)
    #n1 loops through the course name column and d1 loops through the ratings for that particular course
    hc1_data = [{"name": n1, "data":[d1 for d1 in crs_mon_avg[n1]]} for n1 in crs_mon_avg.columns]
    #Set the value of series of the chart to the data using hc1_data
    hc1.options.series = hc1_data

    #Highchart (Series) for average ratings by month by course
    hc2 = jp.HighCharts(a=wp, options=stream_chart_crs_month_def)
    #Access the dictionary that contains chart data using hc.options
    hc2.options.xAxis.categories = list(crs_mon_avg.index)#Sets the X-Axis value to the index of the crs_mon_avg dataframe(month)
    #Set the value of series of the chart to the data using hc1_data
    hc2.options.series = hc1_data

    #Highchart (Spline) for average ratings by weekday to see when everyone is most positive
    hc3 = jp.HighCharts(a=wp, options=spline_chart_pos_week_def)
    #X-Axis is weekdays -> wkdy_avg has two indexes -> one for weekdays and the other for weeknumbers
    hc3.options.xAxis.categories = list(wkdy_avg.index.get_level_values(0))#Sets X_Axis value to index containing weekdays
    #We then plot the average rating on each day against the X-Axis
    hc3.options.series[0].data = list(wkdy_avg["Rating"])

    #Highchart (PieChart) for number of ratings per course
    hc4 = jp.HighCharts(a=wp, options=pie_chart_crs_rating_cnt_def)
    #Extracts the course name and the ratings per course
    hc4_data = [{"name": a, "y": b} for a,b in zip(crs_rat_cnt.index, crs_rat_cnt)] #Index of dataframe has course names
    #Assigns that data to the PieChart
    hc4.options.series[0].data = hc4_data

    #Returns the webpage
    return wp

#Expects a function which returns a webpage and runs it to load webpage on localhost
jp.justpy(app)