from datetime import datetime as dt
from pytz import utc
import justpy as jp
import pandas

df = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])

df["Day"] = df["Timestamp"].dt.date
day_avg = df.groupby(["Day"]).mean()
day_cnt = df.groupby(["Day"]).count()

df["Week"] = df["Timestamp"].dt.strftime("%Y-%U")
week_avg = df.groupby(["Week"]).mean()
week_cnt = df.groupby(["Week"]).count()

df["Month"] = df["Timestamp"].dt.strftime("%Y-%m")
mon_avg = df.groupby(["Month"]).mean()
mon_cnt = df.groupby(["Month"]).count()

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

    h1 = jp.QDiv(a=wp, text="Analysis Of Course Reviews Pt1", classes="text-h3 text-weight-bolder text-center q-pa-md")
    h2 = jp.QDiv(a=wp, text="These graphs plot the Ratings of courses across certain timelines and intervals",
    classes="text-h5 text-weight-bolder text-center q-pa-md")

    #Highchart (Spline) for average ratings by day
    hc1 = jp.HighCharts(a=wp, options=spline_chart_day_avg_def)
    hc1.options.xAxis.categories = list(day_avg.index)
    hc1.options.series[0].data = list(day_avg["Rating"])

    #Highchart (Spline) for number of ratings by day
    hc2 = jp.HighCharts(a=wp, options=spline_chart_day_cnt_def)
    hc2.options.xAxis.categories = list(day_cnt.index)
    hc2.options.series[0].data = list(day_cnt["Rating"])

    #Highchart (Spline) for average ratings by week
    hc3 = jp.HighCharts(a=wp, options=spline_chart_week_avg_def)
    hc3.options.xAxis.categories = list(week_avg.index)
    hc3.options.series[0].data = list(week_avg["Rating"])

    #Highchart (Spline) for number of ratings by week
    hc4 = jp.HighCharts(a=wp, options=spline_chart_week_cnt_def)
    hc4.options.xAxis.categories = list(week_cnt.index)
    hc4.options.series[0].data = list(week_cnt["Rating"])

    #Highchart (Spline) for average ratings by month
    hc5 = jp.HighCharts(a=wp, options=spline_chart_month_avg_def)
    hc5.options.xAxis.categories = list(mon_avg.index)
    hc5.options.series[0].data = list(mon_avg["Rating"])

    #Highchart (Spline) for number of ratings by month
    hc6 = jp.HighCharts(a=wp, options=spline_chart_month_cnt_def)
    hc6.options.xAxis.categories = list(mon_cnt.index)
    hc6.options.series[0].data = list(mon_cnt["Rating"])

    return wp

jp.justpy(app)