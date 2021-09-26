# Dictionary-search-by-scrapeing
Quickly lookup word in dictionary in command-line. Current support Cambridge. English-chinese only.
在命令視窗快速查詢字典。目前僅有`劍橋英漢字典`可用。


## Prerequisite
```
pip install requests
pip install beautifulsoup4
python --version   
## version need 3.5 + ( for "inspect" package ) 
```

## Usage
```
./cambridge.py  <word>
e.g.
./cambridge.py Hello
./cambridge.py "show home"
./cambridge.py show-home    # equal above, using "dash" for phrase.
```
