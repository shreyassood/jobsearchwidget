#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
import getJobs

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def main():
	jobResponse = getJobs.getJobs("Google", 0)
	return render_template('index.html', current = jobResponse['currentpage'], 
		total = jobResponse['totalpages'], jobs = jobResponse['results'])

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=80, debug=True)
