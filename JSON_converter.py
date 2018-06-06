import json

JSON_FILE = "source.json"
HTML_FILE = "source.html"

#contains json tags translated to html, 2 tags just for example, can be extended
TAG_LIST = "tags.json"


def convert_file():
	try:
		html_content = ""
		with open(JSON_FILE, 'r') as f:
			jdata = json.load(f)
		for json_dict in jdata:
			for key, value in json_dict.items():
				converted_key = convert_tag(key)
				html_content += '<{0}>{1}</{0}>'.format(converted_key,
														value)
		with open(HTML_FILE, 'w') as f:
			f.write(html_content)
		print('Done!')
	except Exception:
		raise


def convert_tag(json_tag):
	with open(TAG_LIST, 'r') as f:
		tags = json.load(f)
	for json_dict in tags:
		for key, value in json_dict.items():
			if key == json_tag:
				return value


convert_file()