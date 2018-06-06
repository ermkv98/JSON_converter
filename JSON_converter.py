import json

JSON_FILE = "source.json"
HTML_FILE = "source.html"


def convert_file():
    try:
        html_content = ""
        with open(JSON_FILE) as f:
            jdata = json.load(f)
        html_content += "<ul>"
        for json_dict in jdata:
            html_dict = "<li>"
            for key, value in json_dict.items():
                html_dict += '<{0}>{1}</{0}>'.format(key,
                                                    value)
            html_content += html_dict + "</li>"
        html_content += "</ul>"
        with open(HTML_FILE, 'w') as f:
            f.write(html_content)
        print('Done!')
    except Exception:
        raise


convert_file()