# ## Integrate html with Flask
# ## HTTP verbs GET and POST
# ## lec 05





# from flask import Flask, redirect, url_for, render_template, request

# app = Flask(__name__)

# @app.route('/')
# def welcome():
#     # return "Welcome to my first flask app. Thanks. Thank you so much for visiting."
#     return render_template('index.html')

# @app.route('/success/<int:score>')
# def success(score):
#     # print(score)
#     res = ""
#     if score>=50:
#         res = "PASS"
#     else:
#         res = "FAIL"
    
#     return render_template('result.html', result = res)

# @app.route('/fail/<int:score>')
# def fail(score):
#     return "The person has passed and the score is " + str(score)

# ## result checker
# @app.route('/results/<int:marks>')
# def results(marks):
#     result = ""
#     if marks < 50:
#         result = 'fail'
#     else:
#         result = 'success'
    
#     # return result
#     return redirect(url_for(result, score = marks))


# ## result checker HTML page 
# @app.route('/submit', methods = ['POST', 'GET'])
# def submit():
#     avg_score = 0
#     if request.method == "POST":
#         science = float(request.form['science'])
#         maths = float(request.form['maths'])
#         c = float(request.form['c'])
#         data_science = float(request.form['datascience'])

#         avg_score = (science + maths + c + data_science)/4


#     return redirect(url_for('success', score = avg_score))




# if __name__ == "__main__":
#     ## debug == True will update any updates saved on python code
#     app.run(debug = True)





## Jinja 2 template engine
'''
{%...%} for statements, conditions for loops
{{  }}  Expression to print output
{#  #}  Comments
'''
## lec 06





from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    # return "Welcome to my first flask app. Thanks. Thank you so much for visiting."
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score>= 50:
        res = "PASS"
    else:
        res = "FAIL"
    
    res_dict = {"Score" : score, "Result" : res}

    return render_template('result.html', result = res_dict)



@app.route('/fail/<int:score>')
def fail(score):
    return "The person has passed and the score is " + str(score)

## result checker
@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'
    
    # return result
    return redirect(url_for(result, score = marks))


## result checker HTML page 
@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    avg_score = 0
    if request.method == "POST":
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        avg_score = (science + maths + c + data_science)/4


    return redirect(url_for('success', score = avg_score))




if __name__ == "__main__":
    ## debug == True will update any updates saved on python code
    app.run(debug = True)
    # app.run()
