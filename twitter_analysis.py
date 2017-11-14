import plotly.plotly as py
import plotly.graph_objs as go
import plotly

import collections
import pymongo
from pymongo import MongoClient
client = MongoClient()
DataProject = client.DataProject
import collections
import pymongo
from pymongo import MongoClient

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pylab import figure, axes, pie, title, show
import datetime as dt

def twitter_analysis():
    date = []
    hamon_pos = []
    hamon_neg = []
    macron_pos = []
    macron_neg = []
    fillon_pos = []
    fillon_neg = []
    lepen_pos = []
    lepen_neg = []
    melen_pos = []
    melen_neg = []
    for i in DataProject.twitter.find():
        date.append(i['Date'])
        hamon_pos.append(i['tweets']['Benoit Hamon']['Positive Tweets'])
        hamon_neg.append(i['tweets']['Benoit Hamon']['Negative Tweets'])
        macron_pos.append(i['tweets']['Emmanuel Macron']['Positive Tweets'])
        macron_neg.append(i['tweets']['Emmanuel Macron']['Negative Tweets'])
        fillon_pos.append(i['tweets']['François Fillon']['Positive Tweets'])
        fillon_neg.append(i['tweets']['François Fillon']['Negative Tweets'])
        lepen_pos.append(i['tweets']['Marine Le Pen']['Positive Tweets'])
        lepen_neg.append(i['tweets']['Marine Le Pen']['Negative Tweets'])
        melen_pos.append(i['tweets']['Jean-Luc Mélenchon']['Positive Tweets'])
        melen_neg.append(i['tweets']['Jean-Luc Mélenchon']['Negative Tweets'])

    hamon_all = [x + y for x, y in zip(hamon_neg, hamon_pos)]
    macron_all = [x + y for x, y in zip(macron_neg, macron_pos)]
    fillon_all = [x + y for x, y in zip(fillon_neg, fillon_pos)]
    lepen_all = [x + y for x, y in zip(lepen_neg, lepen_pos)]
    melen_all = [x + y for x, y in zip(melen_neg, melen_pos)]
    x = [dt.datetime.strptime(d, '%Y,%m,%d').date() for d in date]

    return[hamon_all, macron_all, fillon_all, lepen_all, melen_all, x, date, hamon_pos, hamon_neg,macron_pos, macron_neg,fillon_pos,fillon_neg,lepen_pos, lepen_neg, melen_pos,melen_neg]

def graph_twitter_all_tweets_candidates():

    hamon_all, macron_all, fillon_all, lepen_all, melen_all, x, date, hamon_pos, hamon_neg,macron_pos, macron_neg,fillon_pos,fillon_neg,lepen_pos, lepen_neg, melen_pos,melen_neg = twitter_analysis()
    
    data_1 = go.Scatter(
        x = x,
        y= fillon_all,
        mode = 'lines',
        name = 'Fillon'
        )

    data_2 = go.Scatter(
        x = x,
        y= macron_all,
        mode = 'lines',
        name = 'Macron'
        )

    data_3 = go.Scatter(
        x = x,
        y= lepen_all,
        mode = 'lines',
        name = 'Le Pen'
        )

    data_4 = go.Scatter(
        x = x,
        y= melen_all,
        mode = 'lines',
        name = 'Melenchon'
        )

    data_5 = go.Scatter(
        x = x,
        y= hamon_all,
        mode = 'lines',
        name = 'Hamon'
        )

    layout = go.Layout(
        title = 'All tweets for each candidate',
        xaxis = dict(title='date'),
        yaxis = dict(title = 'percentage of tweets')
        )

    data = [data_1, data_2, data_3, data_4, data_5]
    fig = go.Figure(data=data, layout=layout)
    return plotly.offline.plot(fig,filename='templates/all_tweets_candidates.html',auto_open=False)   

def graph_twitter_neg_tweets():

    hamon_all, macron_all, fillon_all, lepen_all, melen_all, x, date, hamon_pos, hamon_neg,macron_pos, macron_neg,fillon_pos,fillon_neg,lepen_pos, lepen_neg, melen_pos,melen_neg = twitter_analysis()
    
    data_1 = go.Scatter(
        x = x,
        y= fillon_neg,
        mode = 'lines',
        name = 'Fillon'
        )

    data_2 = go.Scatter(
        x = x,
        y= macron_neg,
        mode = 'lines',
        name = 'Macron'
        )

    data_3 = go.Scatter(
        x = x,
        y= lepen_neg,
        mode = 'lines',
        name = 'Le Pen'
        )

    data_4 = go.Scatter(
        x = x,
        y= melen_neg,
        mode = 'lines',
        name = 'Melenchon'
        )

    data_5 = go.Scatter(
        x = x,
        y= hamon_neg,
        mode = 'lines',
        name = 'Hamon'
        )

    layout = go.Layout(
        title = 'Negative tweets for each candidate',
        xaxis = dict(title='date'),
        yaxis = dict(title = 'percentage of tweets')
        )

    data = [data_1, data_2, data_3, data_4, data_5]
    fig = go.Figure(data=data, layout=layout)
    return plotly.offline.plot(fig,filename='templates/negative_tweets.html',auto_open=False)

