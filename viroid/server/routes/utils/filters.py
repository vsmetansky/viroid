def apply_filters(filters, entities):
    return [e for e in entities if _check_filters(filters, e)]


def _check_filters(filters, e):
    return any(_check_filter(f, e) for f in filters)


def _check_filter(f, e):
    return getattr(e, f.get('key')) == f.get('value')
