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

    s3 = boto3.session.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    ).resource('s3')

    buckets = s3.buckets.all()
    for bucket in buckets:
        print(bucket.name)

    s3.Bucket('

if __name__ == "__main__":
    main()
