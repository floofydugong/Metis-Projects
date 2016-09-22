# Flask Related
from flask import render_template, request
from flask_wtf import Form
from wtforms import fields
from wtforms.validators import Required
from . import app

# General Imports
import re
import time
from time import sleep
from pprint import pprint
from datetime import datetime
import pickle
import glob
import string

# Data processing/Visuals
import numpy as np
import pandas as pd

# Scraping
import requests
from bs4 import BeautifulSoup

reg_ex = re.compile('\d{3}[-.\s]*\d{3}[-.\s]*\d{4}')

model = pickle.load(open( "app/allen.pkl", "rb" ))
ngram_and_rank = pickle.load( open( "app/ngram_and_rank.pkl", "rb" ) )

class PredictForm(Form):

    submit = fields.SubmitField('Submit')

def get_pic_html(url):
    list_of_pic_urls = []
    html_code_for_pics = []
    string_of_code = ""
    try:
        page_url = url
        response = requests.get(page_url)
        page = response.text
        soup = BeautifulSoup(page, 'lxml')

        # Post Pictures
        find_pics = soup.find("ul", id="viewAdPhotoLayout")
        li = find_pics.select("li > a > img")
        for link in li:
            list_of_pic_urls.append(link.get('src'))
    except:
        return ("failed")

    list_of_pic_urls = list(set(list_of_pic_urls))

    for url in list_of_pic_urls:
        string_of_code = "<a class=\"carousel-item\" href=\"http://localhost:9000/\"><img src =\"" + url + "\"></a>"
        html_code_for_pics.append(string_of_code)
    return "<div class=\"carousel\">" +  ("".join(html_code_for_pics)) + "</div>"

def get_ad_info(url):
    try:
        all_details = []
        page_url = url
        response = requests.get(page_url)
        page = response.text
        soup = BeautifulSoup(page, 'lxml')

        # Post Title
        find_title = soup.find('title')
        title = find_title.text
        title = title.replace(' - San Francisco escorts - backpage.com',"")

        # Post Date
        find_post_date = soup.find("div", class_="adInfo")
        date = find_post_date.text.strip()
        date = date.replace("Posted:\r\n    ","")

        # Post Description
        # find_desc = soup.find("div",class_="postingBody")
        # desc = find_desc.text.strip()
        find_desc = soup.find("div",class_="postingBody")
        desc = str(find_desc).strip()
        desc = desc.replace("<br/>","<br>")
        desc = desc.replace("<b>","")
        desc = desc.replace("</b>","")
        desc_clean = find_desc.text
        # desc_clean = desc_clean.replace("\n","<br/>")

        # desc_clean = desc_clean.replace(r'\d{9,10}'," ")

        # Poster's Age
        find_age = soup.find("div",class_="posting").find(class_="metaInfoDisplay")
        age = find_age.text.strip()
        age = age.replace("Poster's age: ","")

        # Poster's Location
        find_location = soup.find("div",class_="posting").find(style="padding-left:2em;")
        location = find_location.text.strip()
        location = location.replace("• Location:\r\n        ","")

        # all_details.append([URL,title])
        all_details.append(url)
        all_details.append(title)
        all_details.append(date)
        all_details.append(desc)
        all_details.append(age)
        all_details.append(location)
        all_details.append(desc_clean)

        prediction = model.predict([all_details[6]])
        prediction_prob = model.predict_proba([all_details[6]])

        prediction = "<span style='color:red'>Deceptiveness</span>"
        prediction_prob_dec = str('{0:.2f}'.format((prediction_prob[0][0]) * 100)) + '%'
        prediction_prob_js = float(prediction_prob[0][0])


        all_details.append(prediction)
        all_details.append(prediction_prob_dec)
        all_details.append(prediction_prob_js)

        return all_details
    except:
        return "Failed"
        print("Failed for:", page_url)

def colorize(rank):
    if rank <= 10:
        return('token positive_token_1')
    elif rank <= 20 and rank > 10:
        return('token positive_token_2')
    elif rank <= 30 and rank > 20:
        return('token positive_token_3')
    elif rank <= 40 and rank > 30:
        return('token positive_token_4')

def colorize_desc(desc):

    final_sentence = []
    re_sent_split = re.findall(r"[\w]+|[!#$%&'()*+,-./:;<=>?@\s\\^_`{|}~]", desc)

    for i in re_sent_split:

        if i.lower() in ngram_and_rank and ngram_and_rank[i.lower()][0] != 'common':
            i = "<div class='" + ngram_and_rank[i.lower()][0]+ " tooltip='" + "data-tooltip='" + "Deceit Rank : " + str(ngram_and_rank[i.lower()][1]) + "/50" + "'>" + i + "</div>"
            final_sentence.append(i)
        else:
            final_sentence.append(i)
    return "".join(final_sentence)

@app.route('/', methods=('GET', 'POST'))
def index():
    form = PredictForm()
    url = ""
    data_tx_box_2=""
    desc_clean = ""
    color_desc = ""
    picture_html = ""

    if form.validate_on_submit():
        url=request.form.getlist('backpage_url')[0]
        if url:
            try:
                data_tx_box_2 = get_ad_info(url)
                picture_html = get_pic_html(url)
                color_desc = colorize_desc(data_tx_box_2[6])
            except:
                pass
        else:
            pass
    else:
        print("Errors")
        print(form.errors)

    return render_template('index.html', form=form, prediction = data_tx_box_2, text_clean=desc_clean, colored_text = color_desc, carousel_code=picture_html)


