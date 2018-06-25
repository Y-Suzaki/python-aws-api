#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

def get(event, context): 
    response = {
        'statusCode': 200,
        'body': json.dumps([{ 'id':'10001', 'name':'tanaka' }, { 'id':'10002', 'name':'hayashi' }])
    }
    return response