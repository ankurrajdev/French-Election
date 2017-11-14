# coding=<utf-8>
def list_file(filename):
    with open(filename) as f:
        content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content] 
# divide the words into positive and negative:
    categories =['Tranquillité (151)','Surprise (82)','Joie (148)','Tristesse (117)', 'Dégoût (9)','Colère (142)', 'Fureur (8)', 'Peur (82)', 'Terreur (9)','Coupure avec ses émotions (137)']
    # english translation: 'Tranquility', 'Surprise', 'Sadness', 'Disgust','Anger', 'Fury', 'Fear', 'Terror', 
    dic={}
    positive_words=[]
    negative_words=[]
    for cat in categories:
        dic[cat]=content.index(cat)
# can adjust
    for word in content:
        positive_words.extend(content[dic['Tranquillité (151)']+1: dic['Surprise (82)']])
        positive_words.extend(content[dic['Joie (148)']+1: dic['Tristesse (117)']])
        negative_words.extend(content[dic['Tristesse (117)']+1: dic['Dégoût (9)']])
        negative_words.extend(content[dic['Dégoût (9)']+1: dic['Colère (142)']])
        negative_words.extend(content[dic['Colère (142)']+1: dic['Fureur (8)']])
        negative_words.extend(content[dic['Fureur (8)']+1: dic['Peur (82)']])
        negative_words.extend(content[dic['Peur (82)']+1: dic['Terreur (9)']])
        negative_words.extend(content[dic['Terreur (9)']+1: dic['Coupure avec ses émotions (137)']])
        negative_words.extend(content[dic['Coupure avec ses émotions (137)']+1:])
        return(negative_words,positive_words)
list_file('34_new.txt')
negative_words=list_file('34_new.txt')[0]
positive_words=list_file('34_new.txt')[1] 

def remove_punctuation(word):
    symbol='. , : ! ? << >> < > ( ) / « »'
    symbols=symbol.split()
    if len(word)>=2: # too short words
        if word[0] in symbols:
            word=word[1:]
        if word[-1] in symbols:
            word=word[:-1]
    else:
        word=''
    return word

def remove_punc_short(Text):
    text=''
    Words=[]
    words=Text.split()
    if len(word)>=3: # too short words
        if word[0] in symbols:
            word=word[1:]
        if word[-1] in symbols:
            word=word[:-1]
    else:
        word=''
        
        Words.append(word)
        text=" ".join(Words) 
    return text
    
    
def remove_n(Text):
    text=''
    Words=[]
    words=Text.split()
    for word in words:
        if len(word) >=2 and word[0:1]=='\n':
            word=word[2:]
        else:
            word=word
        
        Words.append(word)
        text=" ".join(Words) 
    return text

    #Get debate texts
debate_texts = ['Fillon.txt','Hamon.txt','LePen.txt','Macron.txt']
for text in debate_texts:
    with open(text,'r') as f:
        data = f.read()
    data=remove_n(data)
    data=data.lower()
    words = data.split()
    cpos=0
    cneg=0
    for word in words:
        word = remove_punctuation(word)
        if word in positive_words:
            cpos += 1
        if word in negative_words:
            cneg += 1
    total_words = len(words)
    ppct = cpos/total_words * 100
    npct = cneg/total_words * 100
    pos_neg_ratio = cpos/cneg
    print("%-10s\t%7d\t%2.2f\t%2.2f\t%2.2f"%(text,len(words),ppct,npct,pos_neg_ratio))

from nltk.tokenize import sent_tokenize
import matplotlib.pyplot as plt

#%matplotlib inline
import nltk 
def get_pos_neg_ratios(text):
    text=remove_n(text)
    sents = sent_tokenize(text)
    pos_neg_ratio_list = list()
    cumpos=0
    cumneg=0
    for sent in sents:
        for word in sent.split():
            if word in positive_words:
                cumpos+=1
            if word in negative_words:
                cumneg+=1
        try:
            pos_neg_ratio_list.append(cumpos/cumneg)
        except:
            pos_neg_ratio_list.append(0)
    return pos_neg_ratio_list

    #First let's read all the texts
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pylab import figure, axes, pie, title, show
debate_texts = ['Fillon.txt','Hamon.txt','LePen.txt','Macron.txt']
all_texts = dict()
for text in debate_texts:
    with open(text,'r') as f:
        data = f.read()
        all_texts[text] = data

#Set up side by side plots
COL_NUM = 2
ROW_NUM = 2
fig, axes = plt.subplots(ROW_NUM, COL_NUM, figsize=(12,12))    
for i in range(len(debate_texts)):
    text = all_texts[debate_texts[i]]
    disp_list = get_pos_neg_ratios(text)
    ax = axes[i//2, i%2]
    ax.set_title(debate_texts[i])
    ax.plot(disp_list)
    ax.axis('on')

#plt.show()
plt.savefig('style.png')
#
#
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
#%matplotlib inline

#First let's collect all the text into strings
debate_texts = ['Fillon.txt','Hamon.txt','LePen.txt','Macron.txt']
all_texts = dict()
for text in debate_texts:
    with open(text,'r') as f:
        data = f.read()
        all_texts[text] = data

#Remove unwanted words
DELETE_WORDS = ['fillon','hamon','lepen','macron', 'marine', 'françois','qu']
def remove_words(text_string,DELETE_WORDS=DELETE_WORDS):
    for word in DELETE_WORDS:
        text_string = text_string.replace(word,' ')
    return text_string

#Remove short words
def remove_short_words(text_string,min_length = 5):
    word_list = text_string.split()
    new_list=[]
    for word in word_list:
        if len(word) > min_length:
            #text_string = text_string.replace(' '+word,' ',1)
            #word = word.replace(word,'')
            new_list.append(word)
            text_string = ' '.join(new_list)   
    return text_string

#Set up side by side clouds
COL_NUM = 2
ROW_NUM = 2
fig, axes = plt.subplots(ROW_NUM, COL_NUM, figsize=(12,12))
debate_texts = ['Fillon.txt','Hamon.txt','LePen.txt','Macron.txt']
for i in range(0,len(debate_texts)):
    text_string = remove_n(all_texts[debate_texts[i]])
    text_string = remove_words(all_texts[debate_texts[i]])
    text_string = remove_short_words(text_string,5)
    ax = axes[i//2, i%2]
    ax.set_title(debate_texts[i])
    wordcloud = WordCloud(stopwords=STOPWORDS,background_color='white',width=1200,height=1000,max_words=20).generate(text_string)
    ax.imshow(wordcloud)
    ax.axis('off')
plt.savefig('wordcloud.png')