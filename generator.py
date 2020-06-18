#/usr/bin/env python
# -*- encoding: utf-8 -*-

template_filename = 'htaccess.tpl'
output_filename = 'output'

def generate_tag(keyword):
    return '{{'+keyword+'}}'

replace_dict = {
    'origin_domain': 'baidu.com',
    'new_domain_with_protocol': 'http://test.com'
}

generated_lines = list()
with open(template_filename, 'r') as f:
    for line in f.readlines():
        for k, v in replace_dict.items():
            line = line.replace(generate_tag(k), v)
        generated_lines.append(line)

with open(output_filename, 'w') as f:
    f.writelines(generated_lines)
