"""
    Conversions between xy coordinate and array location
"""


def xy_to_idx(x, y, width):
    return x + (y*width)


def idx_to_xy(idx, width):
    y = idx % width
    x = idx - y
    return x, y
