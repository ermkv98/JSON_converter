import json

JSON_FILE = "source.json"
HTML_FILE = "source.html"


def convert_file():
    try:
        html_content = ""
        with open(JSON_FILE, 'r') as f:
            jdata = json.load(f)
        for json_dict in jdata:
            for key, value in json_dict.items():
                html_content += '<{0}>{1}</{0}>'.format(key,
                                                        value)
        with open(HTML_FILE, 'w') as f:
            f.write(html_content)
        print('Done!')
    except Exception:
        raise


convert_file()