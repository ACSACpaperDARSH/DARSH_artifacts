#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   webclone.py
@Time    :   2022/02/15 14:13:22
@Author  :   Shanto Roy 
@Version :   1.0
@Contact :   sroy10@uh.edu
@Desc    :   This project is about website cloning
'''


from fileinput import filename
from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from urllib.parse import urlparse
from collections import deque
# import urllib2
import os
from pathlib import Path


class WebClone:

    def __init__(self, url) -> None:
        # get the base url
        self.url = url

        # a queue of urls to be crawled next
        self.new_urls = deque([url])

        # a set of urls that we have already processed 
        self.processed_urls = set()

        # a set of domains inside the target website
        self.local_urls = set()

        # a set of domains outside the target website
        self.foreign_urls = set()

        # a set of broken urls
        self.broken_urls = set()

        # count the current number of visited page
        self.count = 0


    # file creation
    def file_creation(self,target_url):
        # get the filename
        list_of_files = target_url.split("/")
        if list_of_files[-1] == "":
            filename = list_of_files[-2] + ".html"
            list_of_files = list_of_files[:-1]
        else:
            filename = list_of_files[-1] + ".html"
        #print(filename)

        # extract directories and subdirectories
        if target_url.startswith("http"):
        # or if list_of_files[0].startswith("http")
            # leave the first 3 items -> ['https:','','something.wordpress.com',]
            # also leave the last item (filename)
            dir_list = list_of_files[3:-1]

        # join all the directories except the filename
        # for the index.html target_dir will have 0 contents
        # to handle that, let's make it False if lenth of target_dir is 0
        if len(dir_list) > 0:
            target_dir = os.path.join(*dir_list)
        else:
            target_dir = False

        # if nested directories do not exist, create the directories
        # macOS supports upto 1016 characters, 1017 fails
        # for now let's just approve something less than 500
        threshold = 500

        # create the parent directory named after the domain
        if not os.path.exists(self.url):
            try:
                os.makedirs(self.url)
            except OSError as e:
                pass
        
        # if nested directory join the sub-directories, else the parent one
        if target_dir != False:
            full_dir = os.path.join(self.url,target_dir)
        else:
            full_dir = self.url

        # make directories
        if not os.path.exists(full_dir):
            if len(full_dir) < threshold:
                try:
                    os.makedirs(full_dir)
                except OSError as e:
                    pass
        

        filepath = os.path.join(full_dir,filename)

        # check once again the total path size
        cwd = os.getcwd()
        abs_path = os.path.join(cwd,filepath)

        return filepath if len(abs_path) < threshold else False


    # save webpage with contents
    def save_webpage_without_change(self,response,filename):
        content = response.content
        f = open(filename, 'wb')
        f.write(content)
        f.close


    # crawl through all local links
    def crawl_and_clone(self):
        # process urls one by one until we exhaust the queue
        while len(self.new_urls):    
            # move url from the queue to processed url set    
            self.url = self.new_urls.popleft()    
            self.processed_urls.add(self.url)    
            # print the current url  
            print("\nProcessing %s" % self.url)
            self.count += 1
            print("# of Visited Pages:", self.count)
            
            try:    
                response = requests.get(self.url)
                get_absolute_path = self.file_creation(self.url)
                if get_absolute_path:
                    self.save_webpage_without_change(response,get_absolute_path)
            except(requests.exceptions.MissingSchema, requests.exceptions.ConnectionError,\
                                requests.exceptions.InvalidURL, requests.exceptions.InvalidSchema):    
                # add broken urls to it’s own set, then continue    
                self.broken_urls.add(self.url)    
                continue
                
            # extract base url to resolve relative links
            parts = urlsplit(self.url)
            base = "{0.netloc}".format(parts)
            strip_base = base.replace("www.", "")
            base_url = "{0.scheme}://{0.netloc}".format(parts)
            path = self.url[:self.url.rfind('/')+1] if '/' in parts.path else self.url
            
            
            # Initialize BeautifulSoup to process the HTML document
            soup = BeautifulSoup(response.text, "lxml")
            for link in soup.find_all('a'):    
                # extract link url from the anchor    
                anchor = link.attrs["href"] if "href" in link.attrs else ''
                if anchor.startswith('/'):        
                    local_link = base_url + anchor        
                    self.local_urls.add(local_link)    
                elif strip_base in anchor:        
                    self.local_urls.add(anchor) 
                else:        
                    self.foreign_urls.add(anchor)
                
            for i in self.local_urls:    
                if not i in self.new_urls and not i in self.processed_urls:        
                    self.new_urls.append(i)
 
