# CF E-Mail Decoder
Cloud-flare obfuscates emails generally to prevent from web-scrapers. But there's an easy way out to decode this.

## Before beginning:
- Obfuscated emails are in `data-cfemail` attribute
- Put the `decode.py` in your library path

## How to use?
```python
from decode import decode

decoded_list = decode('73111712001b15101233181a1a075d12105d1a1d')

print(decoded_list[0])
```

## More examples:
 
```python
from decoder import decode

decoded_list = decode("3e5f54574a554b535f4c4d5f56515110585d5f7e5557574a105f5d105750","73111712001b15101233181a1a075d12105d1a1d")

for emails in decoded_list:
    print(emails)
```