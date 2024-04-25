def removezero_ip(ip):
    # Define a pattern to match one or more zeroes that are followed by a digit other than 0
    pattern = r'(?<=\.)(0+)(?=[1-9])'
    
    # Use re.sub to replace the matched pattern with an empty string
    corrected_ip = re.sub(pattern, '', ip)
    
    return corrected_ip
def check(candidate):
    assert removezero_ip("216.08.094.196")==('216.8.94.196')
    assert removezero_ip("12.01.024")==('12.1.24')
    assert removezero_ip("216.08.094.0196")==('216.8.94.196')

check(removezero_ip)