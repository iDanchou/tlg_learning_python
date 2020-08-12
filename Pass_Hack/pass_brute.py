import requests
import sys

url = sys.argv[1]
wordlist = sys.argv[2]
ext = sys.argv[3]

fo = open(wordlist,"r+")