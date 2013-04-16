#!/usr/bin/python


import ast
import json
import sys
import urllib2
sys.path.append("/home/pi/git/cosm-python")
sys.path.append("/home/pi/git/tweepy")
import tweepy
import cosm
import time
from datetime import datetime
from random import randint

DEBUG = 0
# your private key
key = "aC-HMEeaeDpnJ6VGtAI6hFGh7umSAKxaZndxY0kxUU1kaz0g"
# feed specific id
feedid = "116286"
test = 0

CONSUMER_KEY = 'QG5nVIhWNpNw6OmCuoZH6Q'
CONSUMER_SECRET = 'uQsFecugofj9vNqnzBkTf1aoAM9ZobYLFYbNEuBkA'
ACCESS_KEY = '944356818-UP4xjuRHBnUfe8R8mwl4KWqEj4T1KvRUozWWa25R'
ACCESS_SECRET = 'nq5iv4U1WvbB0I0WMUXUqNntv4IIb9aRasPEkVOk'

def Twitter(tweet):
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
	if DEBUG == 0:
		api.update_status(tweet)
		print "tweeted:\n"+tweet
	if DEBUG == 1:
		print "fake tweeted:\n"+tweet
	
def Cosm_load(feedid, key ,id):
	try:
		url = urllib2.urlopen('http://api.cosm.com/v2/feeds/'+feedid+'.json?key='+key+'&datastreams='+id)
		data = json.load(url)
		#print data
		datastreams = data['datastreams']
		datastreams = str(datastreams)[1:-1]
		datastreams = ast.literal_eval(datastreams)
		#print datastreams
		test = datastreams['current_value']
		return test
	except urllib2.HTTPError, e:
		print e.code
	except urllib2.URLError, e:
		print e.args
	
	
def Main():
	print "start"
	volt = Cosm_load(feedid, key, "Pi_Volt")
	amp = Cosm_load(feedid, key, "Pi_Amp")
	cpu = Cosm_load(feedid, key, "Pi_CPU_Load")
	status = Cosm_load(feedid, key, "Pi_Status")
	temp = Cosm_load(feedid, key, "Pi_Temp")
	download = Cosm_load(feedid, key, "Pi_Download")
	upload = Cosm_load(feedid, key, "Pi_Upload")
	statusout1 = volt+"V "+amp+"mA"
	#print( "Cpu "+cpu+" Status "+status+" Temp: "+"%.2f" % (temp))
	statusout2 = "Cpu %s Status %s Temp: %.0f" % (cpu,status,float(temp))
	statusout3 = "Download: %skb/s Upload: %skb/s" % (download,upload)
	tweetinfo = statusout1+"\n"+statusout2+"\n"+statusout3
	if DEBUG == 1:
		print statusout1 
		print statusout2
		print statusout3
		print "sending to twitter:\n"+tweetinfo
	Twitter(tweetinfo)
Main()
