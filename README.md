# Bitly URL Shortener

## About:
The script shorten url with bit.ly service. 

Based on [Bitly API (4.0.0)](https://dev.bitly.com/v4_documentation.html)

Script take any link or bitlink as input.
If you will enter a link, you got a bitlink. 
And if you will enter a bitlink, you got number of clicks on it
## System requirements:
python3.5+

## How to install:

```bash
$ python -m pip install -r requirements.txt
```

## How to run:
python bitly.py your-url-here

``` bash
$ python bitly.py https://ya.ru
Take your bitlink: http://bit.ly/2HAAwZ4

$ python bitly.py http://bit.ly/2HAAwZ4
Total links on bitlink: 9
```

## Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.