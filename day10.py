# Functions With Outputs

def format_name(first_name, last_name):
    """ Takes a first and last name and format it to return the title case version of the name."""
    if first_name == '' or last_name == '':
        return 'You didn\'t provide valid inputs'
    f_name = first_name.title()
    l_name = last_name.title()
    return f"{f_name} {l_name}"


formatted_string = format_name(first_name=input('What is your first name? '), last_name=input('What is your last name? '
                                                                                              ))
print(formatted_string)
