from flask import Flask,render_template, request, flash, redirect, url_for, send_file
import sys
from FuncMile36 import return_csv
app = Flask("Mile6")

@app.route('/test')
def hello_world():
    return 'Hello, World!'

@app.route("/",  methods=('GET', 'POST'))
def viewentries():
    usernames_list = [
        "dianerobinson@gmail.com",
        "twiliodevs@twil.io",
        "TwilioQuest@gmail.com"
    ]
    if request.method == 'POST':
        url = request.form['inp_url']

        if not url:
            flash('URL is required!')
        else:
            print('url entered is ', url)
            return_csv(url)
            print('called function return_csv - check for created csv file')
            return redirect("/getCSV")

    return render_template('index.html', variable=usernames_list)

@app.route("/getCSV")
def getPlotCSV():
    # with open("outputs/Adjacency.csv") as fp:
    #     csv = fp.read()
    return render_template('csv.html', inp_url = "this is test", csv = "363500.csv")


@app.route("/downloadCSV")
def downloadCSV():
    # with open("outputs/Adjacency.csv") as fp:
    #     csv = fp.read()
    # return render_template('csv.html', inp_url = "this is test", csv = "Mile3/363500.csv")
    return send_file('363500.csv',
                     mimetype='text/csv',
                     attachment_filename='363500.csv',
                     as_attachment=True)


#{{ request.form['inp_url'] }}
# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# @app.route('/')
# def student():
#     return render_template('yourfile.html')
#
# @app.route('/urlinput',methods = ['POST', 'GET'])
# def url_results():
#     if request.method == 'POST':
#         result = request.form['Curtain_OPENTIME']
#         print(result)
#         return "thank you for filling out this form"
    # if request.method =='GET':
    #     inputurl = 'get url from website to run it in the function'
        #run thr url in program
        #output = output.csv
# if 'Mile6' == '__main__':
#     app.run(debug = True)