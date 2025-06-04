import re

def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    # First, replace 3 or more consecutive spaces with a single hyphen.
    # The `+` makes it match one or more, so `{3,}` ensures 3 or more.
    text = re.sub(r' {3,}', '-', text)
    
    # Then, replace any remaining single or double spaces with underscores.
    # This step will also handle the cases where there were originally 1 or 2 spaces.
    text = text.replace(' ', '_')
    
    return text