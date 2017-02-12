#@ author = Pradeep shetty

# Final Project


# Below are the step which were followed To scrape data from IMDB website :http://m.imdb.com/feature/bornondate
# Installed selenium driver using PIP (pip install selenium)
# After installing selenium driver installed chrome web driver(latest version)
# The set up file of chrome web driver was saved in C:\Python27
# Then installed BeautifulSoup(bs4) package via pip installation
# Installed textblob package for sentiment analysis:   TextBlob is a Python (2 and 3) library for processing textual data.
# It provides a consistent API for diving into common natural language processing (NLP)
# tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, and more.





from selenium import webdriver  # Need To import webdriver from selenium package
from bs4 import BeautifulSoup as bs

driver = webdriver.Chrome()

driver.get("http://m.imdb.com/feature/bornondate")

html = driver.page_source
driver.close()

soup = bs(html, 'html5lib')
# print soup.prettify()
##for tags in soup.currentTag():
## print tags

##celeb_records = soup.find_all('a')
##for info in celeb_records:
## print info

## step 1 : Iterating through names of celebrities


celeb_name = []
name = soup.find_all('span', class_='title')

for info in name:
    # print info.text
    celeb_name.append(info.text)

## step 2 : Iterating through details of celebrities
# below are the list of celebrities detail

celeb_detail = []
detail = soup.find_all('div', class_="detail")
for details in detail:
    # print details.text
    celeb_detail.append(details.text)

celeb_images = []
images = soup.find_all('a', class_='poster')
for image in images:
    # print image.img["src"]
    celeb_images.append(image.img["src"])



print "Sentiment Analysis for Birthday Celebrities:"
print '--------------------------------------------------------------------------------------------'
print "Name of Celebrity , celebrity image , Profession and Best Work : "




def celebrities():
    print ' Celebrities Name:  ' + (celeb_name[0]), '\n', ' Profession : ' + (
    celeb_detail[0].split(',')[0]), '\n', ' Best Work : ' + (
    celeb_detail[0].split(',')[1]), '\n', ' Celebrity Image:' + (celeb_images[0]), '\n'
    print ' Celebrities Name:  ' + (celeb_name[1]), '\n', ' Profession : ' + (
    celeb_detail[1].split(',')[0]), '\n', ' Best Work : ' + (
    celeb_detail[1].split(',')[1]), '\n', ' Celebrity Image:' + (celeb_images[1]), '\n'
    print ' Celebrities Name:  ' + (celeb_name[2]), '\n', ' Profession : ' + (
    celeb_detail[2].split(',')[0]), '\n', ' Best Work : ' + (
    celeb_detail[2].split(',')[1]), '\n', ' Celebrity Image:' + (celeb_images[2]), '\n'
    print ' Celebrities Name:  ' + (celeb_name[3]), '\n', ' Profession : ' + (
    celeb_detail[3].split(',')[0]), '\n', ' Best Work : ' + (
    celeb_detail[3].split(',')[1]), '\n', ' Celebrity Image:' + (celeb_images[3]), '\n'
    print ' Celebrities Name:  ' + (celeb_name[4]), '\n', ' Profession : ' + (
    celeb_detail[4].split(',')[0]), '\n', ' Best Work : ' + (
    celeb_detail[4].split(',')[1]), '\n', ' Celebrity Image:' + (celeb_images[4]), '\n'
    print ' Celebrities Name:  ' + (celeb_name[5]), '\n', ' Profession : ' + (
    celeb_detail[5].split(',')[0]), '\n', ' Best Work : ' + (
    celeb_detail[5].split(',')[1]), '\n', ' Celebrity Image:' + (celeb_images[5]), '\n'
    print ' Celebrities Name:  ' + (celeb_name[6]), '\n', ' Profession : ' + (
    celeb_detail[6].split(',')[0]), '\n', ' Best Work : ' + (
    celeb_detail[6].split(',')[1]), '\n', ' Celebrity Image:' + (celeb_images[6]), '\n'
    print ' Celebrities Name:  ' + (celeb_name[7]), '\n', ' Profession : ' + (
    celeb_detail[7].split(',')[0]), '\n', ' Best Work : ' + (
    celeb_detail[7].split(',')[1]), '\n', ' Celebrity Image:' + (celeb_images[7]), '\n'
    print ' Celebrities Name:  ' + (celeb_name[8]), '\n', ' Profession : ' + (
    celeb_detail[8].split(',')[0]), '\n', ' Best Work : ' + (
    celeb_detail[8].split(',')[1]), '\n', ' Celebrity Image:' + (celeb_images[8]), '\n'
    print ' Celebrities Name:  ' + (celeb_name[9]), '\n', ' Profession : ' + (
    celeb_detail[9].split(',')[0]), '\n', ' Best Work : ' + (
    celeb_detail[9].split(',')[1]), '\n', ' Celebrity Image:' + (celeb_images[9]), '\n'
    # data = zip(celeb_detail, celeb_name)
    # print "Below are the list of celebrity names ,their profession  and Best Work:"
    # for sample in enumerate(data, +1):
    #     print list(sample)


