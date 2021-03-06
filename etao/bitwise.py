"""Bits & bytes"""
import base64
import binascii


def hex_to_bytes(hex_string):
    """Convert a string of hexadecimal values into bytes."""

    return binascii.unhexlify(hex_string)


def bytes_to_hex(byte_string):
    """Convert a string of bytes into hexadecimal string representation."""

    return binascii.hexlify(byte_string)


def bytes_to_b64(input_bytes):
    """Return base64 encoding of bytes."""

    return base64.b64encode(input_bytes)


def b64_to_bytes(b64_string):
    """Return bytes decoded from base64."""

    return base64.b64decode(b64_string)


def hex_to_b64(hex_string):
    """Return base64 encoding of bytes given in hexadecimal form."""

    return bytes_to_b64(hex_to_bytes(hex_string))


def b64_to_hex(b64_string):
    """Return the hexadecimal representation of the base64
       encoded bytes."""

    return bytes_to_hex(b64_to_bytes(b64_string))


def xor_bytes(input_bytes, key_bytes):
    """XOR input bytes, repeating the XOR key as necessary."""

    result = ''
    for i in range(len(input_bytes)):
        result += chr(ord(input_bytes[i]) ^ ord(key_bytes[i % len(key_bytes)]))
    return result


def get_bit(byte, n):
    """Extract a single bit from a byte, with 0 referring to
       the least significant (last) bit and 7 referring to the most
       significant (first) bit."""

    if type(byte) == str:
        if len(byte) != 1:
            raise ValueError("Expected a single byte")
        byte = ord(byte)
    elif type(byte) == int:
        if byte < 0 or byte > 255:
            raise ValueError("Expected a value between 0 and 255")
    else:
        raise TypeError("Expected a character or integer")

    if n < 0 or n > 7:
        raise ValueError("n must be between 0 and 7")

    return (byte >> n) & 1


def get_bits(byte):
    """Return an array of the bits in byte."""

    return [get_bit(byte, n) for n in range(7, -1, -1)]


def bytes_to_bits(byte_array):
    """Convert an array or string of bytes to an array
       of bits."""

    bit_arrays = [get_bits(b) for b in byte_array]

    # Return the flattened list
    return [item for sublist in bit_arrays for item in sublist]


def bits_to_bytes(bit_array, bpb=8):
    """Convert an array or string of bits to bytes."""

    if len(bit_array) % bpb != 0:
        raise ValueError("Number of bits must be a multiple of " + str(bpb))

    result = ""
    for i in range(0, len(bit_array), bpb):
        bits = [str(bits) for bits in bit_array[i:i+bpb]]
        bitstring = ''.join(bits)
        result += chr(int(bitstring, 2))

    return result
