
from flask import Flask, render_template, request
import pandas as pd
from location_scape import map_maker
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/homepage')
def homepage():
    return render_template('home.html')

@app.route('/map_options',methods=['POST'])
def map_options():
    if request.method=='POST':
        key= request.form.get('keyword_btn')
        region=request.form.get('region_btn')
        from_date=request.form.get('from_date_btn')
        to_date=request.form.get('to_date_btn')
        radius=request.form.get('radius_btn')
        print(region)
        map_maker(key,from_date,to_date,region,radius)

        return render_template('maps_page.html')

@app.route('/map1')
def map1():
    return render_template('map1.html')

@app.route('/map3')
def map3():
    return render_template('map3.html')

@app.route('/map2')
def map2():
    return render_template('map2.html')


@app.route('/tweets')
def tweets():
    data2 = pd.read_csv("twitter data_bad.csv")
    data = pd.read_csv("twitter data_bad.csv")
    for row in data2:
        print(row)
    return render_template('tweets_page.html',data=data.to_html())



if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)
