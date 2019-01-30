#!/usr/bin/python3

import requests as req
import re

resp = req.get("http://www.wellcome to circleci demo.com")

content = resp.text

stripped = re.sub('<[^<]+?>', '', content)
print(stripped)
