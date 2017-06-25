# helix

this is a prototype to configure dna75 chips on linux distributions.

## dependencies

* python-hidapi (https://github.com/trezor/cython-hidapi)

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

# USB message types

## GET DESCRIPTOR (DEVICE)

discover device information

* device class/subclass
* device protocol
* max packet size
* vendor id
* product id
* manufacturer
* product
* serial no
* number of possible configurations

## GET DESCRIPTOR (CONFIGURATION)

all USB devices have at least one configuration descriptor. the amount of config descriptors is returned in the device descriptor.
each configuration descriptor has at least one interface descriptor and each interface descriptor up to 15 endpoints descriptors.

## SET CONFIGURATION

set device configuration

## GET DESCRIPTOR (HID Report)

requests the device usages and reports that describes the device characteristics

## SET INTERFACE

select an alternative setting to be used for particular interface of the current configuration.

# wireshark dumped messages

    GET DESCRIPTOR Request DEVICE
      bmRequestType: 0x80
      bRequest: GET DESCRIPTOR (6)
      Descriptor Index: 0x00
      bDescriptorType: 0x01
      Language Id: no language specified (0x0000)
      wLength: 18

    GET DESCRIPTOR Response DEVICE
      bLength: 18
      DescriptorType: 0x01 (DEVICE)
      bcdUSB: 0x0200
      bDeviceClass: Miscellaneous (0xef)
      bDeviceSubClass: 2
      bDeviceProtocol: 1 (Interface Association Descriptor)
      bMaxPacketSize0: 64
      idVendor: 0x268b
      idProduct: 0x0408
      bcdDevice: 0x0100
      iManufacturer: 2
      iProduct: 3
      iSerialNumber: 1
      bNumConfigurations: 1

    GET DESCRIPTOR Request Configuration
      bmRequestType: 0x80
      bRequest: GET DESCRIPTOR (6)
      Descriptor Index: 0x00
      bDescriptorType: 0x02
      Language Id: no language specified (0x0000)
      wLength: 9

    GET DESCRIPTOR Response Configuration
      bLength: 9
      bDescriptorType: 0x02 (CONFIGURATION)
      wTotalLength: 107
      bNumInterfaces: 3
      bConfigurationValue: 1
      iConfiguration: 0
      Configuration bmAttributes: 0x80 (NOT SELF-POWERED, NO REMOTE-WAKEUP)
      bMaxPower: 250 (500mA)

     GET DESCRIPTOR Request Configuration
      bmRequestType: 0x80
      bRequest: GET DESCRIPTOR (6)
      Descriptor Index: 0x00
      bDescriptorType: 0x02
      Language Id: no language specified (0x0000)
      wLength: 107

    GET DESCRIPTOR Response Configuration
      bLength: 9
      bDescriptorType: 0x02 (CONFIGURATION)
      wTotalLength: 107
      bNumInterfaces: 3
      bConfigurationValue: 1
      iConfiguration: 0
      Configuration bmAttributes: 0x08
      bMaxPower: 250 (500mA)

      INTERFACE DESCRIPTOR (0.0): class HID
        bLength: 9
        bDescriptorType: 0x04 (INTERFACE)
        bInterfaceNumber: 0
        bAlternateSetting: 0
        bNumEndpoints: 2
        bInterfaceClass: HID (0x03)
        bInterfaceSubClass: No subclass (0x00)
        bInterfaceProtocol: 0x00
        iInterface: 0

      HID DESCRIPTOR
        bLength: 9
        bDescriptorType: 0x21 (HID)
        bcdHID: 0x0110
        bContryCode: Not Supported (0x00)
        bNumDescriptors: 1
        bDescriptorType: HID Report (0x22)
        wDescriptorLength: 31

      ENDPOINT DESCRIPTOR
        bLength: 7
        bDescriptorType: 0x05 (ENDPOINT)
        bEndpointAddress: 0x81 IN Endpoint:1
        bmAttributes; 0x03
        wMaxPacketSize: 64
        bInterval: 1

      ENDPOINT DESCRIPTOR
        bLength: 7
        bDescriptorType: 0x05 (ENDPOINT)
        bEndpointAddress: 0x01 OUT ENDPOINT:1
        bmAttributes 0x03
        wMaxPacketSize: 64
        bInterval: 1

      INTERFACE ASSOCIATION DESCRIPTOR
        bLength: 8
        bDescriptorType: 0x0b (INTERFACE ASSOCIATION)
        bFirstInterface: 1
        bInterfaceCount: 2
        bFunctionClass: Communications and CDC Control (0x02)
        bFunctionSubClass: 0x02
        bFunctionProtocol: 0x01
        iFunction: 0

      INTERFACE DESCRIPTOR (1.0): class Communications and CDC Control
        bLength: 9
        bDescriptorType: 0x04 (INTERFACE)
        bInterfaceNumber: 1
        bAlternateSetting: 0
        bNumEndpoints: 1
        bInterfaceClass: Communications and CDC Control (0x02)
        bInterfaceSubClass: Abstract Control Model (0x02)
        bInterfaceProtocol: AT Commands: V.250 etc (0x01)
        iInterface: 0

      COMMUNICATIONS DESCRIPTOR
        bLength: 5
        bDescriptorType: 0x24 (CS_INTERFACE)
        Descriptor Subtype: Header Functional Descriptor (0x00)
        CDC: 0x0110

      COMMUNICATIONS DESCRIPTOR
        bLength: 4
        bDescriptorType: 0x24 (CS_INTERFACE)
        Descriptor Subtype: Abstract Control Management Functional Descriptor (0x02)
        bmCapabilities: 0x06

      COMMUNICATIONS DESCRIPTOR
        bLength: 5
        bDescriptorType: 0x24 (CS_INTERFACE)
        Descriptor Subtype: Call Management Functional Descriptor (0x01)
        bmCapabilities: 0x00
        Data Interface: 0x02

      COMMUNICATIONS DESCRIPTOR
        bLength: 5
        bDescriptorType: 0x24 (CS_INTERFACE)
        Descriptor Subtype: Union Functional Descriptor (0x06)
        Control Interface: 0x01
        Subordinate Interface: 0x02

      ENDPOINT DESCRIPTOR
        bLength: 7
        bDescriptorType: 0x05 (ENDPOINT)
        bEndpointAddress: 0x84 IN Endpoint:4
        bmAttributes: 0x03
        wMaxPacketSize: 64
        bInterval: 1

      INTERFACE DESCRIPTOR (2.0): class CDC-Data
        bLength: 9
        bDescriptorType: 0x04 (INTERFACE)
        bInterfaceNumber: 2
        bAlternateSetting: 0
        bNumEndpoints: 2
        bInterfaceClass: CDC-Data (0x0a)
        bInterfaceSubClass: 0x00
        bInterfaceProtocol: No class specific protocol required (0x00)
        iInterface: 0

      ENDPOINT DESCRIPTOR
        bLength: 7
        bDescriptorType: 0x05 (ENDPOINT)
        bEndpointAddress: 0x82 IN Endpoint:2
        bmAttributes: 0x02
        wMaxPacketSize: 64
        bInterval: 0

      ENDPOINT DESCRIPTOR
        bLength: 7
        bDescriptorType: 0x05 (ENDPOINT)
        bEndpointAddress: 0x02 OUT Endpoint:2
        bmAttributes: 0x02
        wMaxPacketSize: 64
        bInterval: 0

    SET CONFIGURATION Request
      bmRequestType: 0x00
      bRequest: SET CONFIGURATION (9)
      bConfigurationValue: 1
      wIndex: 0 (0x0000)
      wLength: 0

    GET DESCRIPTOR Request STRING
      bmRequestType: 0x80
      bRequest: GET DESCRIPTOR (6)
      Descriptor Index: 0x03
      bDescriptorType: 0x03
      Language Id: English (United States) (0x0409)
      wLength: 4

    GET DESCRIPTOR Response STRING
      bLength: 26
      bDescriptorType: 0x03 (STRING)
      bString: E

    GET DESCRIPTOR Request STRING
      bmRequestType: 0x80
      bRequest: GET DESCRIPTOR (6)
      Descriptor Index: 0x03
      bDescriptorType: 0x03
      Language Id: English (United States) (0x0409)
      wLength: 26

    GET DESCRIPTOR Response STRING
      bLength: 26
      bDescriptorType: 0x03 (STRING)
      bString: Evolv DNA 75

    SET_IDLE Request
      bmRequestType: 0x21
      bRequest: SET_IDLE (0x0a)
      wValue: 0x0000
      wIndex: 0
      wLength: 0

    GET DESCRIPTOR Request HID Report
      bmRequestType: 0x81
      bDescriptorIndex: 0x00
      bDescriptorType: HID Report (0x22)
      wInterfaceNumber: 0
      wDescriptorLength: 95

    GET DESCRIPTOR Response HID Report
      HID Report
        Global item (Usage)
          Header
            bSize: 2 bytes (2)
            bType: Global (1)
            bTag: Usage (0x0)
          Usage page: [Vendor-defined] (0xff00)
        Global item (Logical minimum)
          Header
            bSize: 1 byte (1)
            bType: Global (1)
            bTag: Logical minimum
          Logical minimum: 0
        Global item (Logical maximum)
          Header
            bSize: 2 bytes (2)
            bType: Global (1)
            bTag: Logical maximum (0x2)
          Logical maximum: 255
        Global item (Report size)
          Header
            bSize: 1 byte (1)
            bType: Global (1)
            bTag: Report size (0x7)
          Report size: 8
        Local item (Usage)
          Header
            bSize: 1 byte (1)
            bType: Local (2)
            bTag: Usage (0x0)
          Usage: [Vendor-defined] (0xff01)
        Main item (Collection)
          Header
            bSize: 1 byte (1)
            bType: Main (0)
            bTag: Collection (0xa)
          Collection type: Application (0x01)
          Global item (Report ID)
            Header
              bSize: 1 byte (1)
              bType: Global (1)
              bTag: Report ID (0x8)
            Report ID: 0x01
          Local item (Usage)
            Header
              bSize: 1 byte (1)
              bType: Local (2)
              bTag: Usage (0x0)
            Usage: [Vendor-defined] (0xff01)
          Global item (Report count)
            Header
              bSize: 1 byte (1)
              bType: Global (1)
              bTag: Report count (0x9)
            Report count: 62
          Main item (Input)
            Header
              bSize: 2 bytes (2)
              bType: Main (0)
              bTag: Input (0x8)
              Data/constant: Data
              Data type: Variable
              Coordinates: Absolute
              Min/max wraparound: No Wrap
              Physical relationship to data: Linear
              Preferred state: Preferred State
              Has null position: No Null position
              [Reserved]: False
              Bits or bytes: Buffered Bytes
          Local item (Usage)
            Header
              bSize: 1 byte (1)
              bType: Local (2)
              bTag: Usage (0x0)
            Usage: [Vendor-defined] (0xff01)
          Global item (Report count)
            Header
              bSize: 1 byte (1)
              bType: Global (1)
              bTag: Report count (0x9)
            Report count: 62
          Main item (output)
            Header
              bSize: 2 bytes (2)
              bType: Main (0)
              bTag: Output (0x9)
              Data/constant: Data
              Data type: Variable
              Coordinates: Absolute
              Min/max wraparound: No Wrap
              Physical relationship to data: Linear
              Preferred state: Preferred State
              Has null position: No Null position
              (Non)-volatile: Non Volatile
              Bits or bytes: Buffered Bytes
          Main item (End collection)
            Header
              bSize: 0 bytes (0)
              bType: Main (0)
              bTag: End collection (0xc)
