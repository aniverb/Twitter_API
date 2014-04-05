"""
easier, simpler way to access twitter api as opposed to urllib library from twitter stream and twitterinsults scripts
"""
import oauth2 as oauth
import twitter #pip install twitter first

consumer_key='OzjrZbLFpAfPTh4kvNzLA'
consumer_secret= 'Qf00IV2sQ9P2VukET7oOLVc1b1yXM5o5SBJE7H6g4'
token='924430736-AUxLlm5dqR2R8e8ibfRmvws0PQmJhXVrgoNfeGUc'
token_secret='zlx7yGP1vaT8boC4BMmcKgdMJEID0Wseq4RJpw028PuDB'

# Create your consumer with the proper key/secret.
consumer = oauth.Consumer(consumer_key, consumer_secret)
oauth_token = oauth.Token(key=token, secret=token_secret)

   
def recent_tweets(topic):   #must be in this format "#topic" or '@handle"
    t = twitter.Twitter(auth=twitter.OAuth(token, token_secret, consumer_key, consumer_secret))
    results=t.search.tweets(q=topic) #implicitly using url here https://dev.twitter.com/docs/api/1.1/get/search/tweets
    for post in results['statuses']: #here we are indexing into the json output as we would with a dictionary
        print post['text'].encode('utf-8')
        
#run this to see the json format 
'''
t = twitter.Twitter(auth=twitter.OAuth(token, token_secret, consumer_key, consumer_secret))
results=t.search.tweets(q=topic) #change q parameter to actual topic
results
'''
    
if __name__ == '__main__':
    recent_tweets('@GA') #change topic here
    recent_tweets('#pyladies')
