#coding:utf-8
import  requests
import json
from bs4 import  BeautifulSoup
from urllib2 import     HTTPError,URLError
import time

#code-info
'''
author:Edward
create-time:2017-4-20

'''
def get_yahoo_answers(after_pv,bpos,cpos):

    page=requests.get(url = 'https://answers.yahoo.com/_module?name=YANewDiscoverTabModule&after'
                            '={0}&sid=396545384&disableLoadMore=false&bpos={1}&cpos={2}'.
        format(
        after_pv,bpos, cpos))

    json_text=page.json()
    after_pv=json_text['YANewDiscoverTabModule']['options']['after']
    bpos= json_text['YANewDiscoverTabModule']['options']['bpos']
    cpos = json_text['YANewDiscoverTabModule']['options']['cpos']
    return  after_pv,bpos,cpos

def main():
    loop_id=3
    page_id=41
    after_pv="pv40~p:0"
    #for i in range(3, 100):
    while True:
        after_pv,loop_id, page_id = get_yahoo_answers(after_pv,loop_id, page_id)
        print after_pv,loop_id, page_id
        time.sleep(0.1)
        page = requests.get(
        url='https://answers.yahoo.com/_module?name=YANewDiscoverTabModule&after'
                '={0}&sid=396545384&disableLoadMore=false&bpos={1}&cpos={2}'.format(
                after_pv,loop_id ,page_id))
        soup=BeautifulSoup(page.json()['YANewDiscoverTabModule']['html'],'lxml')
        text=soup.find_all('a',class_='Fz-14 Fw-b Clr-b Wow-bw title')
        for i in text:
             file=open('info.txt','a')
             print i.get_text()
             try:
                 file.write(i.get_text().encode('utf-8')+'\n')
             finally:
                 file.close()
if __name__ == '__main__':
    main()


