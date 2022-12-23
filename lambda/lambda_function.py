import boto3
import os
import numpy as np
import pandas as pd


def lambda_handler(event, context):
    df = pd.DataFrame({'num_legs': [2, 4, 8, 0],
                       'num_wings': [2, 0, 0, 0],
                       'num_specimen_seen': [8, 2, 5, 6]},
                      index=['sparrow', 'fox', 'spider', 'snake'])
    
    print(df)
    
    # return (success)
