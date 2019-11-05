import boto3
import os
from base64 import b64decode

def decode(ENCRYPTED):
    DECRYPTED = boto3.client('kms').decrypt(CiphertextBlob=b64decode(ENCRYPTED))['Plaintext']
    return DECRYPTED
