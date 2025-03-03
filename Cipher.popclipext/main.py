#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import jsbeautifier

selected_text = os.getenv("POPCLIP_TEXT")

res = jsbeautifier.beautify(selected_text)

print(res)