import requests

baseQuery = "http://api.indeed.com/ads/apisearch?publisher=9327050513995141&format=json&v=2"
start = 0

def buildQuery(baseQuery, company, start_number):
	#q=company%3A%28Google%29
	start=0



def getJsonResponse(query):
	r = requests.get(query)
	if(r == None):
		return None
	if(r.status_code != 200):
		return None
	else:
		return r.content

print(getJsonResponse(baseQuery))