import webbrowser

q_list = ["bts","아이유","블랙핑크","위너"]

url = "https://google.com"
url = "https://www.google.com/search?&q="

for q in q_list:
    webbrowser.open(url+q)

