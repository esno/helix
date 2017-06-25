# dna75 chip info

## dmesg

    usb 1-4.1.4: new full-speed USB device number 11 using xhci_hcd
    hid-generic 0003:268B:0408.0005: hiddev0,hidraw3: USB HID v1.10 Device [Dimension Engineering Evolv DNA 75] on usb-0000:00:14.0-4.1.4/input0
    cdc_acm 1-4.1.4:1.1: ttyACM0: USB ACM device

## lsusb

    Bus 001 Device 011: ID 268b:0408  
    Device Descriptor:
      bLength                18
      bDescriptorType         1
      bcdUSB               2.00
      bDeviceClass          239 Miscellaneous Device
      bDeviceSubClass         2 
      bDeviceProtocol         1 Interface Association
      bMaxPacketSize0        64
      idVendor           0x268b 
      idProduct          0x0408 
      bcdDevice            1.00
      iManufacturer           2 Dimension Engineering
      iProduct                3 Evolv DNA 75
      iSerial                 1 ********
      bNumConfigurations      1
      Configuration Descriptor:
        bLength                 9
        bDescriptorType         2
        wTotalLength          107
        bNumInterfaces          3
        bConfigurationValue     1
        iConfiguration          0 
        bmAttributes         0x80
          (Bus Powered)
        MaxPower              500mA
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        0
          bAlternateSetting       0
          bNumEndpoints           2
          bInterfaceClass         3 Human Interface Device
          bInterfaceSubClass      0 
          bInterfaceProtocol      0 
          iInterface              0 
            HID Device Descriptor:
              bLength                 9
              bDescriptorType        33
              bcdHID               1.10
              bCountryCode            0 Not supported
              bNumDescriptors         1
              bDescriptorType        34 Report
              wDescriptorLength      31
             Report Descriptors: 
               ** UNAVAILABLE **
          Endpoint Descriptor:
            bLength                 7
            bDescriptorType         5
            bEndpointAddress     0x81  EP 1 IN
            bmAttributes            3
              Transfer Type            Interrupt
              Synch Type               None
              Usage Type               Data
            wMaxPacketSize     0x0040  1x 64 bytes
            bInterval               1
          Endpoint Descriptor:
            bLength                 7
            bDescriptorType         5
            bEndpointAddress     0x01  EP 1 OUT
            bmAttributes            3
              Transfer Type            Interrupt
              Synch Type               None
              Usage Type               Data
            wMaxPacketSize     0x0040  1x 64 bytes
            bInterval               1
        Interface Association:
          bLength                 8
          bDescriptorType        11
          bFirstInterface         1
          bInterfaceCount         2
          bFunctionClass          2 Communications
          bFunctionSubClass       2 Abstract (modem)
          bFunctionProtocol       1 AT-commands (v.25ter)
          iFunction               0 
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        1
          bAlternateSetting       0
          bNumEndpoints           1
          bInterfaceClass         2 Communications
          bInterfaceSubClass      2 Abstract (modem)
          bInterfaceProtocol      1 AT-commands (v.25ter)
          iInterface              0 
          CDC Header:
            bcdCDC               1.10
          CDC ACM:
            bmCapabilities       0x06
              sends break
              line coding and serial state
          CDC Call Management:
            bmCapabilities       0x00
            bDataInterface          2
          CDC Union:
            bMasterInterface        1
            bSlaveInterface         2 
          Endpoint Descriptor:
            bLength                 7
            bDescriptorType         5
            bEndpointAddress     0x84  EP 4 IN
            bmAttributes            3
              Transfer Type            Interrupt
              Synch Type               None
              Usage Type               Data
            wMaxPacketSize     0x0040  1x 64 bytes
            bInterval               1
        Interface Descriptor:
          bLength                 9
          bDescriptorType         4
          bInterfaceNumber        2
          bAlternateSetting       0
          bNumEndpoints           2
          bInterfaceClass        10 CDC Data
          bInterfaceSubClass      0 
          bInterfaceProtocol      0 
          iInterface              0 
          Endpoint Descriptor:
            bLength                 7
            bDescriptorType         5
            bEndpointAddress     0x82  EP 2 IN
            bmAttributes            2
              Transfer Type            Bulk
              Synch Type               None
              Usage Type               Data
            wMaxPacketSize     0x0040  1x 64 bytes
            bInterval               0
          Endpoint Descriptor:
            bLength                 7
            bDescriptorType         5
            bEndpointAddress     0x02  EP 2 OUT
            bmAttributes            2
              Transfer Type            Bulk
              Synch Type               None
              Usage Type               Data
            wMaxPacketSize     0x0040  1x 64 bytes
            bInterval               0
    Device Status:     0x0000
      (Bus Powered)
