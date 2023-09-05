# Stride License

## Install

```bash
pip install stride-license
```

## Decode
-  Decode data from license key and secret key
```py
from stride-license import decode_license

# decode data
data = decode_license(license_key, secret_key)
```

## License Status
- Get status of the license key
```py
from stride-license import get_license_status

# get status
status = get_license_status(license_key, secret_key) # Invalid | Active | Expired
```