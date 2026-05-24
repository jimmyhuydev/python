import base64

def decode_password(password):
    decode_bytes = base64.b64decode(password)
    decode_data = decode_bytes.decode()
    print(decode_data)



encode_string = input("Enter the base64 string: ")
decode_password(encode_string)
