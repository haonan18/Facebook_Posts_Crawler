import requests
import json
import csv
import facebook as fb
import networkx as nw

def main():

    access = {"EAAp5hvPqTZBcBAELJNkR8CEXwezStTy6drTcnWAT4Kql9RSagZC6BQwZB09t7WBEZAo0h1xUt0zdd7Yp5Bxfp3pmOun1bWrLZAmTOQPk83VXZCOQUZBjXuTfNn3O0qzSSTbmKL1z3omLh6JZAV6CajQ1JEMyutFZCbT099FfDs3RZBvtArGZCVYpyqA"}
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