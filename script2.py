import requests
import logging
import os
import shutil

if(os.path.exists('./download.log')):
    os.remove('./download.log')

logging.basicConfig(filename='download.log', format='%(asctime)s [%(levelname)s]\t: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

# Make a directory to store files
DIR_PATH = "./files/"
if(os.path.exists(DIR_PATH)):
    logging.info('Existing directory found. Removing ./files/ and all its contents.')
    shutil.rmtree('./files')
os.mkdir(DIR_PATH)

file_url = "http://nptel.ac.in/courses/106105080/pdf/"

data = [[1,2],[2,7],[3,4],[4,6],[5,10],[6,3],[7,5],[8,3]]

for i in data:
    for j in range(i[1]):

        file_name = "M" + str(i[0]) + "L" + str(j+1) + ".pdf"
        link = file_url + file_name
        
        logging.info('Fetching ' + file_name)
        r = requests.get(link, stream=True)
        logging.info('Fetch successful.')

        file_path = DIR_PATH + file_name
        logging.info('Saving file to local disk.') 
        with open(file_path, "wb") as pdf:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    pdf.write(chunk)
        logging.info('File ' + file_name + ' saved successfully.')