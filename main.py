from pyuuidapikey import UUIDAPIKey

if __name__ == '__main__':
    k = UUIDAPIKey()

    i = str('0b9ca335-92a8-46d8-b477-eb2ed83ac927')
    d = k.to_apikey(i)

    print(d)

    d = k.to_uuid(d)

    print(d)

    # for i in '194814773':
    #     print(str(bin(int(i))[2:]))

    # bstr = '11001'

    # binaryToDecimal(11001)
