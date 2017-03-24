import requests
import json
from urllib.parse import urlencode
from math import ceil

baseQuery = "http://api.indeed.com/ads/apisearch"

def buildQuery(baseQuery, company, start_number):
	queryParams = {
		'publisher':'9327050513995141',
		'format':'json',
		'v':'2',
		'start' : str(start_number),
		'q' : "company: (" + company + ")" 
	}
	
	return baseQuery + "?" + urlencode(queryParams)

def getJsonResponse(query):
	r = requests.get(query)
	if(r == None):
		return None
	if(r.status_code != 200):
		return None
	else:
		return r.content

def getJobs(company, page_number):
	query = buildQuery(baseQuery, company, page_number * 10)
	jsResp = getJsonResponse(query)
	
	if(jsResp == None):
		return None

	jsonParsed = json.loads(jsResp.decode('utf-8'))

	if(jsonParsed == None):
		return None

	jobsResult = {
		'results' : jsonParsed['results'],
		'totalpages' : ceil(int(jsonParsed['totalResults']) / 10),
		'currentpage' : jsonParsed['pageNumber']
	}

	return jobsResult


#Response Definition: {Results[], TotalPages, CurrentPage}

print(getJobs("Google", 0))