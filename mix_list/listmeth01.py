#! /usr/bin/env python3

proto = ['ssh', 'http', 'https']

print(proto)

print(proto[1])

proto.extend('dns') # this will add dns

print(proto)
