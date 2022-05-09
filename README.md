# dash-python-and-big-query
### How to connect a table in Google Cloud Big Querry to your dash app


I was working on a dash app that required password access and had different levels of access and I decided to manage that using SQL.
Since I was hosting it on Google Cloud Platform, it made sense to use big query to make that happen. Also, big query is extremely cheap (in contrast
to cloud SQL) and would be practically free for this purpose (so far, they haven't charged me!)


## Firsts steps

Before we go to the coding part, we need to set up a google cloud platform account and create a database in big query. I followed the steps on 
<a href = "https://www.youtube.com/watch?v=43VGD1uv9ao"> this video </a>. It was very useful but some things changed on the configuration of big query,
specifically on the `.json` of the key. What worked for me was following the same steps highlight by the video and to get the missing part, you have to
