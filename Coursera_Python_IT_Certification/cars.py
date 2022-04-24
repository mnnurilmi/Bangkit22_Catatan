import json
import locale
import sys
import reports
import os
import emails

def ambil_data(file):
    with open(file) as f:
        data = json.load(f)
    return data


