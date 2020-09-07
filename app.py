import sys
sys.path.append('C:/users/123122/Desktop/Stepictures/')
sys.path.append("D:/poem")
from flask import Flask,render_template
from flask import jsonify,abort,request,redirect,url_for
import poem
import all_panel
import json
app=Flask(__name__,static_url_path = '/static')

@app.route('/')
def index():
   return render_template('gate.html')


@app.route('/index_stp')
def index_stp():
   return render_template('index_stp.html')

@app.route('/output_stp')
def output_stp():
   return render_template('output_stp.html')

@app.route('/services_stp')
def services_stp():
   return render_template('services_stp.html')


@app.route('/index_poem')
def index_poem():
   return render_template('index_poem.html')

@app.route('/services_poem')
def service_poem():
   return render_template('services_poem.html')

@app.route('/output_poem')
def output_poem():
   return render_template('output_poem.html')

'''
@app.route('/poem')
def index_poem():
    return render_template('唐詩的ｈｔｍｌ')

@app.route('/poem_output')
def poem_no_output():
    return render_template('唐詩的ｏｕｔｐｕｔ')
'''

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
        path_list=[]
        pic_url = all_panel.stepictures(steps)
        title = data['title']
        path_list.append(pic_url)
        path_list.append(steps)
        path_list.append(title)

        return json.dumps({'status':'OK'})

    elif request.method == 'GET':
        print(path_list)
        pic_url.append(picname)
        print(jsonify(pic_url))
        return jsonify(path_list)
   
@app.route('/poem',methods = ['GET','POST'])
def methodget_poem():
    pic_url2 = " "
    if request.method == 'POST':
        
        data = json.loads(request.data)
        title = data['title']
        context = data['context']
        global poem_list
        print(context)
        poem_list=[]
        pic_url2 = poem.poem(context)
        print(pic_url2)
        poem_list.append(title)
        poem_list.append(context)
        poem_list.append(pic_url2[0])
        poem_list.append(pic_url2[1])

        return json.dumps({'status':'OK'})

    elif request.method == 'GET':
        print(poem_list)
        print(jsonify(pic_url2))
        
        return jsonify(poem_list)
    


if __name__ == '__main__':
    app.debug = True
    app.run()