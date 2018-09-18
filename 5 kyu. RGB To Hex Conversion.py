# https://www.codewars.com/kata/rgb-to-hex-conversion/


def rgb(r, g, b):
    """
    The rgb() method is incomplete. Complete the method so that passing in RGB decimal values will result in a
    hexadecimal representation being returned. The valid decimal values for RGB are 0 - 255. Any (r,g,b) argument
    values that fall out of that range should be rounded to the closest valid value.

    :return: RBG to Hex
    """
    return (('%02x' % ((r if r > 0 else 0) if r < 256 else 255)) +
            ('%02x' % ((g if g > 0 else 0) if g < 256 else 255)) +
            ('%02x' % ((b if b > 0 else 0) if b < 256 else 255))).upper()


assert rgb(0,0,0) == "000000"
assert rgb(1,2,3) == "010203"
assert rgb(255,255,255) == "FFFFFF"
assert rgb(254,253,252) == "FEFDFC"
assert rgb(-20,275,125) == "00FF7D"