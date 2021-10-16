import requests
import pytest

url_ddg = "https://api.duckduckgo.com/?q="

@pytest.mark.parametrize("president",
                         ["Washington", "Adams", "Jefferson", "Madison", "Monroe",
                          "Jackson", "Van Buren", "Harrison", "Tyler", "Polk",
                          "Taylor", "Fillmore", "Pierce", "Buchanan", "Lincoln",
                          "Johnson", "Grant", "Hayes", "Garfield", "Arthur",
                          "Cleveland", "McKinley", "Roosevelt", "Taft", "Wilson",
                          "Harding", "Coolidge", "Hoover", "Truman", "Eisenhower",
                          "Kennedy", "Nixon", "Ford", "Carter", "Reagan",
                          "Bush", "Clinton", "Obama", "Trump", "Biden"])
def test_presidents(president):
    resp = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json")
    rsp_data = resp.json()
    related_topics = rsp_data['RelatedTopics']
    for i in range(len(related_topics)):
        assert president in related_topics
