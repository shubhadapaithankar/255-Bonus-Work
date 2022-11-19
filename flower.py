from flask import Flask, render_template, request, redirect, flash
import PIL.Image as Image
from inference import get_flower_name
app = Flask(__name__)
app.secret_key="shubhada"
@app.route('/',methods = ['GET','POST'])
def hello_world():
	if request.method == 'GET':
		return render_template('index.html',name = "Shubhada")
	if request.method == 'POST':
		print(request.files)
		if 'files[]' not in request.files:
			print('file not uploaded , please try again')
			return redirect('/')
		files = request.files.getlist('files[]')
		print(type(files))
		result={}
		for file in files:
			print("files:" + file.filename)
			# file.save(file.filename)
			image=file.read()
			category,flower_name = get_flower_name(image_bytes=image)
			result[flower_name] = category
			print(category)
			print(flower_name)

		print(result)
		for key,value in result.items():
			print(key) 
			print(value) 
			flash(key,value)

		print("all results :")
		# image = files[0].read()
		return render_template('result.html',flower = flower_name, category = category)
