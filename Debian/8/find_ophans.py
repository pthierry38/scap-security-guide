#!/usr/bin/python2

import sys
import os
import re
import glob


# The goal of this script is to find orphans rules that are in xccdf files
# and remove it/them
'''
This fonction find every xccdf file that are in the input/xccdf/
'''
def find_xccdf_files (folder_name, xccdf_list):
    for element in os.listdir(folder_name):
        if element.endswith('.xml'):
            find_oval_def(folder_name + '/' +  element, xccdf_list)
        else:
            find_xccdf_files(folder_name + '/' + element, xccdf_list)



'''
This fonction find every oval definition countainin the file_xccdf and add it
into the xccdf_list
'''
def find_oval_def (file_xccdf, xccdf_list):
    file_open = open (file_xccdf)
    for line in file_open:
        if "<oval id=" in line:
            #remove balises
            xccdf_list.append(get_oval_id(line))
    file_open.close()


'''
This fonction parse the line that countain the oval and return it
'''
def get_oval_id(line):
    right = 0
    left = -1
    for letter in line:
        if (letter == '"' and left < 0):
            right = right + 1
            left = right
            continue
        if (letter == '"' and right > 0):
            break
        right = right + 1
    return line[left: right] + ".xml"

def find_build_oval(folder_name, oval_list):
    for element in os.listdir(folder_name):
        if element.endswith('.xml'):
            oval_list.append(element)
        else:
            find_xccdf_files(folder_name + '/' + element, xccdf_list)



def main():
    if len(sys.argv) < 2:
        print "Usage : ./find_orphans name_of distribution target"
        sys.exit(1)

    oval_list = []
    xccdf_list = []
    build_dir = "build/" + sys.argv[1] + '_oval/'
    xccdf_directory = "input/xccdf/"

    find_build_oval(build_dir, oval_list)
    find_xccdf_files (xccdf_directory, xccdf_list)
    for element_build in oval_list:
        find = False
        for element_xccdf in xccdf_list:
            if (element_build == element_xccdf):
                find = True
        if not find:
            print element_build


if __name__ == "__main__":
    main()
