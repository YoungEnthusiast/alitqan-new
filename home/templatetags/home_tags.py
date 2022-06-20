from django import template
register = template.Library()

@register.simple_tag
def my_url(value, field_name, urlencode=None):
    url = '?{}={}'.format(field_name, value)
    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0]!=field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)
    return url

def suffixPos(i):
    if i in range (11, 101, 100):
        return str(i)+"th"
    elif i in range (12, 101, 100):
        return str(i)+"th"
    elif i in range (13, 101, 100):
        return str(i)+"th"
    elif i in range (1, 101, 10):
        return str(i)+"st"
    elif i in range (2, 101, 10):
        return str(i)+"nd"
    elif i in range (3, 101, 10):
        return str(i)+"rd"
    else:
        return str(i)+"th"

register.filter("my_suffix", suffixPos)
