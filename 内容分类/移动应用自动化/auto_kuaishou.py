# -*- encoding=utf8 -*-
__author__ = "Lunar12"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir="E:/pyProject/移动应用自动化/pylog", devices=[
            "Android://127.0.0.1:5037/50fde3f2",
    ])


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath="E:/pyProject/移动应用自动化/pylog")