import requests
import json
import csv
import facebook as fb
import networkx as nw

def main():

    access = {"EAAp5hvPqTZBcBAFcpwQx5Gc1i2TjdSjDOT4RgHxNPE9I5rXWMjArZAdyL2Ssx6KjlZCj6N5Vh2uUUfrZAMPM5kbOjHDPZASIMvdPulRZCe6UPkqu2Xc3mkrVMpT2YXCaiDGPAignKebMTedNDftlTt8XMNjjzWHREOzIAQfcTMRRMoWvX8j5z8N2gpy4ZCaqTLW4ZARZBgkE6hmZB4jVDjVBCzhzkOADhuxqdLvJcVER54ZASvw0tOAHjQuwdNvxHKrpXkZD"}
    graph = fb.GraphAPI(access)

    fields = [
        'message',
        'created_time',
        'description',
        'caption',
        'link',
        'place',
        'status_type'
    ]
    fields = ','.join(fields)
    posts = graph.get_connections('me', 'posts', fields = fields)

    while True:
        try:
            with open('posts.json1', 'a') as f:
                for post in posts['data']:
                    f.write(json.dumps(post)+"\n")
                posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            break
    

if __name__ == "__main__":
    main()