# -*- coding: utf-8 -*-
"""
Author: Sean
Email: jxzsxsp@qq.com
GitHub: https://github.com/jxzsxsp
"""
import aiml
import os


def run():
    chdir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'botdata', 'xiaoyou')
    brain_path = os.path.join(chdir, 'xiaoyou.brn')
    kernel = aiml.Kernel()

    if os.path.isfile(brain_path):
        kernel.bootstrap(brainFile=brain_path)
    else:
        kernel.bootstrap(learnFiles="startup.xml", commands="load aiml c", chdir=chdir)
        kernel.saveBrain(brain_path)

    while True:
        in_msg = input('请输入对话>')
        if in_msg == 'exit()' or in_msg == '退出':
            break

        re_msg = kernel.respond(in_msg)
        print(re_msg)

if __name__ == '__main__':
    run()
