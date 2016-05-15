from lxml import html

import requests
import csv

local_file = "LOCAL_DIR_LOCATION"
videos = ["https://www.youtube.com/watch?v=VIDEO1", "https://www.youtube.com/watch?v=0UFkjvzvZe4&list=VIDEO2"]
video_list = []
    
# scrape_table function: gets passed an individual page to scrape
def scrape_page(video, video_list):
    print "reading: "
    print video
    page = requests.get(video)
    x = html.fromstring(page.text)
    date = x.xpath('//strong')[2].text_content()
    print "got date:"
    print date
    video_list += [[video, date]]
    print video_list

for video in videos:
    scrape_page(video, video_list)

with open(local_file, "wb") as f:
    writer = csv.writer(f)
    writer.writerows(video_list)

