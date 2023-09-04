# Stride License

## Install

```bash
pip install stride-license
```

## Encode
- Generate License key by encoding data
```py
from stride-license import generate_license, generate_key


secret_key = generate_key()
data = {} # data to be encoded
# license is generated
license = generate_license(data, secret_key)
```

## Decode
-  Decode data from license key and secret key
```py
from stride-license import decode_license

# decode data
data = decode_license(license_key, secret_key)
```