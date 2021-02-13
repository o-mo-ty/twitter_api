# -*- coding: utf-8 -*-
import tweepy
import time

# consumer　第一引数に(consumer　key)　第二引数に(consumer　secret) #
auth = tweepy.OAuthHandler("drB1mNOwKnuXFZoDEWp0318BS","MK8IEPeeZblAu5FQPAOw7y1ZN5bwXO10DOJ7tTudJVvAXU5335")
# ACCESS_TOKEN_KEY 第一引数に(Access token)　第二引数に(Access token secret) #
auth.set_access_token("1045256151187648512-Bp3OzwMjGyEsDtVnrIGNJYWQHXz4f2", "vldfuG1Vk5DJN1OyBkRr7kCSSDelDEpMAef6mE4XPFeov")

# wait_on_rate_limit = レート制限が補充されるのを自動的に待つかどうか #
# wait_on_rate_limit_notify = Tweepyがレート制限の補充を待っているときに通知を出力するかどうか #
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


# '#ブログ, #旅行'をそれぞれ３件ずついいね #
# 取得したいキーワード #
search_list = ['#美男美女と繋がりたい', '#いいねした人全員フォロー','#雰囲気嫌いじゃないよって人いいね']
# ツイート数３件 #
tweet_count = 8

for search in search_list:
    print('Searching... {}' .format(search))
    # サーチ結果 #
    search_result = api.search(q=search, count=tweet_count)
    for tweet in search_result:
        tweet_id = tweet.id
        try:
            # いいねの処理 #
            api.create_favorite(id=tweet_id)
            print('Tweet_liked')
            time.sleep(4)
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break
