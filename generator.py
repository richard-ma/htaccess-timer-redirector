#/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys, getopt

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


template_filename = 'htaccess.tpl'

generated_lines = list()
with open(template_filename, 'r') as f:
    for line in f.readlines():
        for k, v in replace_dict.items():
            line = line.replace(generate_tag(k), v)
        generated_lines.append(line)

with open(output_filename, 'w') as f:
    f.writelines(generated_lines)
