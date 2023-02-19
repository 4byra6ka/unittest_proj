# файл dicts.py
def get_val(collection:dict, key:str, default='git') -> str:
    """Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default."""
    if collection == {} or not (key in collection.keys()):
        return default
    return collection[key]