def Final_Output():
    from textblob import TextBlob
    import tweepy

    ckey = 'please type your consumer key here '
    csecret = 'please type consumer secret here'

    atoken = 'please type access_token'
    asecret = 'please type access_token_secret'

    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    api = tweepy.API(auth)
    public_tweets = api.search(celeb_name[0])
    public_tweets1 = api.search(celeb_name[1])
    public_tweets2 = api.search(celeb_name[2])
    public_tweets3 = api.search(celeb_name[3])
    public_tweets4 = api.search(celeb_name[4])
    public_tweets5 = api.search(celeb_name[5])
    public_tweets6 = api.search(celeb_name[6])
    public_tweets7 = api.search(celeb_name[7])
    public_tweets8 = api.search(celeb_name[8])
    public_tweets9 = api.search(celeb_name[9])

    ####################################################################################
    # print "\n\n\n"

    # print "List of tweets for celebrity %s -> " % (celeb_name[0])
    for tweets in public_tweets:
        # print "***************************************"
        # print tweets.text
        analysis = TextBlob(tweets.text)
        # print "Tweet sentiment.polarity :", analysis.sentiment.polarity
        # print "Tweet sentiment.subjectivity :", analysis.sentiment.subjectivity

        # print '\n\n\n'

        # print "The sentiment analysis of this tweet for %s is:" % (celeb_name[0])
        #
        # if analysis.sentiment.polarity > 0:
        #     print  ['positive']
        # if analysis.sentiment.polarity == 0:
        #     print ['neutral']
        # if analysis.sentiment.polarity < 0:
        #     print ['negative']

    def Overall_sentiment():
        positive = analysis.sentiment.polarity > 0
        neutral = analysis.sentiment.polarity == 0
        negative = analysis.sentiment.polarity < 0

        if positive > negative:
            return "POSITIVE"

        elif positive < negative:
            return "NEGATIVE"
        else:
            return "NEUTRAL"

    # print '\n\n\n'

    tweet_zero = "The Overall sentiment for %s is :" % celeb_name[0], Overall_sentiment()


    # print "\n\n\n\n"

    #######################################################################################
    # print "List of tweets for celebrity %s -> " % (celeb_name[1])

    for tweets in public_tweets1:
        # print "***********************************"
        # print tweets.text
        analysis = TextBlob(tweets.text)
        # print "Tweet sentiment.polarity :", analysis.sentiment.polarity
        # print "Tweet sentiment.subjectivity :", analysis.sentiment.subjectivity

        # print '\n\n\n'

        # print "The sentiment analysis of this tweet for  %s is:" % (celeb_name[1])

        # if analysis.sentiment.polarity > 0:
        #     print 'positive'
        # if analysis.sentiment.polarity == 0:
        #     print 'neutral'
        # if analysis.sentiment.polarity < 0:
        #     print 'negative'

    def Overall_sentiment1():
        positive = analysis.sentiment.polarity > 0
        neutral = analysis.sentiment.polarity == 0
        negative = analysis.sentiment.polarity < 0

        if positive > negative:
            return "POSITIVE"

        elif positive < negative:
            return "NEGATIVE"
        else:
            return "NEUTRAL"

    # print '\n\n\n'

    tweet_first = "The Overall sentiment for %s is :" % celeb_name[1], Overall_sentiment1()


    # print "\n\n\n\n"

    #######################################################################################
    # print "List of tweets for celebrity %s -> " % (celeb_name[2])

    for tweets in public_tweets2:
        # print "***********************************"
        # print tweets.text
        analysis = TextBlob(tweets.text)
        # print "Tweet sentiment.polarity :", analysis.sentiment.polarity
        # print "Tweet sentiment.subjectivity :", analysis.sentiment.subjectivity

        # print '\n\n\n'

        # print "The sentiment analysis of this tweet for  %s is:" % (celeb_name[2])

        # if analysis.sentiment.polarity > 0:
        #     print 'positive'
        # if analysis.sentiment.polarity == 0:
        #     print 'neutral'
        # if analysis.sentiment.polarity < 0:
        #     print 'negative'

    def Overall_sentiment2():
        positive = analysis.sentiment.polarity > 0
        neutral = analysis.sentiment.polarity == 0
        negative = analysis.sentiment.polarity < 0

        if positive > negative:
            return "POSITIVE"

        elif positive < negative:
            return "NEGATIVE"
        else:
            return "NEUTRAL"

    # print '\n\n\n'

    tweet_second = "The Overall sentiment for %s is :" % celeb_name[2], Overall_sentiment2()


    # print "\n\n\n\n"

    #######################################################################################


    # print "List of tweets for celebrity %s -> " % (celeb_name[3])

    for tweets in public_tweets3:
        # print "***********************************"
        # print tweets.text
        analysis = TextBlob(tweets.text)
        # print "Tweet sentiment.polarity :", analysis.sentiment.polarity
        # print "Tweet sentiment.subjectivity :", analysis.sentiment.subjectivity

        # print '\n\n\n'

        # print "The sentiment analysis of this tweet for  %s is:" % (celeb_name[3])

        # if analysis.sentiment.polarity > 0:
        #     print 'positive'
        # if analysis.sentiment.polarity == 0:
        #     print 'neutral'
        # if analysis.sentiment.polarity < 0:
        #     print 'negative'

    def Overall_sentiment3():
        positive = analysis.sentiment.polarity > 0
        neutral = analysis.sentiment.polarity == 0
        negative = analysis.sentiment.polarity < 0

        if positive > negative:
            return "POSITIVE"

        elif positive < negative:
            return "NEGATIVE"
        else:
            return "NEUTRAL"

    # print '\n\n\n'

    tweet_third = "The Overall sentiment for %s is :" % celeb_name[3], Overall_sentiment3()


    # print "\n\n\n\n"

    #######################################################################################


    # print "List of tweets for celebrity %s -> " % (celeb_name[4])

    for tweets in public_tweets4:
        # print "***********************************"
        # print tweets.text
        analysis = TextBlob(tweets.text)
        # print "Tweet sentiment.polarity :", analysis.sentiment.polarity
        # print "Tweet sentiment.subjectivity :", analysis.sentiment.subjectivity

        # print '\n\n\n'

        # print "The sentiment analysis of this tweet for  %s is:" % (celeb_name[4])

        # if analysis.sentiment.polarity > 0:
        #     print 'positive'
        # if analysis.sentiment.polarity == 0:
        #     print 'neutral'
        # if analysis.sentiment.polarity < 0:
        #     print 'negative'

    def Overall_sentiment4():
        positive = analysis.sentiment.polarity > 0
        neutral = analysis.sentiment.polarity == 0
        negative = analysis.sentiment.polarity < 0

        if positive > negative:
            return "POSITIVE"

        elif positive < negative:
            return "NEGATIVE"
        else:
            return "NEUTRAL"

    # print '\n\n\n'

    tweet_fourth = "The Overall sentiment for %s is :" % celeb_name[4], Overall_sentiment4()


    # print "\n\n\n\n"

    #######################################################################################

    # print "List of tweets for celebrity %s -> " % (celeb_name[5])

    for tweets in public_tweets5:
        # print "***********************************"
        # print tweets.text
        analysis = TextBlob(tweets.text)
        # print "Tweet sentiment.polarity :", analysis.sentiment.polarity
        # print "Tweet sentiment.subjectivity :", analysis.sentiment.subjectivity

        # print "The sentiment analysis of this tweet for  %s is:" % (celeb_name[5])

        # if analysis.sentiment.polarity > 0:
        #     print 'positive'
        # if analysis.sentiment.polarity == 0:
        #     print 'neutral'
        # if analysis.sentiment.polarity < 0:
        #     print 'negative'

    def Overall_sentiment5():
        positive = analysis.sentiment.polarity > 0
        neutral = analysis.sentiment.polarity == 0
        negative = analysis.sentiment.polarity < 0

        if positive > negative:
            return "POSITIVE"

        elif positive < negative:
            return "NEGATIVE"
        else:
            return "NEUTRAL"

    # print '\n\n\n'

    tweet_fifth = "The Overall sentiment for %s is :" % celeb_name[5], Overall_sentiment5()


    # print "\n\n\n\n"

    #######################################################################################





    # print "List of tweets for celebrity %s -> " % (celeb_name[6])

    for tweets in public_tweets6:
        # print "***********************************"
        # print tweets.text
        analysis = TextBlob(tweets.text)
        # print "Tweet sentiment.polarity :", analysis.sentiment.polarity
        # print "Tweet sentiment.subjectivity :", analysis.sentiment.subjectivity

        # print "The sentiment analysis of this tweet for  %s is:" % (celeb_name[6])

        # if analysis.sentiment.polarity > 0:
        #     print 'positive'
        # if analysis.sentiment.polarity == 0:
        #     print 'neutral'
        # if analysis.sentiment.polarity < 0:
        #     print 'negative'

    def Overall_sentiment6():
        positive = analysis.sentiment.polarity > 0
        neutral = analysis.sentiment.polarity == 0
        negative = analysis.sentiment.polarity < 0

        if positive > negative:
            return "POSITIVE"

        elif positive < negative:
            return "NEGATIVE"
        else:
            return "NEUTRAL"

    # print '\n\n\n'

    tweet_sixth = "The Overall sentiment for %s is :" % celeb_name[6], Overall_sentiment6()


    # print "\n\n\n\n"

    #######################################################################################

    # print "List of tweets for celebrity %s -> " % (celeb_name[7])

    for tweets in public_tweets7:
        # print "***********************************"
        # print tweets.text
        analysis = TextBlob(tweets.text)
        # print "Tweet sentiment.polarity :", analysis.sentiment.polarity
        # print "Tweet sentiment.subjectivity :", analysis.sentiment.subjectivity

        # print "The sentiment analysis of this tweet for  %s is:" % (celeb_name[7])

        # if analysis.sentiment.polarity > 0:
        #     print 'positive'
        # if analysis.sentiment.polarity == 0:
        #     print 'neutral'
        # if analysis.sentiment.polarity < 0:
        #     print 'negative'

    def Overall_sentiment7():
        positive = analysis.sentiment.polarity > 0
        neutral = analysis.sentiment.polarity == 0
        negative = analysis.sentiment.polarity < 0

        if positive > negative:
            return "POSITIVE"

        elif positive < negative:
            return "NEGATIVE"
        else:
            return "NEUTRAL"

    # print '\n\n\n'

    tweet_seventh = "The Overall sentiment for %s is :" % celeb_name[7], Overall_sentiment7()


    # print "\n\n\n\n"

    #######################################################################################

    # print "List of tweets for celebrity %s -> " % (celeb_name[8])

    for tweets in public_tweets8:
        # print "***********************************"
        # print tweets.text
        analysis = TextBlob(tweets.text)
        # print "Tweet sentiment.polarity :", analysis.sentiment.polarity
        # print "Tweet sentiment.subjectivity :", analysis.sentiment.subjectivity

        # print "The sentiment analysis of this tweet for  %s is:" % (celeb_name[8])

        # if analysis.sentiment.polarity > 0:
        #     print 'positive'
        # if analysis.sentiment.polarity == 0:
        #     print 'neutral'
        # if analysis.sentiment.polarity < 0:
        #     print 'negative'

    def Overall_sentiment8():
        positive = analysis.sentiment.polarity > 0
        neutral = analysis.sentiment.polarity == 0
        negative = analysis.sentiment.polarity < 0

        if positive > negative:
            return "POSITIVE"

        elif positive < negative:
            return "NEGATIVE"
        else:
            return "NEUTRAL"

    # print '\n\n\n'

    tweet_eighth = "The Overall sentiment for %s is :" % celeb_name[8], Overall_sentiment8()


    # print "\n\n\n\n"

    #######################################################################################

    # print "List of tweets for celebrity %s -> " % (celeb_name[9])

    for tweets in public_tweets9:
        # print "***********************************"
        # print tweets.text
        analysis = TextBlob(tweets.text)
        # print "Tweet sentiment.polarity :", analysis.sentiment.polarity
        # print "Tweet sentiment.subjectivity :", analysis.sentiment.subjectivity

        # print "The sentiment analysis of this tweet for  %s is:" % (celeb_name[9])


        Overall_sentiment = []

        # if analysis.sentiment.polarity > 0:
        #     print 'positive'
        #
        # if analysis.sentiment.polarity == 0:
        #     print 'neutral'
        #
        # if analysis.sentiment.polarity < 0:
        #     print 'negative'

    def Overall_sentiment9():
        positive = analysis.sentiment.polarity > 0
        neutral = analysis.sentiment.polarity == 0
        negative = analysis.sentiment.polarity < 0

        if positive > negative:
            return "POSITIVE"

        elif positive < negative:
            return "NEGATIVE"
        else:
            return "NEUTRAL"

    # print '\n\n\n'

    tweet_ninth = "The Overall sentiment for %s is :" % celeb_name[9], Overall_sentiment9()


    # print "\n\n\n\n"

    print '++++++++++++++++++++++++++   Final  Output    +++++++++++++++++++++++++++++++++++++++++ '

    print ' Celebrities Name:  ' + (celeb_name[0]), '\n', ' Profession : ' + (
        celeb_detail[0].split(',')[0]), '\n', ' Best Work : ' + (
        celeb_detail[0].split(',')[1]), '\n', ' Celebrity Image:' + (celeb_images[0]), '\n', tweet_zero, '\n'

    print ' Celebrities Name:  ' + (celeb_name[1]), '\n', ' Profession : ' + (
        celeb_detail[1].split(',')[0]), '\n', ' Best Work : ' + (
        celeb_detail[1].split(',')[1]), '\n', ' Celebrity Image:' + (celeb_images[1]), '\n', tweet_first, '\n'

    print ' Celebrities Name:  ' + (celeb_name[2]), '\n', ' Profession : ' + (
        celeb_detail[2].split(',')[0]), '\n', ' Best Work : ' + (
        celeb_detail[2].split(',')[1]), '\n', ' Celebrity Image:' + (celeb_images[2]), '\n', tweet_second, '\n'

    print ' Celebrities Name:  ' + (celeb_name[3]), '\n', ' Profession : ' + (
        celeb_detail[3].split(',')[0]), '\n', ' Best Work : ' + (
        celeb_detail[3].split(',')[1]), '\n', ' Celebrity Image:' + (celeb_images[3]), '\n', tweet_third, '\n'

    print ' Celebrities Name:  ' + (celeb_name[4]), '\n', ' Profession : ' + (
        celeb_detail[4].split(',')[0]), '\n', ' Best Work : ' + (
        celeb_detail[4].split(',')[1]), '\n', ' Celebrity Image:' + (celeb_images[4]), '\n', tweet_fourth, '\n'

    print ' Celebrities Name:  ' + (celeb_name[5]), '\n', ' Profession : ' + (
        celeb_detail[5].split(',')[0]), '\n', ' Best Work : ' + (
        celeb_detail[5].split(',')[1]), '\n', ' Celebrity Image:' + (celeb_images[5]), '\n', tweet_fifth, '\n'

    print ' Celebrities Name:  ' + (celeb_name[6]), '\n', ' Profession : ' + (
        celeb_detail[6].split(',')[0]), '\n', ' Best Work : ' + (
        celeb_detail[6].split(',')[1]), '\n', ' Celebrity Image:' + (celeb_images[6]), '\n', tweet_sixth, '\n'

    print ' Celebrities Name:  ' + (celeb_name[7]), '\n', ' Profession : ' + (
        celeb_detail[7].split(',')[0]), '\n', ' Best Work : ' + (
        celeb_detail[7].split(',')[1]), '\n', ' Celebrity Image:' + (celeb_images[7]), '\n', tweet_seventh, '\n'

    print ' Celebrities Name:  ' + (celeb_name[8]), '\n', ' Profession : ' + (
        celeb_detail[8].split(',')[0]), '\n', ' Best Work : ' + (
        celeb_detail[8].split(',')[1]), '\n', ' Celebrity Image:' + (celeb_images[8]), '\n', tweet_eighth, '\n'

    print ' Celebrities Name:  ' + (celeb_name[9]), '\n', ' Profession : ' + (
        celeb_detail[9].split(',')[0]), '\n', ' Best Work : ' + (
        celeb_detail[9].split(',')[1]), '\n', ' Celebrity Image:' + (celeb_images[9]), '\n', tweet_ninth, '\n'



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#









if __name__ == '__main__':
    Final_Output()

    # user = input('Press any key to Close: ')
    # print user































