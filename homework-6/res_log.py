def total_count():
    return 225133

def total_get():
    return 122095

def total_head():
    return 528

def total_post():
    return 102503
    
def total_put():
    return 6

def top_10_request():
    dict = {'/administrator/index.php' : 103932, '/apache-log/access.log' : 26336, "'/'" : 6940,
    '/templates/_system/css/general.css' : 4980, '/robots.txt' : 3199, 
    'http://almhuette-raith.at/administrator/index.php' : 2356, '/favicon.ico' : 2201,
    '/wp-login.php' : 1644, '/administrator/' : 1563,
    '/templates/jp_hotel/css/template.css' : 1287} 

    return dict

def top_4xx_big():
    a = (404, 1417, '189.217.45.73', '/index.php?option=com_phocagallery&view=category&id=4025&Itemid=53')
    b = (404, 1417, '189.217.45.73', '/index.php?option=com_phocagallery&view=category&id=7806&Itemid=53')
    c = (404, 1417, '189.217.45.73', '/index.php?option=com_phocagallery&view=category&id=%28SELECT%20%28CASE%20WHEN%20%289168%3D4696%29%20THEN%209168%20ELSE%209168%2A%28SELECT%209168%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%29%20END%29%29&Itemid=53')
    d = (404, 1417, '189.217.45.73', '/index.php?option=com_phocagallery&view=category&id=%28SELECT%20%28CASE%20WHEN%20%281753%3D1753%29%20THEN%201753%20ELSE%201753%2A%28SELECT%201753%20FROM%20INFORMATION_SCHEMA.CHARACTER_SETS%29%20END%29%29&Itemid=53')
    e = (404, 1397, '104.129.9.248', '/index.php?option=com_easyblog&view=dashboard&layout=write')
    arr = [a,b,c,d,e]
    return arr

def top_5xx():
    dict = {'189.217.45.73' : 225, '82.193.127.15' : 4, '91.210.145.36' : 3, '194.87.237.6' : 2, '198.38.94.207' : 2}
    return dict
