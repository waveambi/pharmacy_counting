#!/usr/bin/python
# -*- coding: utf-8 -*-

"""This script is for running data processing in text file level"""
__author__ = "Tao Song"
__version__ = "0.2.2"
__email__ = "ts3089@columbia.edu"

from help_functions import clean_string, process_line

def load_and_process_data(input_path):
    """load data and compute cost and num of doctors
    input: path of input raw log files
    output: drug cost dict {drug: [total_cost, set(doctors)]}
    """
    drug_cost = {}
    with open(input_path, 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = clean_string(line) # remove , within quoted string
            line_split = line.split(",")
            if len(line_split) == 5:
                drug_cost = process_line(line_split, drug_cost) #calculate cost and doctor set
    return drug_cost

def dict_to_list(drug_cost):
    """convert from dictionary to list
    input: drug cost dict
    output: sorted drug cost list [drug, prescriber num, total cost]
    """
    drug_cost_list = []
    for record in drug_cost:
        drug_cost_list.append([record, len(drug_cost[record][1]), drug_cost[record][0]]) 
    drug_cost_list.sort(key=lambda x: (-x[2], x[0])) #sorting by cost and drug name
    return drug_cost_list

def write_to_text(output_path, drug_cost_list):
    """write data into text file
    input: drug cost list and output directory"""
    with open(output_path, 'w') as f:
        f.write('drug_name,num_prescriber,total_cost\n')
        i = 1
        for items in drug_cost_list:
            for item in items:
                if i % 3 == 0:
                    f.write("%s\n" % int(round(item, 0)))
                else:
                    f.write("%s," % item)
                i += 1

def processing_pharmacy_data(input_path, output_path):
    """ensemble all functions
    input: path of raw text file, output directory"""
    drug_cost = load_and_process_data(input_path)
    drug_cost_list = dict_to_list(drug_cost)
    write_to_text(output_path, drug_cost_list)
