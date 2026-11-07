def search_by_title(items, keyword):
    keyword = keyword.lower()
    return [
        dvd for dvd in items
        if keyword in dvd.title.lower()
    ]