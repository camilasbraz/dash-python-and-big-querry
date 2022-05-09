# dash-python-and-big-query
### How to connect a table in Google Cloud Big Query to your dash app


I was working on a dash app that required password access and had different levels of access and I decided to manage that using SQL.
Since I was hosting it on Google Cloud Platform, it made sense to use big query to make that happen. Also, big query is extremely cheap (in contrast
to cloud SQL) and would be practically free for this purpose (so far, they haven't charged me!)


## Initial steps

Before we go to the coding part, we need to set up a google cloud platform account and create a database in big query. I followed the steps on 
<a href = "https://www.youtube.com/watch?v=43VGD1uv9ao"> this video </a>. It was very useful but some things changed on the configuration of big query,
specifically on the `.json` of the key. What worked for me was following the same steps highlight by the video and to get the missing part, you have to
go to `PIs&Services` menu and click on `Credentials`. In the section `Service Accounts` click on the service you have just created and then in the`KEYS`
tab then in `ADD KEYS`. Choosse json as the format and download it (it will probably start downloading automatically).

You should put this json on your assets folder.

## Useful links


<a href = "https://github.com/googleapis/python-bigquery-sqlalchemy">  bigquery-sqlalchemy git hub </a>

<a href = "https://hackersandslackers.com/bigquery-and-sql-databases/">bigquery-and-sql-databases </a>

<a href = "https://www.pythonanywhere.com/forums/topic/14348/"> pythonanywhere forum on a related topic </a>

<a href = "https://gist.github.com/antoniocachuan/07dd96e38cb6fca56e39ddabb1438425">  code example </a>

## Dash-User-Management git hub

<a href = "https://github.com/Chris3691/Dash-User-Management">  Dash-User-Management </a>
