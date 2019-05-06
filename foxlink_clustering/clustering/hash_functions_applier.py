from foxlink_clustering.hash_functions import superfasthash
from foxlink_clustering.hash_functions import pearson
from foxlink_clustering.hash_functions import custom_md5
from foxlink_clustering.hash_functions import custom_sha256
from foxlink_clustering.hash_functions import custom_blake2b
from foxlink_clustering.hash_functions import custom_sha3_384
from foxlink_clustering.hash_functions import custom_sha1
from foxlink_clustering.hash_functions import custom_sha512


def apply(shingle):
    return [superfasthash.apply(shingle),
            pearson.apply(shingle),
            custom_md5.apply(shingle),
            custom_sha256.apply(shingle),
            custom_blake2b.apply(shingle),
            custom_sha3_384.apply(shingle),
            custom_sha1.apply(shingle),
            custom_sha512.apply(shingle)]
