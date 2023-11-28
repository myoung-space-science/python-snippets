this = 'This'
that = 'That'

def get(name):
    here = globals().copy()
    return here[name]

names = ['this', 'that', 'other']
for name in names:
    try:
        print(f"{name} = {get(name)}")
    except KeyError:
        print(f"Could not find '{name}'")
