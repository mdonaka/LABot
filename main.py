"""For local"""
import os
import sys
from os.path import join, dirname
from dotenv import load_dotenv
os.chdir("./lambda_dir/")

from lambda_dir.lambda_function import lambda_handler

if __name__ == "__main__":
    load_dotenv(verbose=True)

    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    lambda_handler({}, {})
