#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import sys

def main():
    url = sys.argv[1]
    outputFileName = sys.argv[2]
    page = requests.get(url)
    parsed = BeautifulSoup(page.content, "html.parser")
    outputFile = open(outputFileName, "w")
    outputFile.write(str(parsed))
    
if __name__ == "__main__":
    main()