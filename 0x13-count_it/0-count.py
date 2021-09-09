#!/usr/bin/env python3
""" A script for counting hot terms on subreddits """
import json
import requests


def count_words(subreddit, word_list=[], after=''):
    """
    a recursive function that queries the Reddit API,
    parses the title of all hot articles, and prints a
    sorted count of given keywords (case-insensitive,
    delimited by spaces. Javascript should count as javascript,
    but java should not).

    Parameters:
        subreddit - the subreddit to search
        word_list - contains the same word (case-insensitive),
            the final count should be the sum of each duplicate
    """
    hot = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,after)
    headers = {'User-agent': 'Hot_List_App/0.0.1'}
    hot_request = requests.get(hot, headers=headers)
    hot_list = hot_request.json()

    if hot_list.get("data") and hot_list['data'].get('children'):
		children = hot_list.get("data").get("children")
		for child in children:
			word_list.append(child.get("data").get("title"))

		next_page = hot_list.get("data").get("after")
		if next_page:
			return count_words(subreddit, word_list, next_page)

	if word_list == []:
		return None
	return word_list
