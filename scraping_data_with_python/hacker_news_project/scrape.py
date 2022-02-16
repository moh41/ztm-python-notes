import requests
from bs4 import BeautifulSoup
import pprint

def sort_stories_by_votes(hn):
    return sorted(hn, key=lambda x: x["votes"], reverse=True)

def get_top_stories_from_hn():
    top_stories = []
    for i in range(10):
        r = requests.get(f"https://news.ycombinator.com/news?p={i}")
        soup = BeautifulSoup(r.text, "html.parser")
        links = soup.select(".titlelink")
        subtext = soup.select(".subtext")
        top_stories.extend(create_custom_hn(links, subtext))
    return sort_stories_by_votes(top_stories)

def create_custom_hn(links, subtext):
    hn = []
    for i, item in enumerate(links):
        title = item.getText()
        href = item.get("href", None)
        votes_count = subtext[i].select(".score")
        if len(votes_count):
            votes_count = int(votes_count[0].getText().replace(" points", ""))
            if votes_count > 99:
                hn.append({ "title": title, "href": href, "votes": votes_count })
    return hn

pprint.pprint(get_top_stories_from_hn())