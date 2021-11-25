EMAIL = 'daahaaa@icloud.com'
PASSWORD = '_5Z4GUeDFwL5WAr'

def payload_segment(segment_name):
    return  {    
            'name': segment_name,
            'pass_condition': 1,
            'relations': [
            {'object_type': 'remarketing_player',
                'params': 
                {
                    'type': 'positive',
                    'left': 365,
                    'right': 0}}]}

def payload_campaign(name_company):
    return {
            'name': name_company,
            'objective': 'reach',
            'package_id': '960'}