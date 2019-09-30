# Jeremiah Sullivan, Jingyi Li. EC601 Boston University, September 2019. 
## Product Definition

# Product Mission
Twitter accounts should present an inherently non-stationary signal. Observing changes in a particular user over time could provide insight to that users behavior over time. Perhaps this could be used to predict future behavior. 

# Target Users
The managers of Boston University: when Boston University has some activities or something happened, the managers can know the comments' sentiment easily in Twitter account, it also means they can know the students' attitude for one thing that happened in Boston University. So, it can help them to manage Boston University better. Also, it could be used to predict future behavior.

# User stories
Users can use this product to identify if the comments in the Twitter are positive or negative.

Input:  Comments from BU Twitter account // #boston… 

Output: Overall sentiment from the past month

# MVP
A program that can accept an account/hashtag/… and (for a given time / something) output the overall sentiment (happy or sad)

# Architecture 


## Introduction
This repository contains the code necessary for a simple twitter relationship query using the following libraries
> python-twitter

> Google Vision

>  Google NLP

## Installation guide

Perhaps make a make file, but for now... 

## Python-Twitter

>> pip install python-twitter

## Google Vision

## Google NLP
>> pip install --upgrade google-cloud-language -> https://pypi.org/project/google-cloud-language/
>> download API key
>> pip install --upgrade google-api-python-client
>> export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/[FILE_NAME].json"
>> pip install oauth2client


## API Storage

In the interest in simplicity as the author can barely keep his eyes open, all API keys shall be stored in seperate ascii text (.txt) files. 
These files will be easy to read for an external program, but *shall* be ignored by git. 
This *shall* be ensured by appropriately building the ".gitignore" file. 

Similarly, any data (initial, intermediate, or final), *should* be stored in a seperate file and similarly ignored by the ".gitignore" file.  

## System Diagram 
![](tweet_diagram.png)
