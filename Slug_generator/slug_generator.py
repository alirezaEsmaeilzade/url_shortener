import uuid


def base16_to_base32(digits):
    decimal = int(digits, 16)
    if decimal < 10:
        return str(decimal)
    else:
        return chr(decimal + ord('a') - 10)


def convert_base16_to_base32(base16_num):
    return ''.join(base16_to_base32(base16_num[2*i:2*i+1]) for i in range(8))


def slug_generator():
    unique_id = uuid.uuid1().hex
    return convert_base16_to_base32(unique_id)