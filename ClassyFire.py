import plotly.plotly as py
import plotly.graph_objs as go
import plotly
from pymongo import MongoClient
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import re
import datetime as dt

#Connexion Server
client = MongoClient('127.0.0.1',27017)
db = client.DataProject
path = "bags_of_words/"
######### Creating Bag of words ########################
politicians = ["Arthaud","Fillon","Hamon","Hollande","Sarkozy","Le Pen","Macron","Melenchon","Poutou","Valls","Cheminade","Aignan","Asselineau","Lassalle"]
bag_of_politicians = dict()
for politician in politicians:
    bag_path = path + politician + ".txt"
    with open(bag_path,'r', encoding='ISO-8859-1') as f:
        bag_politician = f.read().split(',')
        bag_of_politicians[politician] = bag_politician
########################################################
def toDate(date):
    return dt.datetime.strptime(date, "%Y,%m,%d")

def toString(date):
    return dt.datetime.strftime(date, "%Y,%m,%d")
########################################################
def classify(text):
    #Initializing
    pts_politicians =pd.Series(0,index=politicians)
    for politician in politicians:
        pts_politician = 0
        for word in bag_of_politicians[politician]:
            pts_politician += len(re.findall(word, text.lower()))
            #pts_politician += sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(word), text.lower()))
        pts_politicians[politician] = pts_politician
    #Normalizating to a probability vector
    psum =  pts_politicians.sum()
    proba = pts_politicians
    if psum !=0:
        proba /=psum
    return proba
#######################################
def classy_fire(article,alpha = 0.6):
    ptitle = classify(article['Title'])
    pcontent  =  classify(article['Content'])
    return alpha*ptitle + (1-alpha)*pcontent
#########################################
def number_of_articles_date(source,date,threshold=0.2):
    #Init
    number_of_articles = pd.Series(0,index = politicians)
    #Extracting Articles
    articles = list(db.Articles.find({'Source':source,'Date':date},{'Title':1,'Content':1,'_id':0}))
    for ID in range(len(articles)):
               if (classy_fire(articles[ID]).max()) > threshold:
                   number_of_articles.ix[classy_fire(articles[ID]).argmax()] += 1
    return number_of_articles
########################################################
def number_of_articles(source,dateBegin,dateEnd,Candidates=["Fillon","Macron","Le Pen","Melenchon","Hamon"]):
    dateBegin = toDate(dateBegin)
    dateEnd = toDate(dateEnd)
    delta = dateEnd-dateBegin
    df = pd.DataFrame()
    for i in range(delta.days + 1):
        date = toString(dateBegin + dt.timedelta(days=i))
        df[date]=number_of_articles_date(source,date)
    return df.transpose()[Candidates]
########################################################
def article_candidate(dateBegin,dateEnd,Candidate,Sources=["LeMonde","LeFigaro","France24"]):
    dateBegin = toDate(dateBegin)
    dateEnd = toDate(dateEnd)
    delta = dateEnd-dateBegin
    dflist = list()
    for i in range(delta.days + 1):
        date = toString(dateBegin + dt.timedelta(days=i))
        article_day = dict.fromkeys(Sources)
        article_day['date'] = date
        for source in Sources:
            article_day[source]= number_of_articles_date(source,date)[Candidate]
        dflist.append(article_day)
        df = pd.DataFrame(dflist).set_index('date')
    return df

def graph_media(source, dateBegin='2017,03,28', dateEnd='2017,04,23'):
    df = number_of_articles(source,dateBegin,dateEnd)

    data_1 = go.Scatter(
    	x= [toDate(x) for x in df.index.values],
        y= df['Fillon'],
        mode = 'lines',
        name = 'Fillon'
    	)

    data_2 = go.Scatter(
        x= [toDate(x) for x in df.index.values],
        y= df['Hamon'],
        mode = 'lines',
        name = 'Hamon'
        )

    data_3 = go.Scatter(
        x= [toDate(x) for x in df.index.values],
        y= df['Le Pen'],
        mode = 'lines',
        name = 'Le Pen'
        )

    data_4 = go.Scatter(
        x= [toDate(x) for x in df.index.values],
        y= df['Macron'],
        mode = 'lines',
        name = 'Macron'
        )

    data_5 = go.Scatter(
        x= [toDate(x) for x in df.index.values],
        y= df['Melenchon'],
        mode = 'lines',
        name = 'Melenchon'
        )

    if source == 'LeFigaro':
        name_newspaper = 'le Figaro'
    elif source == 'LeMonde':
        name_newspaper='le Monde'
    elif source == 'France24':
        name_newspaper = 'France 24'

    layout = go.Layout(
        title = 'Number of articles for {}'.format(name_newspaper),
        xaxis = dict(title='Date'),
        yaxis = dict(title = 'Number of Articles')
        )

    data = [data_1, data_2, data_3, data_4, data_5]
    fig = go.Figure(data=data, layout=layout)
    return plotly.offline.plot(fig,filename='templates/number_articles_media_{}.html'.format(source),auto_open=False) 

def graph_candidate(Candidate, dateBegin='2017,03,28', dateEnd='2017,04,23'):
    df = article_candidate(dateBegin,dateEnd,Candidate)
    data_1 = go.Scatter(
        x= [toDate(x) for x in df.index.values],
        y= df['LeMonde'],
        mode = 'lines',
        name = 'Le Monde'
        )

    data_2 = go.Scatter(
        x= [toDate(x) for x in df.index.values],
        y= df['LeFigaro'],
        mode = 'lines',
        name = 'Le Figaro'
        )

    data_3 = go.Scatter(
        x= [toDate(x) for x in df.index.values],
        y= df['France24'],
        mode = 'lines',
        name = 'France 24'
        )

    layout = go.Layout(
        title = 'Number of Articles for {}'.format(Candidate),
        xaxis = dict(title='Date'),
        yaxis = dict(title = 'Number of Articles')
        )

    data = [data_1, data_2, data_3]
    fig = go.Figure(data=data, layout=layout)
    return plotly.offline.plot(fig,filename='templates/number_articles_candidate_{}.html'.format(Candidate),auto_open=False)

def graph_total():

    S = pd.Series()
    df= number_of_articles('LeFigaro',dateBegin='2017,03,28', dateEnd='2017,04,23')
    S = df.sum(axis=1)

    for source in ['LeMonde', 'France24']:
        df = number_of_articles(source,dateBegin='2017,03,28', dateEnd='2017,04,23')
        S+=df.sum(axis=1)
    
    data_1 = go.Scatter(
        x= [toDate(x) for x in df.index.values],
        y= S.values,
        mode = 'lines',
        name = 'Total number'
        )

    layout = go.Layout(
        title = 'Total number of articles written per day',
        xaxis = dict(title='Date'),
        yaxis = dict(title = 'Number of Articles')
        )

    data = [data_1]
    fig = go.Figure(data=data, layout=layout)
    return plotly.offline.plot(fig,filename='templates/number_articles_total.html',auto_open=False)