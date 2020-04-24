# Extracting-Features-From-Tweets
This project help in extracting the general User and Content Features from Tweets:
About the project:

The code help in extractiong lots of general user and content features from Arabic tweets, the following is some explanation of some of the features.

•	Count of: (Mention in tweet, Chars in tweet text, Words in tweet text, Hashtags in tweet, Unique words, Unique chars , number of question marks “?” in tweet text, number of exclamation marks “!” in tweet text , number of Ellipse in tweet text , number of Special symbol ($!) in tweet..  , fo/fe: follower/ friends ration of the author, fe/fo  , Used url shortner: containing of url shortner if the tweet contains an url shortner )
•	tweet is a retweet(containing RT)
•	Day of week of publishing the tweet (Fri, Sat…),
•	Registration age of author when propagating the tweet (the dataset contains the two dates).
•	does the image  of the author (if has) hold a face
•	author’s tweet time spacing,
•	Average (tweets length of the author, urls/mentions ratio in tweets of the author, of hashtags of the author)
•	Retweet fraction of the author, listed count of the auther

you run the script.py to extract the features from Arabic Tweets using Python 2.7
You need to install following python libraries to run this script:
1) pyarabic
2) opencv-python

If you have already installed 'pip' then these libraries can be easily installed, just run following commands:

for windows:

pip install pyarabic
pip install opencv-python

for linux (ubuntu):

sudo pip install pyarabic
sudo pip install opencv-python

After installing the libraries, run this script:
python script.py

[NOTE: Don't remove "haarcascade_face_alt.xml" file. It is being used for face detection]
