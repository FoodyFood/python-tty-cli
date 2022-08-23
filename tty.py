import os
import sys
import signal
from cmd import Cmd

class MyCli(Cmd):
    prompt = 'CLI> '
    intro = "CLI - Version 1.0 - FoodyFood \n? for Help, x to Exit\n"


    def do_list(self, inp):
        print("List of things You Have Access To:")
        print("\n")
    def help_list(self):
        print("List the things you have access to\n")


    def do_fetch(self, inp):
        print(f"Fetching: {inp}")
        print("\n")
    def help_fetch(self):
        print("Fetches something\n")


    def do_exit(self, inp):
        return True
    def help_exit(self):
        print('Exit CLI.')


    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
        print("Default: {}".format(inp))


def signal_handler(sig, frame):
    print('') # Empty on purpose, it formats better in terminal
    sys.exit(0)


if __name__ == '__main__':
    os.system('clear')
    signal.signal(signal.SIGINT, signal_handler)
    MyCli().cmdloop()