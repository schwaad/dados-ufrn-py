def extrair_urls(obj):
    urls = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == "url":
                urls.append(v)
            else:
                urls.extend(extrair_urls(v))
    elif isinstance(obj, list):
        for item in obj:
            urls.extend(extrair_urls(item))
    return urls
