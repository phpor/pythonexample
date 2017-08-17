# encoding=utf-8

from SshTty import SshTty
import re


class Filter:

    def __init__(self):
        self.p_mobile_in_json = re.compile(r':(1\d{2})\d{4}(\d{4})([^0-9])', re.MULTILINE)
        self.p_mobile = re.compile(r'(1\d{2})\d{4}(\d{4})([^0-9]|\s|$)', re.MULTILINE)
        self.p_email = re.compile(r'([a-zA-Z0-9_\-.]{2})\S*(.@[a-zA-Z0-9]+\.\S+)', re.MULTILINE)
        self.p_card = re.compile(r'(\d{4})(\d{8,11})\d{4}', re.MULTILINE)

    def output_filter(self, s):
        s = re.sub(self.p_mobile_in_json, r':"\1****\2"\3', s)
        s = re.sub(self.p_mobile, r'\1****\2\3', s)
        s = re.sub(self.p_email, r'\1****\2', s)
        s = re.sub(self.p_card, r'\1\2****', s)

        return s

that = SshTty("172.16.22.37", 22, 'phpor', 'lijunjie')
that.set_output_filter(Filter().output_filter)
that.connect()


