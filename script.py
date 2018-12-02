import requests

file_url = "http://nptel.ac.in/courses/106105080/pdf/"

data = [[1,2],[2,7],[3,4],[4,6],[5,10],[6,3],[7,5],[8,3]]

for i in data:
    for j in range(i[1]):
        fname = "M" + str(i[0]) + "L" + str(j+1) + ".pdf"
        link = file_url + fname
        
        r = requests.get(link, stream = True)
        
        with open(fname,"wb") as pdf:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    pdf.write(chunk)