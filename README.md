# tubesearch
Python script using the YouTube Data List API to search through videos.  Requires a Google API Key  

Create an API key at https://console.developers.google.com/apis 

Then add it to a file in your home directory ($HOME) named .google_key.

**Arguments:**

<table>
<thead>
<tr>
<th>-h, --help</th>                  
<th>Show this help message and exit</th> 
<tr>
<th>-q QUERY, --query QUERY</th>         
<th>Search terms separated by '+'.  example: -q pop+music.</th>
</tr>
<th>-r RESULTS, --results RESULTS       
<th>The number of items returned from 0 to 50 (default is 5)
</tr>
<th>-s SAFE, --safesearch SAFE     
<th>Safesearch level, strict, none or moderate (default is none)
</tr>
<th>-t TYPE, --type TYPE        
<th>Type of content; video, playlist or channel (default is any)
</tr>
<th>-d DIMENSION, --dimension DIMENSION 
<th>The dimension of the video; 2d or 3d (default is either)
</tr>
<th>-x DEFINITION, --definition DEFINITION
<th>Video quality; high or standard. (default is either)
</tr>
<th>-l DURATION, --length DURATION      
<th>Length of the video; short, medium, long. (defaults is any)
</tr>
<th>-o ORDER, --order ORDER         
<th>The order to sort by- date, rating, relevance, viewCount, title (default is relevance)
</tr>
<th>-a DATE, --after DATE
<th>Show content published after the listed date, using format:1970-01-01
</tr>
</table>

