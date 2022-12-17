import json
import os

f = open("accordion_template.html", "r", encoding="utf-8")
accordion_template = f.read()

f = open("accordion_item_template.html", "r", encoding="utf-8")
accordion_item_template = f.read()

class accordion:
	def __init__(self, name):
		self.name = name
		self.items = []

	def add_item(self, item):
		self.items.append( item )

	def build(self):
		constructed_items = ""
		for item in self.items:
			constructed_items += item.build(self.name)

		result = accordion_template.format(self.name, constructed_items)
		return result

class accordion_item:
	def __init__(self, name):
		self.name = name
		self.items = []

	def add_item(self, item):
		self.items.append( item )

	def build(self, accordion_name):
		constructed_items = ""
		for item in self.items:
			if type(item) is accordion:
				constructed_items += item.build()
			if type(item) is tuple:
				constructed_items += f"<a href=\"/docs/{item[1]}.html\">{item[0]}</a><br>"
		header = self.name + "-header"
		item_id = self.name + "-item"
		result = accordion_item_template.format(
			accordion_name, header, item_id, self.name, constructed_items)
		return result


f = open("template.html", "r", encoding="utf-8")
template = f.read()

f = open("content.json", "r", encoding="utf-8")
#ПОЧЕМУ-ТО JSON очень чувствителен к trailing commas. Осторожно!
content = json.loads(f.read())

def generate_accordion_item(name:str, items:dict)->accordion_item:
	result = accordion_item(name)


	for key in items.keys():
		if type(items[key]) is str:
			result.add_item( (key,items[key]) )
		if type(items[key]) is dict:
			result.add_item( generate_accordion(key, items[key]) )

	return result


def generate_accordion(name:str, items:dict)->accordion:
	result = accordion(name)
	result.add_item( generate_accordion_item(name, items) )
	return result

main_accordion = generate_accordion("Документация", content["items"])
navigation_panel = main_accordion.build()

for obj in os.listdir(".."):
	if os.path.isfile(f"../{obj}"):
		os.remove(f"../{obj}")


for article in content["articles"].keys():
	f = open(f"../{article}.html", "w", encoding="utf-8")
	f.write(template.format(article, navigation_panel, content["articles"][article]) )


