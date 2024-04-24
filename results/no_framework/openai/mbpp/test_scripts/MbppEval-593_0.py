import re

def removezero_ip(ip):
    def remove_zero(match):
        return str(int(match.group(0)))

    return re.sub(r'\b0+(\d+)', remove_zero, ip)

# Test cases




def check(candidate):
    assert removezero_ip("216.08.094.196")==('216.8.94.196')
    assert removezero_ip("12.01.024")==('12.1.24')
    assert removezero_ip("216.08.094.0196")==('216.8.94.196')

check(removezero_ip)