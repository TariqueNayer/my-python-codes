from operator import itemgetter
from pathlib import Path
import requests
import json

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
    #Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    
    #Build a dictionary for each article.
    submission_dict = {
    'Title': response_dict.get("title",0),
    'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
    'comments': response_dict.get('descendants',0),
    }
    submission_dicts.append(submission_dict)
    
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse= True)

# Write a JSON file.
jfile = json.dumps(submission_dicts, indent=4)

path = Path(r"C:\Users\personal\Desktop\python\Networking\Hacker_news_top_commented.json")
path.write_text(jfile)