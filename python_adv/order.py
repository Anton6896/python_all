
""" first class functions  """


def html_tag(tag):
    def mess(mess):
        print(f"\t<{tag}> {mess} </{tag}>")
    return mess


"""  closures (is an inner function that have an access to the free variables ) """


def outher(var):
    message = var

    def inner():
        print(f"message : {message}")

    """
    the outher func will be out of scope but !! 
    the inner func is still in memory, expecting (wathing to) params (var) location !   
    """

    return inner


first = outher('hello')
second = outher('world')

if __name__ == '__main__':
    html_h1 = html_tag('h1')
    html_h1('new message here')

    first()
    second()
