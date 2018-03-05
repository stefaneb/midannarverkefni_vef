from bottle import run, route, template, static_file, error
import requests

response = requests.get('http://apis.is/petrol')

data = response.json()

@route('/')
def index():
    return template('index',data=data)

@route('/company/<company>')
def company(company):
    return template('company', company=company, data=data)

#static file route
@route('/static/<filename>')
def static_server(filename):
    return static_file(filename,root=('./static_files'))

run()