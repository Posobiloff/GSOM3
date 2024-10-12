import requests
#1. This code counts the number of .png files in the web page
r = requests.get("https://gsom.spbu.ru/en/")
r_content = str(r.content)
pngs = r_content.count(".png")
print(f"In the web page there are {pngs} .png files")
#2. This code extract the first .png from the web page
r = requests.get("https://gsom.spbu.ru/en/")
r_content = str(r.content)
f_png = r_content.find(".png")
f_index = r_content.rfind("/t", 0, f_png)
l_index = r_content.find(".png", f_png) + 4
l_part = r_content[f_index:l_index]
f_part = "https://gsom.spbu.ru"
whole = f_part+l_part
w_b = requests.get(whole)
file = open("/home/jovyan/PyProject1/GSOM3/Assignment12/GSOM.png", "wb")
file.write(w_b.content)