#/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys, getopt, os

# get current path
# https://blog.csdn.net/vitaminc4/article/details/78702852
current_path = os.path.split(os.path.realpath(__file__))[0]
# set working directory
os.chdir(current_path)

def generate_tag(keyword):
    return '{{'+keyword+'}}'

opts, args = getopt.getopt(sys.argv[1:], '-o:-s:-t:', ["output=", "origin_domain=", "new_domain_with_protocol="])

replace_dict = dict()

for opt_name, opt_value in opts:
    # output filename
    if opt_name in ('-o', '--output'):
        output_filename = opt_value
        # todo: print and log
        print("OUTPUT Filename: %s" % (output_filename))

    # origin_domain
    if opt_name in ('-s', '--origin_domain'):
        replace_dict['origin_domain'] = opt_value
        # todo: print and log
        print("origin domain: %s" % (replace_dict['origin_domain']))

    # new_domain_with_protocol
    if opt_name in ('-t', '--new_domain_with_protocol'):
        replace_dict['new_domain_with_protocol'] = opt_value
        # todo: print and log
        print("new domain with protocol: %s" % (replace_dict['new_domain_with_protocol']))

# remove htaccess file when origin_domain is -
if replace_dict['origin_domain'] == '-':
    if os.path.exists(output_filename):
        os.remove(output_filename)
    sys.exit()

template_filename = 'htaccess.tpl'

generated_lines = list()
with open(template_filename, 'r') as f:
    for line in f.readlines():
        for k, v in replace_dict.items():
            line = line.replace(generate_tag(k), v)
        generated_lines.append(line)

with open(output_filename, 'w') as f:
    f.writelines(generated_lines)
