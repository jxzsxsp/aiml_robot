# -*- coding: utf-8 -*-
"""
Author: Sean
Email: jxzsxsp@qq.com
GitHub: https://github.com/jxzsxsp
"""
import aiml
import sys
import os

from pip._vendor.distlib.compat import raw_input


def get_module_dir(name):
    path = getattr(sys.modules[name], '__file__', None)
    if not path:
        raise AttributeError('module %s has not attribute __file__' % name)
    return os.path.dirname(os.path.abspath(path))


def run():
    alice_path = get_module_dir('aiml') + '/botdata/alice'
    # 切换到语料库所在工作目录
    os.chdir(alice_path)

    alice = aiml.Kernel()
    alice.learn("startup.xml")
    alice.respond('LOAD ALICE')

    while True:
        print(alice.respond(raw_input("Enter your message >> ")))


if __name__ == '__main__':
    run()