#!/usr/bin/env python3
import os
import json

print("Content-Type: text/html\r\n\r\n")
print("<!doctype html><title>stan loona</title><h2>stan loona</h2>")

env = json.dumps(dict(os.environ))
# print(env)
print(os.environ["QUERY_STRING"])
print(os.environ["HTTP_USER_AGENT"])

