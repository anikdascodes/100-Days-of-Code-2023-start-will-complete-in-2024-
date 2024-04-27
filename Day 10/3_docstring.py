def format_name(f_name, l_name):
    """Take a first amd last name and format it
    to return the title case version of the name.""" # so for create docstring after define the function the next line we an use multiline comment to make docstring
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"



format_name()