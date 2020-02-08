# -*- coding: utf-8 -*-
'''
@Time    : 2020/2/6 11:05 下午
@Author  : XJ.LV
@FileName: test.py
@Software: PyCharm
'''


import sentencepiece as spm

#构建词表 --input 输入文件  --model_prefix 输出路径及文件前缀
spm.SentencePieceTrainer.train('--input=/Users/edz/temp/DATA/clean3.en --model_prefix=/Users/edz/temp/DATA/en --vocab_size=50000')


