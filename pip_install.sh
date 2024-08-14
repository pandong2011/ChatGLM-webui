#!/bin/bash
ph=$1
if [ph == 'dev']; then
  cd venv/bin
  pwd
  ./pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r ../../requirements.txt
else
  pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
fi
