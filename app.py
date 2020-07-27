import sys
sys.path.append('C:/users/123122/Desktop/Stepictures')
from flask import Flask,render_template
from flask import jsonify,abort,request,redirect,url_for
import all_panel
import json
app=Flask(__name__,static_url_path = '/static')

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/outputpic')
def output1():
   return render_template('output.html')

@app.route('/services')
def services():
   return render_template('services.html')

@app.route('/test')
def output2():
   return render_template('test4.html')



@app.route('/post_step',methods = ['GET','POST'])
def methodget():
    steps = []
    pic_url=[]
    picname = 'static/img/logo.png' 
    if request.method == 'POST':
        data = json.loads(request.data)

        #print(str(data)+"pPPP")
        for i in range(int(data['num'])):
            steps.append(data['step'+str(i+1)])
        global path_list
        path_list = all_panel.stepictures(steps)

        return json.dumps({'status':'OK'})

    elif request.method == 'GET':
        print(path_list)
        pic_url.append(picname)
        print(jsonify(pic_url))
        return jsonify(path_list)
    
    


if __name__ == '__main__':
    app.debug = True
    app.run()