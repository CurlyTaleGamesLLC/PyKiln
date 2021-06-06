# Poorly ported to Micropython by Curly Tale Games LLC

import ustruct

class UnaryStruct:
    """
    Arbitrary single value structure register that is readable and writeable.

    Values map to the first value in the defined struct.  See struct
    module documentation for struct format string and its possible value types.

    :param int register_address: The register address to read the bit from
    :param type struct_format: The struct format string for this register.
    """

    def __init__(self, register_address, struct_format):
        self.format = struct_format
        self.address = register_address

    def __get__(self, obj, objtype=None):
        buf = bytearray(1 + ustruct.calcsize(self.format))
        buf[0] = self.address
        with obj.i2c_device as i2c:
            i2c.write_then_readinto(buf, buf, out_end=1, in_start=1)
        return ustruct.unpack_from(self.format, buf, 1)[0]

    def __set__(self, obj, value):
        buf = bytearray(1 + ustruct.calcsize(self.format))
        buf[0] = self.address
        ustruct.pack_into(self.format, buf, 1, value)
        with obj.i2c_device as i2c:
            i2c.write(buf)