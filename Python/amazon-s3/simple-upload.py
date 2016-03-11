#! venv/bin/python3.4
# -*- encoding: utf-8 -*-
"""
Script that uploads a file to a S3 bucket
"""
from json import load
from os import path
import boto3

def main():
    """
    Script's main function
    """
    script_dir = path.dirname(__file__)
    config = load(open(path.join(script_dir, 'config.json'), 'r'))
    access_key = config['amazon']['access_key']
    secret_key = config['amazon']['secret_key']

    client = boto3.client(
        's3',
        aws_access_key=access_key,
        aws_secret_access_key=secret_key,
    )
if __name__ == "__main__":
    main()
