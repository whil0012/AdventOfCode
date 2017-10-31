def get_named_property_item(line, get_named_property_item_func):
    line_segments = [x.strip() for x in line.split(" ")]
    return get_named_property_item_func(line_segments)


def get_named_property_items_from_file(file_name, get_named_property_item_func):
    with open(file_name, "r") as input_file:
        return [get_named_property_item(x, get_named_property_item_func) for x in input_file]
