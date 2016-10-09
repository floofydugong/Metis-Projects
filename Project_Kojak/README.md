============
Kojak
============

> Identifying Potential Trafficking Victims in Classified Ads

[![Build Status]][buildstatus-url]]()

Performed Naive Bayes Classification on escort ads from Backpage.com to determine potential human trafficking victims, displaying the results using a Flask application.

**Data Source:** 320 hand labeled Backpage.com escort ads

**Model:** I used a Multinomial Naive Bayes model in with the output of a Count Vectorizer as the input to predict whether or not the ad was fradulent.

**Conclusion:** The model was able to predict with 81% accuracy. Althougn this is a great milestone, the data that I scraped and labeled inherently had bias. For future work, I would like to consult law enforcement agencies and NGO's to develop a truth set.

![Ominlux Screenshot](/Project_Kojak/images/OminluxBlurredScreenshot.png)

## Application Demo

Link to Screencast and Career Day Presentation

## Release History

* 0.1.0
    * The first proper release for Metis' Career Day Presentation
* 0.0.1
    * Work in progress

[buildstatus-url] : https://img.shields.io/badge/build-passing-brightgreen.svg