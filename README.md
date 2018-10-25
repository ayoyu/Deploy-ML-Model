# Deploy-your-ML-Model-like-a-Rest-API
## Sentiment Analysis : Movie Classifier API

A **RESTful API** is an application program interface (API) that uses HTTP requests to GET, PUT, POST and DELETE data.
So my model can be used by multiple developers working on different platforms, such as web or mobile.

To test this API first type in your shell:
```
$ pip install -r requirements.txt
```
then make sure to run *REST_API.Py* script.

After that in your shell:
```
$ curl http://127.0.0.1:5000/ -d "query = Here you type the data that you want to send to the server" -X GET 
```
Or from python if you have the requests library installed:
```
>>> from request import get
>>> get('http://127.0.0.1:5000/',{'query':Here you type the data that you want to send to the server}).json()
```
examples:

* Using curl in the terminal:
```
$ curl http://127.0.0.1:5000/ -d "query=I love so much that movie" -X GET 
```
```
{
    "positive": "69.1%"
} 
```
* Using Python :
```
>>> from request import get
>>> get('http://127.0.0.1:5000/',{'query':'i love that movie'}).json()
>>> {'positive': '83.81%'}
```
if you want to see the web version of this Movie classifier app go and check http://ayoubelkhallioui.pythonanywhere.com/

* Updated : 

I hosted the API in Pythonanywhere so :

in your terminal:
```
$ curl http://ayoubelkhallioui.pythonanywhere.com/ -d "query=I love so much that movie" -X GET 
```
or in the browser:
```
http://ayoubelkhallioui.pythonanywhere.com/?query="I love so much that movie" 
```
