from flask import Flask,flash, redirect,render_template,url_for,request
import os
from werkzeug.utils import secure_filename
from Caption import *



app=Flask(__name__)
UPLOAD_FOLDER = ' C:\\Users\\Personal\\Desktop\\ardent_project\\my_project\\static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

@app.route("/")
def index():
	return render_template('index.html')


@app.route("/submit",methods=['GET','POST'])
def home():
	if request.method =='POST':
		file = request.files['file']
		#print(file)
		if file:
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            

			#collecting image path from backend and sending in the frontend 
			#path='http://127.0.0.1:5000/static/'+filename
			

			# ekhane model ta call kore predict er vettore image ta pass kore je caption ta generate hbe seta store korbi tahalei hbe
			
			#.......................................................
            
			caption_generated=generate_desc(filename)
			#......................................................./
			return render_template('home.html',filepath=path,caption=caption_generated)

	return render_template('index.html')
	

if __name__=="__main__":
	app.run(debug=True)
