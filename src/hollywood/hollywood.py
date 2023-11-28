
def isInList(entries_to_check: list, valid_entries: list) -> bool:
    if entries_to_check:
        for studio in entries_to_check:
            if studio in valid_entries:
                return True
    return False