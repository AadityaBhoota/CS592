import re

def removezero_ip(ip):
    """
    Write a function to remove leading zeroes from an IP address.

    Examples:
    removezero_ip("216.08.094.196") == "216.8.94.196"
    removezero_ip("12.01.024") == "12.1.24"
    removezero_ip("216.08.094.0196") == "216.8.94.196"
    """
    # Split the IP address into its components
    parts = ip.split('.')
    
    # Remove leading zeroes from each part
    parts = [str(int(part)) for part in parts]
    
    # Join the parts back into a string
    return '.'.join(parts)

def check(candidate):
    assert removezero_ip("216.08.094.196")==('216.8.94.196')
    assert removezero_ip("12.01.024")==('12.1.24')
    assert removezero_ip("216.08.094.0196")==('216.8.94.196')

check(removezero_ip)