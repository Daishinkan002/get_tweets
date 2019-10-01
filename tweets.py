
import sys
import tweepy



consumer_key = "Enter your api key"
consumer_secret = "Enter your secret key"
access_tokens_key = "Enter your access token key"
access_secret = "Enter your access secret key"



def Tweety_Handler(user,n):
	authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)
	authentication.set_access_token(access_tokens_key, access_secret)
	api = tweepy.API(authentication)


	database = []
	for tweet in tweepy.Cursor(api.user_timeline, screen_name = user).items(n):
		database.append([user,tweet.id_str,tweet.created_at,tweet.text.encode("utf-8")])


	filename = user + "_tweets.txt"
	print("writing to " + filename)
	with open(filename, 'w+') as file:
		for tweet in database:
			file.write(str(tweet))
			file.write("\n\n------------------------------------------------------ -------------------------------------------------\n\n")
        

if __name__ == '__main__':
    
    if len(sys.argv) == 2:
        n = int(input("Enter how many tweets u want  : "))
        Tweety_Handler(sys.argv[1],n)
    else :
        print("Error: enter one username alongside filename while compiling this program\n\n")
