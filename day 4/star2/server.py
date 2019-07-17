    
from bottle import  route, jinja2_view,run,static_file,request
from functools import partial
from jinja2 import Template

user = {"name":"","last_name":""}

view = partial(jinja2_view, template_lookup=['templates'])

@route("/",method="get")
@view("index.html")
def index():
    global user
    return{"user":user}

@route("/signup",method="post")
@view("index.html")
def add_name():
    global user
    user["name"] = request.forms.get("first"),
    user["last_name"] = request.forms.get("last"),
    return {"user": user}
    

if __name__ == "__main__":
    run(host='localhost', port=4700, debug=True, reloader=True)