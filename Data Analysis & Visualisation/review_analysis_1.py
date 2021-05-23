#Import Libraries
from datetime import datetime as dt
from pytz import utc
import justpy as jp
import pandas

#Read CSV file containing all reviews and set Timestamp column values to be of date type
df = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])

#Create a column for date and group data by date
df["Day"] = df["Timestamp"].dt.date
day_avg = df.groupby(["Day"]).mean() #find mean values of ratings
day_cnt = df.groupby(["Day"]).count() #find the number of ratings 

#Create a column for week (%Y makes sure that same weeks in different years dont get considered the same)
#Group data by week (%U is for week value)
df["Week"] = df["Timestamp"].dt.strftime("%Y-%U")
week_avg = df.groupby(["Week"]).mean() #find mean values of ratings
week_cnt = df.groupby(["Week"]).count() #find the number of ratings

#Create a column for month (%Y makes sure that same months in different years dont get considered the same)
#Group data by month (%m is for month value)
df["Month"] = df["Timestamp"].dt.strftime("%Y-%m")
mon_avg = df.groupby(["Month"]).mean() #find mean values of ratings
mon_cnt = df.groupby(["Month"]).count() #find the number of ratings 

#Chart for mean value of ratings by day
spline_chart_day_avg_def = '''
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Rating By Date'
    },
    subtitle: {
        text: 'Based on reviews given by 50,000 users'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
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
            rangeDescription: 'Range: 0 to 5.'
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

#Chart for number of ratings by day
spline_chart_day_cnt_def = '''
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Number of Ratings By Date'
    },
    subtitle: {
        text: 'Based on reviews given by 50,000 users'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
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
            text: 'Number of Ratings'
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
        name: 'Number of Ratings',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
'''

#Chart for mean value of ratings by week
spline_chart_week_avg_def = '''
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Rating By Week'
    },
    subtitle: {
        text: 'Based on reviews given by 50,000 users'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Week'
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
            rangeDescription: 'Range: 0 to 5.'
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

#Chart for number of ratings by week
spline_chart_week_cnt_def = '''
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Number of Ratings By Week'
    },
    subtitle: {
        text: 'Based on reviews given by 50,000 users'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Week'
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
            text: 'Number of Ratings'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 5.'
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
        name: 'Number of Ratings',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
'''

#Chart for mean value of ratings by month
spline_chart_month_avg_def = '''
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Rating By Month'
    },
    subtitle: {
        text: 'Based on reviews given by 50,000 users'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Month'
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
            rangeDescription: 'Range: 0 to 5.'
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

#Chart for number of ratings by month
spline_chart_month_cnt_def = '''
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Number of Ratings By Month'
    },
    subtitle: {
        text: 'Based on reviews given by 50,000 users'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Month'
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
            text: 'Number of Ratings'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 5.'
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
        name: 'Number of Ratings',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
'''

def app():
    #Creates a webpage and loads it in dark mode
    wp = jp.QuasarPage(dark=True)

    #Heading and Sub-Heading Tags
    h1 = jp.QDiv(a=wp, text="Analysis Of Course Reviews Pt1", classes="text-h3 text-weight-bolder text-center q-pa-md")
    h2 = jp.QDiv(a=wp, text="These graphs plot the Ratings of courses across certain timelines and intervals", 
    classes="text-h5 text-weight-bolder text-center q-pa-md")

    #Highchart (Spline) for average ratings by day
    hc1 = jp.HighCharts(a=wp, options=spline_chart_day_avg_def)
    #Access the dictionary that contains chart data using hc.options and change title
    #hc.options.title.text = "Average Rating By Day"
    #Change data to be plotted
    hc1.options.xAxis.categories = list(day_avg.index) #Sets the X-Axis value to the index of the day_avg dataframe(date)
    hc1.options.series[0].data = list(day_avg["Rating"]) #Plots the average rating per day against the X-Axis

    #Highchart (Spline) for number of ratings by day
    hc2 = jp.HighCharts(a=wp, options=spline_chart_day_cnt_def)
    #Access the dictionary that contains chart data using hc.options
    hc2.options.xAxis.categories = list(day_cnt.index) #Sets the X-Axis value to the index of the day_cnt dataframe(date)
    hc2.options.series[0].data = list(day_cnt["Rating"]) #Plots the number of ratings per day against the X-Axis

    #Highchart (Spline) for average ratings by week
    hc3 = jp.HighCharts(a=wp, options=spline_chart_week_avg_def)
    #Access the dictionary that contains chart data using hc.options
    hc3.options.xAxis.categories = list(week_avg.index) #Sets the X-Axis value to the index of the week_avg dataframe(week)
    hc3.options.series[0].data = list(week_avg["Rating"]) #Plots the average rating per week against the X-Axis

    #Highchart (Spline) for number of ratings by week
    hc4 = jp.HighCharts(a=wp, options=spline_chart_week_cnt_def)
    #Access the dictionary that contains chart data using hc.options
    hc4.options.xAxis.categories = list(week_cnt.index) #Sets the X-Axis value to the index of the week_cnt dataframe(week)
    hc4.options.series[0].data = list(week_cnt["Rating"]) #Plots the number of ratings per week against the X-Axis

    #Highchart (Spline) for average ratings by month
    hc5 = jp.HighCharts(a=wp, options=spline_chart_month_avg_def)
    #Access the dictionary that contains chart data using hc.options
    hc5.options.xAxis.categories = list(mon_avg.index) #Sets the X-Axis value to the index of the mon_avg dataframe(month)
    hc5.options.series[0].data = list(mon_avg["Rating"]) #Plots the average rating per month against the X-Axis

    #Highchart (Spline) for number of ratings by month
    hc6 = jp.HighCharts(a=wp, options=spline_chart_month_cnt_def)
    #Access the dictionary that contains chart data using hc.options
    hc6.options.xAxis.categories = list(mon_cnt.index) #Sets the X-Axis value to the index of the mon_cnt dataframe(month)
    hc6.options.series[0].data = list(mon_cnt["Rating"]) #Plots the number of ratings per month against the X-Axis

    #Returns the webpage
    return wp

#Expects a function which returns a webpage and runs it to load webpage on localhost
jp.justpy(app)