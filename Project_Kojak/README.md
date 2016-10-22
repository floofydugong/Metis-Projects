============
Codename : Kojak
============

> Identifying Potential Trafficking Victims in Classified Ads

![Ominlux Build Status][buildstatus-url]

Performed Naive Bayes Classification on escort ads from Backpage.com to determine potential human trafficking victims, displaying the results using a Flask application.

**Data Source:** 320 hand labeled Backpage.com escort ads

**Model:** I used a Multinomial Naive Bayes model in with the output of a Count Vectorizer as the input to predict whether or not the ad was fradulent.

**Conclusion:** The model was able to predict with 81% accuracy. Althougn this is a great milestone, the data that I scraped and labeled inherently had bias. For future work, I would like to consult law enforcement agencies and NGO's to develop a truth set.

![Ominlux Screenshot](/Project_Kojak/images/OminluxBlurredScreenshot.png)

## Final Project Presentation

Thank you to all those in attendance of Metis' Career Day. Click on the image below to watch my final project presentation.

[![Presentation Link](https://pbs.twimg.com/media/CtAJ13_VMAALFCp.jpg:large)](http://www.youtube.com/watch?v=U72M6iIPerg)

## Release History

* 0.1.0
    * The first release for Metis' Career Day Presentation
* 0.0.1
    * Work in progress

[buildstatus-url]: https://img.shields.io/badge/build-passing-brightgreen.svg