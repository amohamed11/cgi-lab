#!/usr/bin/env python3
import os
import json

env = json.dumps(dict(os.environ))
print(env)