def graph_twitter_pos_tweets():

    hamon_all, macron_all, fillon_all, lepen_all, melen_all, x, date, hamon_pos, hamon_neg,macron_pos, macron_neg,fillon_pos,fillon_neg,lepen_pos, lepen_neg, melen_pos,melen_neg = twitter_analysis()
    
    data_1 = go.Scatter(
        x = x,
        y= fillon_pos,
        mode = 'lines',
        name = 'Fillon'
        )

    data_2 = go.Scatter(
        x = x,
        y= macron_pos,
        mode = 'lines',
        name = 'Macron'
        )

    data_3 = go.Scatter(
        x = x,
        y= lepen_pos,
        mode = 'lines',
        name = 'Le Pen'
        )

    data_4 = go.Scatter(
        x = x,
        y= melen_pos,
        mode = 'lines',
        name = 'Melenchon'
        )

    data_5 = go.Scatter(
        x = x,
        y= hamon_pos,
        mode = 'lines',
        name = 'Hamon'
        )

    layout = go.Layout(
        title = 'Positive tweets  for each candidate',
        xaxis = dict(title='date'),
        yaxis = dict(title = 'percentage of tweets')
        )

    data = [data_1, data_2, data_3, data_4, data_5]
    fig = go.Figure(data=data, layout=layout)
    return plotly.offline.plot(fig,filename='templates/positive_tweets.html',auto_open=False)   

def graph_twitter_pos_neg_tweets():

    hamon_all, macron_all, fillon_all, lepen_all, melen_all, x, date, hamon_pos, hamon_neg,macron_pos, macron_neg,fillon_pos,fillon_neg,lepen_pos, lepen_neg, melen_pos,melen_neg = twitter_analysis()
    
    hamon_ratio =[y-x for x, y in zip(hamon_neg, hamon_pos)]  
    macron_ratio=[y-x for x, y in zip(macron_neg,macron_pos)]  
    fillon_ratio=[y-x for x, y in zip(fillon_neg, fillon_pos)]  
    lepen_ratio=[y-x for x, y in zip(lepen_neg, lepen_pos)]  
    melen_ratio=[y-x for x, y in zip(melen_neg, melen_pos)]
    
    data_1 = go.Scatter(
        x = x,
        y= fillon_ratio,
        mode = 'lines',
        name = 'Fillon'
        )

    data_2 = go.Scatter(
        x = x,
        y= macron_ratio,
        mode = 'lines',
        name = 'Macron'
        )

    data_3 = go.Scatter(
        x = x,
        y= lepen_ratio,
        mode = 'lines',
        name = 'Le Pen'
        )

    data_4 = go.Scatter(
        x = x,
        y= melen_ratio,
        mode = 'lines',
        name = 'Melenchon'
        )

    data_5 = go.Scatter(
        x = x,
        y= hamon_ratio,
        mode = 'lines',
        name = 'Hamon'
        )

    layout = go.Layout(
        title = 'Difference between positive and negative tweets for each candidate',
        xaxis = dict(title='date'),
        yaxis = dict(title = 'percentage of tweets')
        )

    data = [data_1, data_2, data_3, data_4, data_5]
    fig = go.Figure(data=data, layout=layout)
    return plotly.offline.plot(fig,filename='templates/pos_neg_tweets.html',auto_open=False)   

def graph_twitter_all_tweets():

    hamon_all, macron_all, fillon_all, lepen_all, melen_all, x, date, hamon_pos, hamon_neg,macron_pos, macron_neg,fillon_pos,fillon_neg,lepen_pos, lepen_neg, melen_pos,melen_neg = twitter_analysis()
    all_tt=[a+b+c+d+e for a,b,c,d,e in zip(hamon_all, fillon_all, lepen_all, macron_all, melen_all)]

    data_1 = go.Scatter(
        x = x,
        y= all_tt,
        mode = 'lines',
        name = 'Fillon'
        )


    layout = go.Layout(
        title = 'Total number of tweets',
        xaxis = dict(title='date'),
        yaxis = dict(title = 'percentage of tweets')
        )

    data = [data_1]
    fig = go.Figure(data=data, layout=layout)
    return plotly.offline.plot(fig,filename='templates/total_number_tweets.html',auto_open=False)
