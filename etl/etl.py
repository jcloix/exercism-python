def transform(legacy_data):
    return {val.lower(): key for key in legacy_data.keys() for val in legacy_data[key]}
