#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('3-hypermedia_del_pagination').Server

server = Server()

server.indexed_dataset()

try:
        server.get_hyper_index(300000, 100)
except AssertionError:
        print("AssertionError raised when out of range")        



index = 3
page_size = 2

print("Nb items: {}".format(len(server._Server__indexed_dataset)))
res = server.get_hyper_index(index, page_size)
print(res)

print(server.get_hyper_index(res.get('next_index'), page_size))

del server._Server__indexed_dataset[res.get('index')]
print("Nb items: {}".format(len(server._Server__indexed_dataset)))
print(server.get_hyper_index(index, page_size))
print(server.get_hyper_index(res.get('next_index'), page_size))
