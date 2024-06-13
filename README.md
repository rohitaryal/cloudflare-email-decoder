# CF E-Mail Decoder
Cloud-flare obfuscates emails generally to prevent from web-scrapers. But there's an easy way out to decode this. (This can also encode emails if you need)

## Before beginning:
- Obfuscated emails are in `data-cfemail` attribute
- Put the `decode.py` in your library path

## How to use?

### For decoding:
```python
from decoder import decode

decoded_list = decode('a7c2dfc6cad7cbc2e7d389cac2')
print(decoded_list[0])
```

### For encoding:
```python
from decoder import encode

encoded_list = encode('example@gmail.com')
print(encoded_list[0])
```

## More examples:
 
 #### Example 1:
```python
from decoder import decode

decoded_list = decode("a7c2dfc6cad7cbc2e7d389cac2","73111712001b15101233181a1a075d12105d1a1d")

for emails in decoded_list:
    print(emails)
```
#### Example 2:

```python
from decoder import encode

encoded_list = encode('example@t.me', 'example@a.in')

for strings in encoded_list:
    print(strings)
```

#### Example 3:

```python
from decoder import decode, encode

plain_email = "example@gmail.com"

encoded_email = encode(plain_email)
decoded_email = decode(encoded_email[0])

print("Testing With: " + plain_email)

print("Re-encoded: " + encoded_email[0])
print("Re-decoded: " + decoded_email[0])

```

---
*In case of some issue submit it in issue section*