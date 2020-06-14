#!/usr/local/bin/python3

import http.client,ssl,json,argparse,datetime,sys
from pathlib import Path
from os import path

def check_key():
	home = str(Path.home())
	if path.exists(home + "/.google_key"):
		with open(home + '/.google_key', 'r') as reader:
                    key=reader.readline().strip('\n\r')
                    return key
	else:
		print("\nA Google API key must be created for this program to work and it needs to be stored in $HOME/.google_key\n")
		quit()

def construct_url(key, query='blah', afterdate='blah'):
	parser = argparse.ArgumentParser()
	parser.add_argument("-q", "--query", help="Search Terms", action="store", dest="query")
	parser.add_argument("-r", "--results", help="The number of items returned from 0 to 50", action="store", dest="results")
	parser.add_argument("-s", "--safesearch", help="Safesearch level, strict, none or moderate", action="store", dest="safe")
	parser.add_argument("-t", "--type", help="Type of content; video, playlist or channel", action="store", dest="type")
	parser.add_argument("-d", "--dimension", help="The dimension of the video; 2d or 3d", action="store", dest="dimension")
	parser.add_argument("-x", "--definition", help="Video quality; high or standard", action="store", dest="definition")
	parser.add_argument("-l", "--length", help="Length of the video; short, medium, long", action="store", dest="duration")
	parser.add_argument("-a", "--after", help="Published after date, using format:1970-01-01", action="store", dest="after")
	parser.add_argument("-o", "--order", help="The order to sort by- date, rating, relevance, viewCount, title", action="store", dest="order")
	args = parser.parse_args()

	url='/youtube/v3/search?part=snippet&key=' + key
	safe='&safeSearch='
	results='&maxResults='
	content='&type='
	order='&order='
	defintion='&videoDefinition='	
	dimension='&videoDimension='
	duration='&videoDuration='
	after='&publishedAfter='

	if not len(sys.argv) > 1 and query == "blah" and afterdate == "blah":
       		print("An argument is required.")
       		parser.print_usage()
       		quit()
	if args.query:
		url = url + '&q=' + args.query
	if query != "blah":
		url = url + '&q=' + query
	if args.results:
		url = url + results + args.results
	if args.safe:
		url = url + safe + args.safe
	if args.type:
		url = url + content + args.type
	if args.order:
		url = url + order + args.order
	if args.definition:
		url = url + defintion + args.definition
	if args.dimension:
		url = url + dimension + args.dimension
	if args.duration:
		url = url + duration + args.duration
	if args.after:
		try:
			datetime.datetime.strptime(args.after, '%Y-%m-%d')
		except ValueError:	
			raise ValueError("Invalid date format for last update.  Should be YYYY-MM-DD")
		url = url + after + args.after + 'T00:00:00Z'
	if afterdate != "blah":
		url = url + after + afterdate + 'T00:00:00Z'
	if args.definition or args.dimension or  args.duration:
		url = url + content + 'video'
	return url

def api_req(url):	
        method = 'GET'
        headers = {"Accept": "image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/vnd.ms-powerpoint, application/vnd.ms-excel, application/msword, application/x-shockwave-flash, */*", "Accept-Language": "en-us", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; MANM; rv:11.0) like Gecko", "Connection": "Keep-Alive"}

        conn = http.client.HTTPSConnection('www.googleapis.com', context=ssl._create_unverified_context())
	
        conn.request(method, url, None, headers)

        httpResponse = conn.getresponse()

        decoded=httpResponse.read().decode('utf-8')

        response_dict=json.loads(decoded)

        if 'error' in response_dict:
                print(decoded)
                quit()
        return response_dict

def print_results(response_dict):
	x=0
	print ('Results of tubesearch query')
	print ('----------------------------------')

	count=len(response_dict['items'])

	while x < len(response_dict['items']):
		viddict=response_dict['items'][x]['id']
		if 'videoId' in viddict:
			print("Video Url: https://www.youtube.com/watch?v=" + str(viddict['videoId']))
		if 'playlistId' in viddict:
			print("Playlist Url: https://www.youtube.com/playlist?list=" + str(viddict['playlistId']))
		if 'channelId' in viddict:
			print("Channel Url: https://www.youtube.com/channel/" + str(viddict['channelId']))
		snipdict=response_dict['items'][x]['snippet']
		for k, v in snipdict.items():
			print(k +': ', v)
		print ('----------------------------------')
		x=x+1
	print ('Total number of results: ' + str(count))

def main():
    key=check_key()	
    url=construct_url(key)
    response_dict=api_req(url)
    print_results(response_dict)

if __name__ == "__main__":
    main()
	
