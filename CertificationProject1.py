def add_setting(settings,tpl) :
        key=tpl[0].lower()
        value=tpl[1].lower()
        if key in settings:
            return f'Setting \'{key}\' already exists! Cannot add a new setting with this name.'
        settings[key]=value
        return f'Setting \'{key}\' added with value \'{value}\' successfully!'
         
def delete_setting(settings,key):
    key=key.lower()
    if key in settings:
        del settings[key]
        return f'Setting \'{key}\' deleted successfully!'
    return 'Setting not found!'
def update_setting(settings,tpl):
    key=tpl[0].lower()
    value=tpl[1].lower()
    if key in settings:
        settings[key]=value
        return f'Setting \'{key}\' updated to \'{value}\' successfully!'
    return f'Setting \'{key}\' does not exist! Cannot update a non-existing setting.'


def view_settings(settings):
    if not settings:
        return 'No settings available.'
    output='Current User Settings:\n'
    for key,value in settings.items():
        output+=f'{key.capitalize()}: {value}\n'
    return output

test_settings={
    'theme':"dark",
    'font':"default"
}
# test2={}
# print(add_setting(test_settings,('STYLE','ITALic')))
# view_settings(test_settings)
# print(update_setting(test_settings,('theme','bright')))
print(view_settings(test_settings))
