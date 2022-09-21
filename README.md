# PBP Assignment 2: Introduction to Django and Models View Template (MVT) Concept

## Heroku Application
[HTML](https://raaassignment2.herokuapp.com/mywatchlist/html) ---
[XML](https://raaassignment2.herokuapp.com/mywatchlist/xml) ---
[JSON](https://raaassignment2.herokuapp.com/mywatchlist/json)

## Difference between HTML, XML, JSON
Generally, we use these data format each for a different reason. HTML mainly used for its customizability making it reader-friendly for formats. While XML is mainly used for its structure that is consistent even when displaying tons and tons of data. But, with the rise of web application, that is more of dynamic websites, JSON is used for structuring information that is easily and fluently interact with its peers languganges.

## Why we need the data delivery in implementing a platform
Data delivery is used in a way that makes it easier to display data to various individual or teams that is working on said projects. With an ease of access and ease of readiblity, they can work on the project as efficiently as possible.

## Way to implement things

### Create a new app
By using the command python manage.py startapp mywatchlist and the app to the project django setting.
<br/>

### Add watchlist URL
Add the path to the project django
>url.py.
<br/>

### Create models
From the app folder, I add the fields requirements to the class models.py
<br/>

### Add data
Add data to mywatchlist/fixtures/initial_mywatchlist_data.json and migrate + loaddata the file
<br/>

### Implement feature to present data with different formats
Add a new function to views.py and route it to urls.py
<br/>

## Postman Screenshots
[HTML](https://cdn.discordapp.com/attachments/938087203547013131/1022280339479072798/unknown.png) ---
[XML](https://cdn.discordapp.com/attachments/938087203547013131/1022280397121388605/unknown.png) ---
[JSON](https://cdn.discordapp.com/attachments/938087203547013131/1022280432076718080/unknown.png)
<br/>

[Project Template](https://github.com/pbp-fasilkom-ui/assignment-repository)
