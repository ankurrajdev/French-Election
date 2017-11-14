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
candidates=['Front National','Les Républicains','En Marche!',
'Parti socialiste','La France Insoumise','François Fillon',
'Marine Le Pen','Emmanuel Macron','Benoit Hamon','Jean-Luc Mélenchon']
#En Marche!
#Les Républicains"
#"Parti socialiste"
#"Front National"
#

def twitter_analysis_party():
    date = []
    front_pos = []
    front_neg = []
    repub_pos = []
    repub_neg = []
    marche_pos = []
    marche_neg = []
    social_pos = []
    social_neg = []
    insoum_pos = []
    insoum_neg = []

    for i in DataProject.twitter.find():
        date.append(i['Date'])
        front_pos.append(i['tweets']['Front National']['Positive Tweets'])
        front_neg.append(i['tweets']['Front National']['Negative Tweets'])
        repub_pos.append(i['tweets']['Les Républicains']['Positive Tweets'])
        repub_neg.append(i['tweets']['Les Républicains']['Negative Tweets'])
        marche_pos.append(i['tweets']['En Marche!']['Positive Tweets'])
        marche_neg.append(i['tweets']['En Marche!']['Negative Tweets'])
        social_pos.append(i['tweets']['Parti socialiste']['Positive Tweets'])
        social_neg.append(i['tweets']['Parti socialiste']['Negative Tweets'])
        insoum_pos.append(i['tweets']['La France Insoumise']['Positive Tweets'])
        insoum_neg.append(i['tweets']['La France Insoumise']['Negative Tweets'])

    front_all = [x + y for x, y in zip(front_neg, front_pos)]
    repub_all = [x + y for x, y in zip(repub_neg, repub_pos)]
    marche_all = [x + y for x, y in zip(marche_neg, marche_pos)]
    social_all = [x + y for x, y in zip(social_neg, social_pos)]
    insoum_all = [x + y for x, y in zip(insoum_neg, insoum_pos)]
    x = [dt.datetime.strptime(d, '%Y,%m,%d').date() for d in date]

    return[front_all, repub_all, marche_all, social_all, insoum_all, x, date, front_pos, front_neg,repub_pos, repub_neg,marche_pos,marche_neg,social_pos, social_neg, insoum_pos,insoum_neg]

def graph_twitter_all_tweets_party():
    front_all, repub_all, marche_all, social_all, insoum_all, x, date, front_pos, front_neg,repub_pos, repub_neg,marche_pos,marche_neg,social_pos, social_neg, insoum_pos,insoum_neg=twitter_analysis_party()
    data_3 = go.Scatter(
        x = x,
        y= front_all,
        mode = 'lines',
        name = 'Front National'
        )

    data_1 = go.Scatter(
        x = x,
        y= repub_all,
        mode = 'lines',
        name = 'Les Républicains'
        )

    data_2 = go.Scatter(
        x = x,
        y= marche_all,
        mode = 'lines',
        name = 'En Marche!'
        )

    data_5 = go.Scatter(
        x = x,
        y= social_all,
        mode = 'lines',
        name = 'Parti socialiste'
        )

    data_4 = go.Scatter(
        x = x,
        y= insoum_all,
        mode = 'lines',
        name = 'La France Insoumise'
        )

    layout = go.Layout(
        title = 'All tweets for each party',
        xaxis = dict(title='date'),
        yaxis = dict(title = 'number of tweets')
        )

    data = [data_1, data_2, data_3, data_4, data_5]
    fig = go.Figure(data=data, layout=layout)
    return plotly.offline.plot(fig,filename='templates/all_tweets_party.html',auto_open=False)   

