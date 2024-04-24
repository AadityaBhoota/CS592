    ip_parts = ip.split('.')
    corrected_parts = [str(int(part)) for part in ip_parts]
    corrected_ip = '.'.join(corrected_parts)
    return corrected_ip

def check(candidate):
    assert removezero_ip("216.08.094.196")==('216.8.94.196')
    assert removezero_ip("12.01.024")==('12.1.24')
    assert removezero_ip("216.08.094.0196")==('216.8.94.196')

check(removezero_ip)