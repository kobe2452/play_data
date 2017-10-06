import requests, re, time, sys, xlwt
from bs4 import BeautifulSoup
from lxml import etree
import urllib.request

def getHTMLText(url, cookies):

    try:
        r = requests.get(url, cookies)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("Failed!")

def getVideosInOnePage(html, worksheet, page):

    soup = BeautifulSoup(html, "html.parser")
    videoContentList = soup.find('div', attrs={'id':'videobox'})

    i = 0
    selector = etree.HTML(html)
    
    for videoLi in videoContentList.find_all('div', attrs={'class':'listchannel'}):

        oneVideo = []

        videoName = videoLi.find('img', attrs={'width':'120'}).get('title')
        videoUrl = videoLi.find('a', attrs={'target':'blank'}).get('href')

        timeLength = selector.xpath('//div[@class="listchannel"]/text()')[4+i*17].strip()
        uploadTimestamp = selector.xpath('//div[@class="listchannel"]/text()')[6+i*17].strip()
        try:
            authorId = videoLi.find('a', attrs={'target':'_parent'}).getText()
        except AttributeError:
            authorId = "None"
                    
        try:
            authorUrl = videoLi.find('a', attrs={'target':'_parent'}).get('href')
        except AttributeError:
            authorUrl = "None"
        viewCount = selector.xpath('//div[@class="listchannel"]/text()')[10+i*17].strip()
        likeCount = selector.xpath('//div[@class="listchannel"]/text()')[11+i*17].strip()
        commentCount = selector.xpath('//div[@class="listchannel"]/text()')[13+i*17].strip()

        oneVideo.append(videoUrl)
        oneVideo.append(videoName)
        oneVideo.append(timeLength)
        oneVideo.append(uploadTimestamp)
        oneVideo.append(authorId)
        oneVideo.append(authorUrl)
        oneVideo.append(long(viewCount))
        oneVideo.append(long(likeCount))
        oneVideo.append(long(commentCount))

        rownumber = (page-1) * 20 + i + 1
        saveListToExcel(worksheet, oneVideo, rownumber)
        
        i += 1

def saveListToExcel(worksheet, oneVideo, rownumber):
    
    for i, e in enumerate(oneVideo):
        worksheet.write(rownumber, i, e)

def main():

    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet('worksheet', cell_overwrite_ok=True)

    headers = ['videoUrl', 'videoName', 'timeLength', 'uploadTimestamp', 'authorId', 'authorUrl', 'viewCount', 'likeCount', 'commentCount']
    for i, e in enumerate(headers):
        worksheet.write(0, i, e)

    cookies = ''

    starting = 1
    ending = 501

    for page in range(starting, ending):
        FvUrl = 'http://93.91p12.space/v.php?category=mf&viewtype=basic&page=' + str(page)
        print('Saving video info on page ' + str(page))
        getVideosInOnePage(getHTMLText(FvUrl, cookies), worksheet, page)

    workbook.save('91_page' + str(starting) + '-' + str(ending) + '.xls')
    
if __name__=='__main__':
    main()