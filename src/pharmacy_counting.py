#!/usr/bin/python
# -*- coding: utf-8 -*-

"""This script is main part for running phamacy counting"""
__author__ = "Tao Song"
__version__ = "0.3.4"
__email__ = "ts3089@columbia.edu"

from read_process_write import processing_pharmacy_data
import sys

#input_path = '../input/itcont.txt'
#output_path = '../output/top_cost_drug.txt'

def main():
    processing_pharmacy_data(sys.argv[1], sys.argv[2]) #Runs all the functions

#below code only runs when executed from command line
if __name__ == '__main__':
	main()