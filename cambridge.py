#!/bin/python3.8
import requests
import inspect
import sys
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print( "usage cambridge.py <word> ")
    exit(1)
word = sys.argv[1]

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
r = requests.get(f'https://dictionary.cambridge.org/zht/詞典/英語-漢語-繁體/{word}', headers = headers)
if r.status_code != 200:
    print("error status", r.status_code)
file = r.text

# 寫入 file
# with open("a.html","w") as file :
#     file.write(r.text)

# 寫出 file
# # bs4 parse the html file
# file = open("a.html")

soup = BeautifulSoup(file,"html.parser")


# 檢測 css selector 是否出錯, 抓到空陣列回來
def testEmpyhList( ary ):
    if ary == []:
        print( "enpty array")
        print( inspect.stack()[1].function )
        exit(1)


#first parse
def parse0(soup):
    # 簡短中翻英
    print(soup.select("meta[itemprop='headline']")[0]["content"])
    print( "=" * 70 )  #換行

    # 第一層級 parse , 取詞性區塊
    block_PartOfSpeechs = soup.select(".pos-body")  # biggest, first block got
    testEmpyhList( block_PartOfSpeechs )

    for block in block_PartOfSpeechs :
        parse1( block )



# level 1 process
def parse1(block):
    # 第二層級, 由詞性區塊 取出 詞語解釋區塊
    # for i , block_interpretation in enumerate( block.select(".pr.dsense") ):
    block_interpretations = block.select(".pr.dsense")
    testEmpyhList( block_interpretations )

    for block in block_interpretations :
        parse2( block )

# level 2 process
def parse2( block ):
    print( "-" * 70 )
    try:
        # 顯示詞性+語意 ( 1 word) , 有些單字是沒有這段的,避免index error, 使用try
        print( "##" , block.select(".dsense_h")[0].text.replace('\n      ', '') )
    except BaseException:
        pass
    

    # 簡短英文解釋( 1 statement )
    print( block.select(".ddef_h")[0].text)

    # 簡短中文解釋
    print( block.select(".def-body > .trans.dtrans.dtrans-se.break-cj")[0].text )

    block_examples = block.select(".examp.dexamp")

    for example in block_examples:
        print( example.text.replace( '\n',"" ) )

    print( "\n")


parse0( soup )

