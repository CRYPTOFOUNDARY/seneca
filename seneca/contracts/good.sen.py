def one_you_can_export():
    print('Running one_you_can_export()')

def one_you_can_also_export():
    print('Running one_you_can_also_export()')
    one_you_can_export()

@protected
def one_you_cannot_export():
    print('Running one_you_cannot_export()')

def one_you_can_also_also_export():
    print('Running one_you_can_also_also_export()')
    one_you_cannot_export()
