#!/usr/bin/env python
# coding: utf-8
#
# Set oracle as a custom command in config file.
# Eliane Araujo 2016

import sys
import tstlib

def add_command_oracle():
    config = tstlib.Config()
    if config.get('custom_commands') == None:
        config['custom_commands'] = {}
    if 'oracle' not in config.get('custom_commands').keys():
        config.get('custom_commands')['oracle'] = ['tst-oracle']
    
    config.save()
    
def main():
    add_command_oracle()
    return

if __name__ == "__main__":
    #just call main
    main ()