def graph_twitter_neg_tweets_party():
    front_all, repub_all, marche_all, social_all, insoum_all, x, date, front_pos, front_neg,repub_pos, repub_neg,marche_pos,marche_neg,social_pos, social_neg, insoum_pos,insoum_neg=twitter_analysis_party()
    data_3 = go.Scatter(
        x = x,
        y= front_neg,
        mode = 'lines',
        name = 'Front National'
        )

    data_1 = go.Scatter(
        x = x,
        y= repub_neg,
        mode = 'lines',
        name = 'Les Républicains'
        )

    data_2 = go.Scatter(
        x = x,
        y= marche_neg,
        mode = 'lines',
        name = 'En Marche!'
        )

    data_5 = go.Scatter(
        x = x,
        y= social_neg,
        mode = 'lines',
        name = 'Parti socialiste'
        )

    data_4 = go.Scatter(
        x = x,
        y= insoum_neg,
        mode = 'lines',
        name = 'La France Insoumise'
        )

    layout = go.Layout(
        title = 'Negative tweets for each partys',
        xaxis = dict(title='date'),
        yaxis = dict(title = 'number of tweets')
        )

    data = [data_1, data_2, data_3, data_4, data_5]
    fig = go.Figure(data=data, layout=layout)
    return plotly.offline.plot(fig,filename='templates/tweets_party_neg.html',auto_open=False)   

def graph_twitter_pos_tweets_party():

    front_all, repub_all, marche_all, social_all, insoum_all, x, date, front_pos, front_neg,repub_pos, repub_neg,marche_pos,marche_neg,social_pos, social_neg, insoum_pos,insoum_neg=twitter_analysis_party()
    data_3 = go.Scatter(
        x = x,
        y= front_pos,
        mode = 'lines',
        name = 'Front National'
        )

    data_1 = go.Scatter(
        x = x,
        y= repub_pos,
        mode = 'lines',
        name = 'Les Républicains'
        )

    data_2 = go.Scatter(
        x = x,
        y= marche_pos,
        mode = 'lines',
        name = 'En Marche!'
        )

    data_5 = go.Scatter(
        x = x,
        y= social_pos,
        mode = 'lines',
        name = 'Parti socialiste'
        )

    data_4 = go.Scatter(
        x = x,
        y= insoum_pos,
        mode = 'lines',
        name = 'La France Insoumise'
        )

    layout = go.Layout(
        title = 'Positive tweets for each party',
        xaxis = dict(title='date'),
        yaxis = dict(title = 'number of tweets')
        )

    data = [data_1, data_2, data_3, data_4, data_5]
    fig = go.Figure(data=data, layout=layout)
    return plotly.offline.plot(fig,filename='templates/tweets_party_pos.html',auto_open=False)   

def graph_twitter_pos_neg_tweets_party():
    front_all, repub_all, marche_all, social_all, insoum_all, x, date, front_pos, front_neg,repub_pos, repub_neg,marche_pos,marche_neg,social_pos, social_neg, insoum_pos,insoum_neg=twitter_analysis_party()
    front_ratio =[y-x for x, y in zip(front_neg, front_pos)]  
    marche_ratio=[y-x for x, y in zip(marche_neg,marche_pos)]  
    repub_ratio=[y-x for x, y in zip(repub_neg, repub_pos)]  
    social_ratio=[y-x for x, y in zip(social_neg, social_pos)]  
    insoum_ratio=[y-x for x, y in zip(insoum_neg, insoum_pos)]
    data_3 = go.Scatter(
        x = x,
        y= front_ratio,
        mode = 'lines',
        name = 'Front National'
        )

    data_1 = go.Scatter(
        x = x,
        y= repub_ratio,
        mode = 'lines',
        name = 'Les Républicains'
        )

    data_2 = go.Scatter(
        x = x,
        y= marche_ratio,
        mode = 'lines',
        name = 'En Marche!'
        )

    data_5 = go.Scatter(
        x = x,
        y= social_ratio,
        mode = 'lines',
        name = 'Parti socialiste'
        )

    data_4 = go.Scatter(
        x = x,
        y= insoum_ratio,
        mode = 'lines',
        name = 'La France Insoumise'
        )

    layout = go.Layout(
        title = 'Difference between positive and negative tweets for each party',
        xaxis = dict(title='date'),
        yaxis = dict(title = 'number of tweets')
        )

    data = [data_1, data_2, data_3, data_4, data_5]
    fig = go.Figure(data=data, layout=layout)
    return plotly.offline.plot(fig,filename='templates/tweets_party_pos_neg.html',auto_open=False)   

graph_twitter_pos_tweets_party()
graph_twitter_neg_tweets_party()
graph_twitter_pos_neg_tweets_party()
graph_twitter_all_tweets_party()


