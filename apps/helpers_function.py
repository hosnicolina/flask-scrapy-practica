def clean_url(url):
    if url[-1] == '/':
        return url
    else:
        return url + '/'
