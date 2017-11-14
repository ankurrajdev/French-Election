import os
import sys
from flask import Flask, request, session, g, redirect, url_for, abort, render_template


from flask_wtf import FlaskForm
from wtforms.fields import SelectMultipleField, SelectField
from flask import Flask, render_template
#from datetime import date
#import time
#import gmplot
#import pandas

#from nltk.tokenize import sent_tokenize
#from ClassyFire import *
#from twitter_analysis import *
#from party_cand_twitter import *


app = Flask(__name__)

app.secret_key = 'A0Zr98slkjdf984jnflskj_sdkfjhT'

class Candidate_or_Media(FlaskForm):
	c_or_m = [('candidate', 'Per candidate'), ('media', 'Per media')]
	C_M = SelectField('Data Attributes', choices=c_or_m)

class SimpleForm(FlaskForm):
    files = [('macron', 'Macron'), ('fillon', 'Fillon'), ('lepen', 'Le Pen')]
    example = SelectMultipleField('Label', choices=files)

def panel1():
	filename1 = graph_per_media()[0]
	filename2 = graph_per_candidate()[0]
	return [filename1, filename2]

def panel2():
	filename1 = twitter()[3]
	filename2 = twitter()[4]
	return [filename1, filename2]

def panel3():
	filename1 = sentimental_analysis()[0]
	filename2 = sentimental_analysis()[1]
	return [filename1, filename2]


def panel4():
	filename1 = twitter()[5]
	filename2 = twitter_party()[3]
	return [filename1, filename2]

def graph_per_media():
	#graph_media('LeFigaro')
	filename1 = 'number_articles_media_{}.html'.format('LeFigaro')
	#graph_media('LeMonde')
	filename2 = 'number_articles_media_{}.html'.format('LeMonde')
	#graph_media('France24')
	filename3 = 'number_articles_media_{}.html'.format('France24')
	return [filename1, filename2, filename3]

def graph_per_candidate():
	#graph_candidate('Le Pen')
	filename1 = 'number_articles_candidate_{}.html'.format('Le Pen')
	#graph_candidate('Fillon')
	filename2 = 'number_articles_candidate_{}.html'.format('Fillon')
	#graph_candidate('Macron')
	filename3 = 'number_articles_candidate_{}.html'.format('Macron')
	#graph_candidate('Hamon')
	filename4 = 'number_articles_candidate_{}.html'.format('Hamon')
	#graph_candidate('Melenchon')
	filename5 = 'number_articles_candidate_{}.html'.format('Melenchon')
	return [filename1, filename2, filename3, filename4, filename5]

def twitter():
	#graph_total()
	filename1 = 'number_articles_total.html'
	#graph_twitter_all_tweets()
	filename2 = 'total_number_tweets.html'
	#graph_twitter_all_tweets_candidates()
	filename3 = 'all_tweets_candidates.html'
	#graph_twitter_pos_tweets()
	filename4 = 'positive_tweets.html'
	#graph_twitter_neg_tweets()
	filename5 = 'negative_tweets.html'
	#graph_twitter_pos_neg_tweets()
	filename6 = 'pos_neg_tweets.html'
	return [filename1, filename2, filename3, filename4, filename5, filename6]

def sentimental_analysis():
	filename1 = url_for('static', filename = 'graphs/fillon.png')
	filename2 = 'fillon_dist.html'
	filename3 = 'macron_dist.html'
	filename4 = 'lepen_dist.html'
	filename5 = 'hamon_dist.html'
	filename6 = url_for('static', filename = 'graphs/hamon.png')
	filename7 = url_for('static', filename = 'graphs/lepen.png')
	filename8 = url_for('static', filename = 'graphs/macron.png')
	return [filename1, filename2, filename3, filename4, filename5, filename6, filename7, filename8]

def twitter_party():
	#graph_twitter_all_tweets_party()
	filename1 = 'all_tweets_party.html'
	#graph_twitter_pos_tweets_party()
	filename2 = 'tweets_party_pos.html'
	#graph_twitter_neg_tweets_party()
	filename3 = 'tweets_party_neg.html'
	#graph_twitter_pos_neg_tweets_party()
	filename4 = 'tweets_party_pos_neg.html'
	return [filename1, filename2, filename3, filename4]


def get_homepage_links():
	return 	[	{"href": url_for('home'), "label":"Home" },
				{"href": url_for('analysis'), "label":"Analysis"},
				{"href": url_for('team'), "label":"Team"},
				{"href": url_for('references'), "label":"References"},
			]

def analysis_link():
	return 	[	{"href": url_for('analysis_1'), "label":"Media Coverage" },
				{"href": url_for('analysis_2'), "label":"Public Opinion"},
				{"href": url_for('analysis_3'), "label":"Speech Analysis"},
				{"href": url_for('analysis_4'), "label":"Candidate vs Party"},
			]

@app.route("/")
def home():
	return render_template('home.html', contenu1=panel1(), contenu2=panel2(), contenu3=panel3(), contenu4 = panel4(), links=get_homepage_links(), analysis_links=analysis_link())

@app.route("/team", methods=['GET','POST'])
def team():
	return render_template('team.html', links=get_homepage_links())

@app.route("/references", methods=['GET','POST'])
def references():
	return render_template('references.html', links=get_homepage_links())

@app.route("/analysis/", methods=['GET','POST'])
def analysis():
	return render_template('analysis.html', links=get_homepage_links(), analysis_links=analysis_link())

@app.route("/analysis/analysis_1", methods=['GET','POST'])
def analysis_1():
	form = Candidate_or_Media()
	
	if form.validate_on_submit():
		if request.form.get('C_M') == 'media':
			return render_template('analysis_1.html', form=form, choice='media', picture=graph_per_media(), links=get_homepage_links(), analysis_links=analysis_link())
		
		if request.form.get('C_M') == 'candidate':
			return render_template('analysis_1.html', form=form, choice='candidate', picture=graph_per_candidate(), links=get_homepage_links(), analysis_links=analysis_link() )
	
	return render_template('analysis_1.html', links=get_homepage_links(), analysis_links=analysis_link(), form=form)

@app.route("/analysis/analysis_2", methods=['GET','POST'])
def analysis_2():
	return render_template('analysis_2.html', picture= twitter(), picture1 = graph_per_candidate(), links=get_homepage_links(), analysis_links=analysis_link())

@app.route("/analysis/analysis_3", methods=['GET','POST'])
def analysis_3():
	return render_template('analysis_3.html', picture = sentimental_analysis(), links=get_homepage_links(), analysis_links=analysis_link())

@app.route("/analysis/analysis_4", methods=['GET','POST'])
def analysis_4():
	return render_template('analysis_4.html', picture2 = twitter(),picture1 = twitter_party(), links=get_homepage_links(), analysis_links=analysis_link())

if __name__ == '__main__':
   app.run() 
