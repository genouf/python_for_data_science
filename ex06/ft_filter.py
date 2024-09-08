def ft_filter(function_to_apply, list_of_inputs):
    """
    Filter elements of a list using a function.
    :param function_to_apply: The function to apply to the list elements.
    :param list_of_inputs: The list of inputs to filter.
    """
    return [item for item in list_of_inputs if function_to_apply(item)]
