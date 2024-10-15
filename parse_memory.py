
import string
import sys
import json


import logging
logging.basicConfig(level=logging.DEBUG)

from tools import valid_ip, write2file



WHITE_SPACE = " "

in_file = sys.argv[1]
# out_file = sys.argv[2]
logging.info("Input file: " + in_file)
prefix = in_file.split(".")[0]
PRINTABLE_FILE = prefix + "_out.log"
IPADDR_FILE = prefix + "_IPLIST.log"


def containIPDomains(line):
    is_valid = False
    lc_line = line.lower()
    if "list" in lc_line or "[" in line or "]" in line or "{" in line or "}" in line:
        is_valid = True
    else:
        items = line.split('"')
        for item in items:
            if valid_ip(item):
                is_valid = True
                break

        items2 = line.split(WHITE_SPACE)
        for item in items2:
            if ":" in item:
                item = item.split(":")[0]
            if valid_ip(item):
                is_valid = True
                break

    if is_valid is False:
        logging.debug("Invalid Line::::" + line)
    return is_valid


def parseIPFromString(lines):
    addr_set = set()
    # lines = content.split("\n")
    for line in lines:
        new_line = line.replace("\\", "")
        items = new_line.split('"')
        for data in items:
            if valid_ip(data):
                addr_set.add(data)
    write2file(addr_set, IPADDR_FILE)
    
    return addr_set


def obtainPrintables():
    logs_set = set()

    printable = set(string.printable)
    with open(in_file, "r") as f:
        new_line = ""
        for line in f:
            line = line.strip().strip("\t")
            if not containIPDomains(line):
                continue
            
            iter = filter(lambda x: x in printable, line)
            prior_char=None
            for s in iter:
                # remove continuous white space
                if s == WHITE_SPACE and prior_char == WHITE_SPACE:
                    prior_char = s
                    continue
                new_line += s
                prior_char = s
            
        striped_line = new_line.replace("\\", "")
        logs_set.add(striped_line)

    write2file(logs_set, PRINTABLE_FILE)
    
    return logs_set


def extract_ipaddr_from_printable_strings():
    content = obtainPrintables()



if __name__ == "__main__":
    logs_set = obtainPrintables()
    parseIPFromString(logs_set)
