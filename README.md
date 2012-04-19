django-lasso
============

##get all endpoints:
	http://localhost:8000/api/v1/?format=json

##example list of all links:
	http://localhost:8000/api/v1/link/?format=json&limit=5

##Getting all items with a certain tag:
	http://127.0.0.1:8000/api/v1/tag/?value=google



##Saving a new url
	curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"url": "http://adam.com", "pub_date": "2011-05-22T00:46:38"}' http://localhost:8000/api/v1/link/
	
####response:
	HTTP/1.0 201 CREATED
	Date: Thu, 19 Apr 2012 19:36:39 GMT
	Server: WSGIServer/0.1 Python/2.7.2
	Content-Type: text/html; charset=utf-8
	Location: http://localhost:8000/api/v1/link/2/



##Saving a tag:
	$ curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"value": "adam","link": "/api/v1/link/2/"}' http://localhost:8000/api/v1/tag/
####response:
	HTTP/1.0 201 CREATED
	Date: Thu, 19 Apr 2012 20:00:01 GMT
	Server: WSGIServer/0.1 Python/2.7.2
	Content-Type: text/html; charset=utf-8
	Location: http://localhost:8000/api/v1/tag/2/



