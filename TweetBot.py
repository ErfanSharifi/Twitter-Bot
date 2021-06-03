import API_Credential as apic
import tweepy
#Hello
#goodmorning
#salam



class TweetBo():
    
    def __init__(self):

        pass

    def Authentication(self):
        
        obj = apic.API()
        credit = obj.Credential()

        auth = tweepy.OAuthHandler(credit[0], credit[1])
        auth.set_access_token(credit[2], credit[3])
        return auth


    def Post(self):
        
        obj = TweetBo()
        auth = obj.Authentication()
  
        api = tweepy.API(auth)

        statement = input("What do you want to post: ")

        api.update_status(statement)


    def Follow(self):

        obj = TweetBo()
        auth = obj.Authentication()

        api = tweepy.API(auth)

        screen_name = input("Who do you want to follow: ")

        api.create_friendship(screen_name)

    
    def Unfollow(self):

        obj = TweetBo()
        auth = obj.Authentication()
        
        api = tweepy.API(auth)
        screen_name = input("Who do you want to Unfollow: ")
        api.destroy_friendship(screen_name)


    def Comment(self):
        #Read Comments of specific tweet with tweet ID

        obj = TweetBo()
        auth = obj.Authentication()

        api = tweepy.API(auth)
        #Name of send tweet
        name = input("Who is owner of tweet: ")
        
        #ID's of specific tweet
        tweet_id = screen_name = input("Write tweet ID: ")



        replies=[]


        for tweet in tweepy.Cursor(api.search,q='to:'+name, result_type='recent', timeout=999999).items(1000):
            if hasattr(tweet, 'in_reply_to_status_id_str'):
                if (tweet.in_reply_to_status_id_str==tweet_id):
                    replies.append(tweet)
        with open('replies_clean.csv', 'w', encoding='utf-8') as f:
            csv_writer = csv.DictWriter(f, fieldnames=('user', 'text'))
            csv_writer.writeheader()
            for tweet in replies:
                row = {'user': tweet.user.screen_name, 'text': tweet.text.replace('\n', ' ')}
                print (row)
                csv_writer.writerow(row)


    def Hashtag(self):

        obj = TweetBo()
        auth = obj.Authentication()
        api = tweepy.API(auth, wait_on_rate_limit=True)

        #Search of specific Hashtag
        search_words = input("Which Hashtag you want to search: ")

        #Search from this date
        date_since = "2020-01-01"

        f = open("Hashtag.txt", "w", encoding= 'utf-8')

        for tweet in tw.Cursor(api.search, q=search_words, lang="fa", since=date_since).items(10):
            c =  ("Name:"), tweet.author.name.encode('utf8')
            b =  ("Screen-name:"), tweet.author.screen_name.encode('utf8')
            a = (("Text:"), tweet.text)

            c = str(c)
            b = str(b)
            a = str(a)

            f.write(c + '\r\n')
            f.write(b + '\r\n')
            f.write(a + '\r\n')

        f.close()



    def Count(self):

        #When you want search in resualt hashtag file for specific name

        with open('Hashtag.txt', 'r' , encoding="utf-8") as f:

            my_word = "@akramsharifi"
            count = 0

            # f1 = f.readlines()
            for line in f:
                print (line)
                if (my_word) in line:
                    count += 1
            print (my_word, count)


    def Follower(self):

        #extract list of followers of specific user

        obj = TweetBo()
        auth = obj.Authentication()
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

        user = api.get_user("ErfanSharify")
        screen_name = "khamenei_ir"
        c = api.followers(screen_name)

        p = open("Follower-List.txt", "w")
        for user in tweepy.Cursor(api.followers, screen_name = screen_name).items():
            print (user.screen_name)
            p.write(user.screen_name + "\r\n")
        p.close

    def TakeID(self):

        obj = TweetBo()
        auth = obj.Authentication()
        api = tweepy.API(auth)

        user = api.get_user("ErfanSharifi")
        user = user.id
        print (user)

    def TakeName(self):

        obj = TweetBo()
        auth = obj.Authentication()
        api = tweepy.API(auth)

        id = 57741058
        user = api.get_user(id) 
        screen_name = user.screen_name 
        print("The screen name of the user is : " + screen_name) 


def main():

    obj = TweetBo()
    obj.Authentication()


    print("""

    1)Post
    2)Follow
    3)Unfollow
    4)Comment
    5)Hashtag
    6)Count
    7)Follower
    8)Take user ID
    9)Take screen_name

    """)
    select = input("Please Choose:")
    if select == "1":

        obj = TweetBo()
        obj.Post()

    elif select == "2":
        obj = TweetBo()
        obj.Follow()
    
    elif select == "3":
        obj = TweetBo()
        obj.Unfollow()

    elif select == "4":
        obj = TweetBo()
        obj.Comment()

    elif select == "5":
        obj = TweetBo()
        obj.Hashtag()

    elif select == "6":
        obj = TweetBo()
        obj.Count()

    elif select == "7":
        obj = TweetBo()
        obj.Follower()

    else:
        input("Please choose corect number")
        main()
main()
