#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from wh_fronting.main import askLoki

def main():
    """"""
    return None


if __name__ == "__main__":
    inputSTR = "馬曉莉見過王曉明很多次"
    refDICT = {"FT": []}
    resultDICT = askLoki(inputSTR, refDICT=refDICT)
    print(resultDICT)