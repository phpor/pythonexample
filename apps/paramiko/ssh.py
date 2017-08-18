# encoding=utf-8

from SshTty import SshTty
import re
import getpass
import sys, getopt


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


class FilterSsh:

    output_filter = None

    def __init__(self, output_filter=None):
        self.output_filter = output_filter

    @staticmethod
    def usage():
        print """Usage:        
        --help: show this help
        -h: host
        -p: port
        -U: user
        -P: password
        """
        return True

    def main(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:], "h:p:U:P:", ["help"])
        except getopt.GetoptError:
            FilterSsh.usage() and exit(1)

        for opt, arg in opts:
            if opt == '--help':
                FilterSsh.usage() and exit(1)
            elif opt == '-h':
                host = arg
            elif opt == '-p':
                port = int(arg)
            elif opt == '-U':
                user = arg
            elif opt == '-P':
                password = arg

        that = SshTty(host, port, user, password)
        that.set_output_filter(self.output_filter)
        # 环境变量需要在sshd中明确配置为Accept
        that.set_env({"SSH_USER":getpass.getuser(), "SSH_USER_ROLE": "user"})
        that.connect()


FilterSsh(Filter().output_filter).main()