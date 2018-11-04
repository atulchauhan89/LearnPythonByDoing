# import the base64 module, this will help you in encoding and decoding of base64 strings
import base64


def main():
    input_string = input("Please provide input...")
    # Here we will encode the string into base64 encoding
    encode = input_string.encode('utf-8')
    base64_encode = base64.b64encode(encode)
    print("base64 encoded line", base64_encode)
    # Now let's decode the above converted base64_encode
    print("Decoded line", base64.b64decode(base64_encode).decode('utf-8'))

if __name__ == '__main__':
    main()
    
    
# Try encoding with 0b110011101110100010000000000001000101100    

