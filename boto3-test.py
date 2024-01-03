"""
Service Interface - connections
"""
import boto3

session = boto3.session()

s3 = boto3.client('s3') # use more this option

s3 = session.client('s3') 

