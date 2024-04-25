def removezero_ip(ip):
    parts = ip.split('.')
    cleaned_parts = []
    for part in parts:
        cleaned_parts.append(str(int(part)))
    return '.'.join(cleaned_parts)

# Test cases




def check(candidate):
    assert removezero_ip("216.08.094.196")==('216.8.94.196')
    assert removezero_ip("12.01.024")==('12.1.24')
    assert removezero_ip("216.08.094.0196")==('216.8.94.196')

check(removezero_ip)