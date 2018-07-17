#!/usr/bin/python
# -*- coding: utf-8 -*-

"""This script is for running cleaning and processing function in text line level"""
__author__ = "Tao Song"
__version__ = "0.1.6"
__email__ = "ts3089@columbia.edu"

import re

def clean_string(text):
    """function for pre-cleaning string
    input: raw single line text string
    output: single line text string without , in quoted
    """
    text = re.sub(r',(?=[^"]*"[^"]*$)', " ", text)
    return text

def process_line(splits, drug_sales):
    """function for building dict {drug: [total_cost, set(doctors)]}
    input: list of single line text splits, drug_sales dict
    output: updated or created drug_sales dict
    """
    if splits[3] not in drug_sales:
        drug_sales[splits[3]] = [0, set()]
    drug_sales[splits[3]][0] += float(splits[4].strip('\n'))
    drug_sales[splits[3]][1].add(splits[1] + splits[2])
    return drug_sales