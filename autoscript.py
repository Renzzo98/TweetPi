import csv
import datetime
import random
import time
import tweepy
import config
import pandas as pd
from pandas import DataFrame, read_csv

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)



# Tweepy Helper Functions #


#Given a string, it will post it to Twitter
def updateStatus(statusMsg):
	auth.set_access_token(config.access_token_key, config.access_token_secret)
	api = tweepy.API(auth)
	api.update_status(status = statusMsg)


# System Helper Functions #



#Pick an random Quote, check if haven't been posted before, marked it posted in the df, and post it to Twitter
def postRandomQuote():
	Tweets = getList()
	randInt = pickRandomNum(Tweets)
	file = 'Tweets.csv'
	df = pd.read_csv(file)
	passed = False
	while (not passed):
		if (df.at[randInt,'POSTED'] == False):
			passed = True
		else:
			randInt = pickRandomNum(Tweets)
	msg = df.at[randInt,'MSG']
	print('Quote picked:')
	print(msg)
	print('...Posting...')
	markPosted(randInt)
	time.sleep(2)
	updateStatus(msg)


#Return the current date in Month-Day-Year Format
def getCurrentTime():
	now = datetime.datetime.now()
	time = now.strftime("%m-%d-%Y")
	return time


#Checks to make sure the message you want to save doesn't passed Twitter's character limit
def charLimit(msg):
	size = len(msg)
	if (size>280):
		return False
	else:
		return True


#Print the amount of Tweets I can post to the terminal
def getSize(list):
	size = len(list)
	return size


#Pick a random number from the list of Tweets
def pickRandomNum(list):
	size = getSize(list)
	randi = random.randint(0, size)
	print(randi)
	return randi


# CSV Helper Functions #



#Initalize an new CSV file and list
def initNewList():
	with open('Tweets.csv', mode = 'w') as TweetList:
		fieldnames = ['ID','DATE', 'MSG','POSTED']
		writer = csv.DictWriter(TweetList, fieldnames = fieldnames)
	
		writer.writeheader()
		writer.writerow({'ID': 0, 'DATE': '01-10-2018','MSG': 'HELLO WORLD', 'POSTED': False})
#Need to use only once!#


#Return the amount of rows in the DataFrame
def getDFSize(): 
	file = 'Tweets.csv'
	df = pd.read_csv(file)
	print len(df.index)


#Returns the ID of the last Tweet in the Dataframe
def getLastID():
	file = r'Tweets.csv'
	df = pd.read_csv(file)
	#print('Last ID', df['ID'].max())
	lastID = df['ID'].iloc[-1]
	result = int(lastID) + 1
	return result


#Return the Data Types of each column
def getTypeofField():
	file = 'Tweets.csv'
	df = pd.read_csv(file)
	print("TYPE OF ID IS", df['ID'].dtypes)
	print("TYPE OF DATE IS", df['DATE'].dtypes)
	print("TYPE OF MSG IS", df['MSG'].dtypes)
	print("TYPE OF POSTED IS", df['POSTED'].dtypes)


#Prints out the Dataframe in the terminal
def printList():
	file = 'Tweets.csv'
	df = pd.read_csv(file)
	print df


#Adds an new Row (Aka Quote) to the Dataframe and saves it to the csv file
def appendTweet(msg):
	time = getCurrentTime()
	CurID = getLastID()
	with open('Tweets.csv', mode = 'a') as TweetList:
		fieldnames = ['ID','DATE','MSG','POSTED']
		writer = csv.DictWriter(TweetList, fieldnames = fieldnames)
		writer.writerow({'ID': CurID, 'DATE': time, 'MSG': msg, 'POSTED': False}) 


#Ask for User Input for which quote to add then adds it using the AppendTweet Function
def manuallyAddTweet():
	msg = raw_input("\nWhat quote do you want to add?\n")
	checked = False
	while (not checked): #Checks to make sure the message in the Tweet doesn't past Twitter char limit
		if (charLimit(msg)):
			checked = True
		else:
			print ("Quote too big. Please Add an different one!")
			msg = raw_input("\nWhat quote do you want to add?\n")
	appendTweet(msg)


#Adds Removes an Row from the Dataframe and overwrites the csvFile 
def DropTweet(RowID):
	file = 'Tweets.csv'
	df = pd.read_csv(file)
	df.drop(df.index[RowID], inplace=True)
	print df
	df.to_csv('Tweets.csv', encoding='utf-8', index=False)
#THIS FUNCTION IS NOT NEEDED // SIMPLY CHANGE THE POSTED FIELD#


#Return the list of IDs(Tweets) that are not posted yet
def getList():
	file = 'Tweets.csv'
	df = pd.read_csv(file)
	list = df.index[~df['POSTED']].tolist()
	return list


#Given a row index, it will change its value in the POSTED field to True	
def markPosted(rowID):
	file = 'Tweets.csv'
	df = pd.read_csv(file)
	df.at[rowID,'POSTED'] = True
	df.to_csv('Tweets.csv', encoding='utf-8', index=False)


#Given a row index, it will change its value in the POSTED field to False
def mark_NOTPosted(rowID):
	file = 'Tweets.csv'
	df = pd.read_csv(file)
	df.at[rowID,'POSTED'] = False
	df.to_csv('Tweets.csv', encoding='utf-8', index=False)


# Main Application #



#Display the UI, welcoming the user to the application
def welcomeScreen():
	print( "                                          \n" +
		   "                                          \n" +
		   "                                          \n" +
		   " ***               *************          \n" +
		   " ******         ***********************   \n" +
		   " *********      *********************     \n" +
		   "  **********************************      \n" +
		   "    ************************************  \n" +
		   " ***********************************      \n" +
		   "  *********************************       \n" +
		   "    *******************************       \n" +
		   "  ********************************        \n" +
		   "   ******************************         \n" +
		   "      **************************          \n" +
		   "       ************************           \n" +
		   "******************************            \n" +
		   " **************************               \n" +
		   "   **********************                 \n" +
		   "      *************                       \n" +
		   "										  \n" +
		   " ###########  ########     ###########    \n" +
		   "     ##       ##     ##        ###        \n" +
		   "     ##       ##     ##        ###        \n" +
		   "     ##       ##     ##        ###        \n" +
		   "     ##       ########         ###        \n" +
		   "     ##       ##               ###        \n" +
		   "     ##       ##               ###        \n" +
		   "     ##       ##           ###########    \n" +
		   "                                          \n" 
		  
	)


#Display the Main Menu UI, displaying all of the choices that the user can do
def mainMenu():
	while (True):
		print("\nWhat would you like to do today? "+
			"\n1) Post a random quote for the day?"+
			"\n2) Check the current quote database?"+
			"\n3) How many Quotes do I have?" +
			"\n4) Add an quote to the database?"
		)
		decision = input("\n\nWhat is your choice?\n")
		if (decision > 4):
			raise NameError ('Incorrect Input')
		else:
			return decision


#Handles all of the user's decision from the main menu, and runs the functions needed
def decisionTree(choice):
	if (choice == 1):
		postRandomQuote()
	elif (choice == 2):
		printList()
	elif (choice == 3):
		TweetIDs = getList()
		print('You have ' + str(getSize(TweetIDs)) + ' Quotes left to post')
	else:
		manuallyAddTweet()






def main():
	decisionTree(1)
main()
