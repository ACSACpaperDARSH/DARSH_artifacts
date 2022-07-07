#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   main.py
@Time    :   2022/02/15 14:15:25
@Author  :   Shanto Roy 
@Version :   1.0
@Contact :   sroy10@uh.edu
@Desc    :   Main File
'''


from webclone import WebClone
import sys
import os

if __name__=="__main__":
    # base_url = "https://twentysixteendemo.wordpress.com/"
    base_url = "https://shantoroy.com/"
    # base_url = sys.argv[1]
    # base_url = "http://10.0.0.10"
    site_clone = WebClone(base_url) 
    site_clone.crawl_and_clone()
    print("\n\n\nNumber of Visited Urls:", len(site_clone.processed_urls))

    # rename index file to index.html
    # it stores the index.html as domain_name/ip with html section
    # for that, we need to rename the file
    # for 'http://' root folder -> "http:" 
    # for 'https://' root folder -> "https:" 
    # then there is a subfolder with the domain name
    path0, path1 = base_url[ : base_url.index(":")+1], base_url[base_url.index("/")+2 : ]
    path = os.path.join(path0, path1)
    # print(path,path0,path1)
    os.rename(os.path.join(path, path1.replace("/","") + ".html"), os.path.join(path, "index.html"))

