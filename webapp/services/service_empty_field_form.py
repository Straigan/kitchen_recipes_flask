def replacing_an_empty_field_with_none(field: str) -> str | None:
    """Замена пустой ячейки на None"""
    if field == '':
        return None
    else:
        return field
