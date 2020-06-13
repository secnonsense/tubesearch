# tubesearch
Python script using the YouTube Data List API to search through videos.  Requires a Google API Key  

Create an API key at https://console.developers.google.com/apis 

Then add it to a file in your home directory ($HOME) called .google_key.

Arguments:

  -h, --help                  Show this help message and exit  
  -q QUERY, --query           Search terms separated by '+'.  example: -q pop+music.   
  -r RESULTS, --results       The number of items returned from 0 to 50  
  -s SAFE, --safesearch       Safesearch level, strict, none or moderate  
  -t TYPE, --type TYPE        Type of content; video, playlist or channel  
  -d DIMENSION, --dimension   The dimension of the video; 2d or 3d  
  -x DEFINITION, --definition Video quality; high or standard  
  -l DURATION, --length       Length of the video; short, medium, long  
  -o ORDER, --order           The order to sort by- date, rating, relevance,viewCount, title  
