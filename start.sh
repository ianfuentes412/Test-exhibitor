#!/bin/bash
pip3  install -r requirements.txt
python3 -m pytest --alluredir=allure-results tests/tests.py -v -s