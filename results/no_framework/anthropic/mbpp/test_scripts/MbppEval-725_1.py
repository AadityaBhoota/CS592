import re

def extract_quotation(text):
    """
    Extracts values between quotation marks " " of the given string.

    Examples:
    extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
    extract_quotation('Cast your "favorite" entertainment "apps"') == ['favorite', 'apps']
    extract_quotation('Watch content "4k Ultra HD" resolution with "HDR 10" Support') == ['4k Ultra HD', 'HDR 10']
    """
    return re.findall(r'"(.*?)"', text)

def check(candidate):
    assert extract_quotation('Cortex "A53" Based "multi" tasking "Processor"') == ['A53', 'multi', 'Processor']
    assert extract_quotation('Cast your "favorite" entertainment "apps"') == ['favorite', 'apps']
    assert extract_quotation('Watch content "4k Ultra HD" resolution with "HDR 10" Support') == ['4k Ultra HD', 'HDR 10']
    assert extract_quotation("Watch content '4k Ultra HD' resolution with 'HDR 10' Support") == []

check(extract_quotation)