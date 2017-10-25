import serial
from time import sleep
from flask import Flask,jsonify
import xml.etree.ElementTree as ET
import json

app = Flask(__name__)

tree = ET.parse('containers.xml')
root = tree.getroot()

tree2 = ET.parse('consumption.xml')
root2 = tree2.getroot()

@app.route("/")
def index():
	with open('weights.txt','r') as r:
		a = r.readline()
	a = a.split(" ")
	json_data = []
	for container in root.findall('container'):
		content = container.find('content').text
		iden = container.get('id')
		json_data.append({"content": content, "left": a[int(iden)-1]})
	return jsonify(json_data)

@app.route("/containers/")
def containers():
	json_data = []
	for container in root.findall('container'):
		iden = container.get('id')
		content = container.find('content').text
		left = container.find('left').text
		json_data.append({"id": iden,"content": content, "left": left})
	return jsonify(json_data)


@app.route("/container/<iden>")
def container(iden):
	json_data = []
	for container in root.findall('.//container[@id="'+iden+'"]'):
		iden = container.get('id')
		content = container.find('content').text
		left = container.find('left').text
		saturated_fat = container.find('saturated_fat').text
		polyunsaturated_fat = container.find('polyunsaturated_fat').text
		monounsaturated_fat = container.find('monounsaturated_fat').text
		cholestrol = container.find('cholestrol').text
		sodium = container.find('sodium').text
		potassium = container.find('potassium').text
		carbohydrates = container.find('carbohydrates').text
		dietary_fiber = container.find('dietary_fiber').text
		sugars = container.find('sugars').text
		protein = container.find('protein').text
		vitamin_a = container.find('vitamin_a').text
		vitamin_c = container.find('vitamin_c').text
		calcium = container.find('calcium').text
		iron = container.find('iron').text
		json_data.append({"id": iden,"content": content, "left": left, "polyunsaturated_fat": polyunsaturated_fat, "monounsaturated_fat": monounsaturated_fat, "cholestrol": cholestrol, "sodium": sodium, "potassium": potassium, "carbohydrates": carbohydrates, "dietary_fiber": dietary_fiber, "sugars": sugars, "protein": protein, "vitamin_a": vitamin_a, "vitamin_c": vitamin_c, "calcium": calcium, "iron": iron})
	return jsonify(json_data)

@app.route("/consumption_all/")
def consumption_all():
	json_data = []
	for container in root2.findall('.//container'):
		for left in container:
			json_data.append({"timestamp": left.get("at"), "left": left.text})
	return jsonify(json_data)

@app.route("/consumption/<iden>")
def consumption(iden):
	json_data = []
	for container in root2.findall('.//container[@id="'+iden+'"]'):
		for left in container:
			json_data.append({"timestamp": left.get("at"), "left": left.text})
	return jsonify(json_data)

app.run(host= '0.0.0.0')
