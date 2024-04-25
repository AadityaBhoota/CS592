def removezero_ip(ip):
    ip_parts = ip.split('.')
    clean_ip_parts = []

    for part in ip_parts:
        clean_ip_parts.append(str(int(part)))

    clean_ip = '.'.join(clean_ip_parts)
    return clean_ip

def check(candidate):
    assert removezero_ip("216.08.094.196")==('216.8.94.196')
    assert removezero_ip("12.01.024")==('12.1.24')
    assert removezero_ip("216.08.094.0196")==('216.8.94.196')

check(removezero_ip)