# TweetPi

TweetPi is a Python Script that allows you to upload and manage Tweets you want to post, and then post them in a timed schedule.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Although you can run this project in any UNIX-based system, I advise you to have this running on Raspbin Scratch.

### Prerequisites

Before you can have the program running, specfic package must be installed to have the program working properly. These package include....

* Tweepy
* Numpy
* Pandas
* Postfix
* Python-Crontab - optional



To install Tweepy, simply run this command:
```
pip install tweepy
```



To install Numpy, simply run this command:
```
pip install numpy
```



To install pandas, simply run this command:
```
pip install pandas
```
If you have any issues with pip installing pandas as it's known to get struck with the setup file, you can also run this command:
```
sudo apt-get install pandas
```
Note: It also helps to have numpy installed first to avoid pandas find the numpy package to install itself.



To install Postfix, simply run this command:
```
Sudo apt-get install postfix
```
Although it is not directly used, postfix allow you to fix an communication error with crontab, which prevent it from working.

Note: If you planned on using python-crontab, then postfix may not be needed, but it is still advised to be installed.

Optional:
To install Python-crontab, simply run this command:
```
pip install python-crontab
```

Once all of the necessary packages are installed, you may continue on with the Running process


### Installing

Once you get the packages installed, and running. The rest of the script simply depends on which version you want to run, the automatic one, or the manually one. 

I will go over the two version in their section

## The Manual Version

THe Manual Version simply requires you to run the python script. 

```
python script.py
```

Once you do, you will the welcome screen, and a main menu. The main menu will display to you some choices you can do, like

* Post a Random Tweet
* Display the Tweet Table
* How many Tweet do I have?
* Add an Tweet to the Table?

### Post a Random Tweet

Picks a random Tweet from the table, and post it to your Twitter Account. 

### Display the Tweet Table

Prints your Tweet Table to the terminal

### How many Tweet do I have?

Displays to you on how many Tweets in your table you still haven't posted yet

### Add an Tweet to the Table?

Allow you to add an Tweet to the Table. It will prompt you with a input request, asking you to enter the Tweet you want to add


## The Automatic Version

The Automatic Version uses the crontab on raspbin system to schedule the script(aka post the tweet) at specific times 

### Add a task with Crontab

To schedule a task, simply edit the cron table and add a scheduled task, with crontab format

To edit the cron table, run the following command

```
crontab -e
```

The first time you run this command, it will ask you to select your edit. Although I recommanded vim, please choose the editor you're comfortable with. 
(The editor can be changed later)

Once the editor opens the cron table, simply scroll down and add an task with using the following format:
```
m h  dom mon dow   command
```
* m (0 - 59) represents the minute you want it to run on
* h (0 - 23) represents the hour you want it to run on
* dom (1 - 31) represents the day of the month you want it to run on
* mon (1 - 12) represents the month you want it to run on
* dow (0 - 7) represents the day of the week you want it to run on. (0 to 6 are Sunday to Saturday, with 7 is Sunday, the same as 0)

For example:
```
0 0 * * *  /home/pi/backup.sh
```
This entry will run the backup.sh script every day at midnight

### View scheduled tasks

To view your currently saved scheduled tasks, run the following command:
```
crontab -l
```

For more information, read the following article on Cron:
[Scheduling task with Cron](https://www.raspberrypi.org/documentation/linux/usage/cron.md)

### Running the script

When using the automatic mode, run the script called, autoscript.py, instead of script.py

So a crontab entry could look like this

```
0 19 * * 1,5  cd /home/pi/TweetPi/ && python autoscript.py
```

NOTE: In order for the automatic version to work, you need to add tweets to the csv file, which can be done by running the manually version.


## Built With

* [Python](https://www.python.org/doc/) - The Script Langauge used
* [Tweepy](http://www.tweepy.org/) - The Python Library used to call the Twitter API
* [CSV](https://docs.python.org/3/library/csv.html) - Used to create the csv file
* [Pandas](https://pandas.pydata.org/) - Used to read and write to the csv file
* [Python- Crontab](https://pypi.org/project/python-crontab/) - Used to schedule the task the python script on your raspberry pi


## Authors

* **Hugo Renzzo Olcese** - *Everything* - [Renzzo98](https://github.com/Renzzo98?tab=repositories)

See also the list of [contributors](https://github.com/Renzzo98/TweetPi/contributors) who participated in this project.


## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
