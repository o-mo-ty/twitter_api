print('Hello, world!')
print(1 + 2)


CONSUMER_KEY        = 'xHrAIV54bDkaSeLOhqDCHnPwh'
CONSUMER_SECRET_KEY = 'aoM5pmuXEVL3bTIjnD6lpAMgCt9zb1heM5z7T5GrrsCjuEXKGE'
ACCESS_TOKEN        = '1045256151187648512-aWTTlX0cj4SdSUtE4sIF1kgf1wf7Df'
ACCESS_TOKEN_SECRET = 'zGwbn3knGe650jNRRqbMeqZY0NPZGVakqIJJCDAYE50o3'
from twitter import *
t = Twitter(auth=OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET_KEY))

timelines = t.statuses.home_timeline()
for timeline in timelines:
    tl = '({id}) [{username}]:{text}'.format(
    id=timeline['id'], username=timeline['user']['name'], text=timeline['text'])
print (tl)
