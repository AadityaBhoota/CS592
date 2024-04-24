def removezero_ip(ip):
    def remove_zero(match):
        return str(int(match.group(0)))

    pattern = r'\b0+(\d+)\b'
    result = re.sub(pattern, remove_zero, ip)
    return result

def check(candidate):
    assert removezero_ip("216.08.094.196")==('216.8.94.196')
    assert removezero_ip("12.01.024")==('12.1.24')
    assert removezero_ip("216.08.094.0196")==('216.8.94.196')

check(removezero_ip)