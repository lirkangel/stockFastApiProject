from collections import namedtuple


def singleton(a_class):
    def on_call(*args, **kwargs):
        if on_call.instance is None:
            on_call.instance = a_class(*args, **kwargs)
        return on_call.instance

    on_call.instance = None
    return on_call


def convert_dict_to_json(data: dict):
    return namedtuple(
        "X", data.keys()
    )(*tuple(map(lambda x: x if not isinstance(x, dict) else convert_dict_to_json(x), data.values())))
