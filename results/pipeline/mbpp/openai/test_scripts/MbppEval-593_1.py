def remove_leading_zeroes(component):
    return str(int(component))

def removezero_ip(ip):
    components = ip.split(".")
    components_no_zeroes = [remove_leading_zeroes(component) for component in components]
    modified_ip = ".".join(components_no_zeroes)
    
    return modified_ip

def check(candidate):
    assert removezero_ip("216.08.094.196")==('216.8.94.196')
    assert removezero_ip("12.01.024")==('12.1.24')
    assert removezero_ip("216.08.094.0196")==('216.8.94.196')

check(removezero_ip)