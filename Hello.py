from flask import Flask,render_template, request

app = Flask("Mile6")

@app.route('/test')
def hello_world():
    return 'Hello, World!'

@app.route("/")
def viewentries():
    usernames_list = [
        "dianerobinson@gmail.com",
        "twiliodevs@twil.io",
        "TwilioQuest@gmail.com"
    ]
    return render_template('index.html', variable=usernames_list)



#
# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# @app.route('/')
# def student():
#     return render_template('yourfile.html')
#
# @app.route('/result',methods = ['POST', 'GET'])
# def result():
#     if request.method == 'POST':
#         result = request.form['Curtain_OPENTIME']
#         print(result)
#         return "thank you for filling out this form"
#
# if 'Mile6' == '__main__':
#     app.run(debug = True)