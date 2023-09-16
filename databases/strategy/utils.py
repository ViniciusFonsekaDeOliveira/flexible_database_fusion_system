def getWhereClauseConditions(data: dict, placeholder: str):
    conditions = [f"{column} = {placeholder}"for column in data.keys()]
    clause_values = tuple(data.values())
    size = len(data.keys())

    if size == 1:
        clause_conditions = conditions[0]
        return clause_conditions, clause_values
    elif size >= 2:
        clause_conditions = " AND ".join(conditions)
        return clause_conditions, clause_values
    else:
        raise ValueError(
            "Where clause conditions must have a valid data identifier")
