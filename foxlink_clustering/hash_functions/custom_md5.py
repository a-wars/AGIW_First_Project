import hashlib
from foxlink_clustering.hash_functions import type_converter


def apply(shingle):
    shingle = shingle.encode('utf-8')
    m = hashlib.md5()
    m.update(shingle)
    return type_converter.hex_msb_to_int(m.hexdigest())
