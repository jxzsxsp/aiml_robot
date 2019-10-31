# -*- coding: utf-8 -*-
"""
Author: Sean
Email: jxzsxsp@qq.com
GitHub: https://github.com/jxzsxsp
"""
import aiml
import sys
import os


def get_module_dir(name):
    path = getattr(sys.modules[name], '__file__', None)
    if not path:
        raise AttributeError('module %s has not attribute __file__' % name)
    return os.path.dirname(os.path.abspath(path))


def run():
    chdir = os.path.join( aiml.__path__[0],'botdata','standard' )

    kernel = aiml.Kernel()
    kernel.bootstrap(learnFiles="startup.xml", commands="load aiml b", chdir=chdir)

    while True:
        print(kernel.respond(input("Enter your message >> ")))


if __name__ == '__main__':
    run()