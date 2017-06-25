#!/usr/bin/env python

import hid

class dna75:
    _vendorId = 0x268b
    _productId = 0x0408

    def __init__(self):
        self._connect()
        self._disconnect()

    def _connect(self):
        self.h = hid.device()
        self.h.open(self._vendorId, self._productId)
        self.h.set_nonblocking(1)

        print('Connecting %s [%s] (%s)' % (
            self.h.get_product_string(),
            self.h.get_manufacturer_string(),
            self.h.get_serial_number_string()))

    def _disconnect(self):
        self.h.close()

class helix:
    def __init__(self):
        try:
            dna = dna75()
        except OSError:
            print('there is no dna chip available')

if __name__ == '__main__':
    helix()
