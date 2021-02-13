import tweepy

CK="xHrAIV54bDkaSeLOhqDCHnPwh"
CS="CaoM5pmuXEVL3bTIjnD6lpAMgCt9zb1heM5z7T5GrrsCjuEXKGE"
AT="1045256151187648512-aWTTlX0cj4SdSUtE4sIF1kgf1wf7Df"
AS="zGwbn3knGe650jNRRqbMeqZY0NPZGVakqIJJCDAYE50o3"

auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)


api.update_status("a")
