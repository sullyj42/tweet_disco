# Tweet Disco Guide

# Jeremiah Sullivan, Jingyi Li. EC601 Boston University, September 2019. 
## Use Cases
Twitter accounts should present an inherently non-stationary signal for a single. Over the life of an account (generally several years), users likely experience major life changes. These changes may exhibit themselves in the twitter feed. Observing changes in a particular user over time could provide insight to that users behavior over time. Perhaps this could be used to predict future behavior. 

This utility could be useful for a salesman dealing with a specific person (ie as a used car salesman I am interested if the person is becoming more stingy or more expensive).  

## User stories
Identify if the language is positive or negative

Input:  Comments from BU Twitter account // #boston… 
Output: Overall sentiment from the past month

MVP: A program that can accept an account/hashtag/… and (for a given time / something) output the overall sentiment (happy or sad)

## Architecture 


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
>> pip install --upgrade google-cloud-language
>> pip install --upgrade google-api-python-client
>> pip install oauth2client


## API Storage

In the interest in simplicity as the author can barely keep his eyes open, all API keys shall be stored in seperate ascii text (.txt) files. 
These files will be easy to read for an external program, but *shall* be ignored by git. 
This *shall* be ensured by appropriately building the ".gitignore" file. 

Similarly, any data (initial, intermediate, or final), *should* be stored in a seperate file and similarly ignored by the ".gitignore" file.  

## System Diagram 
![](tweet_diagram.png)
