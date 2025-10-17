# Data processing
### Specificators of the data's format
Table 1. Specificators of the byte order
|Specificator|Byte order|
|-----------|-----------|
|<|Reverse order (Little endian)|
|>|Straight order (Big endian)|

Table 2. Format specificators
|Specificator|Description|Number of bytes|
|-------------|-------------|-------------|
|x|Pass byte|1|
|b|Sign byte byte|1|
|B|Unsign byte|1|
|h|Signed short integer number|2|
|H|Unsigned short integer number|2|
|i|Signed integer number|4|
|I|Unsigned integer number|4|
|l|Signed long integer number|4|
|L|Unsigned long integer number|4|
|Q|Unsigned very long integer number|8|
|f|Floating point number|4|
|d|Double floating point number|8|
|p|Counter and symbols 1 + quantity|1 + quantity|
|s|Symbols|Quantity|

Table 3. Bytewise operators
Table is constructed for:
- a = 0b0101
- b = 0b0001

|Operator|Description|Example|Decimal result|Binary result|
|----------|----------|----------|----------|----------|
|&|Logical AND|a&b|1|0b0001|
|\||Logical OR|a\|b|5|0b0101|
|^|Excluding OR|a^b|4|0b0100|
|-|Inversion|~a|-6|Binary representaion depends on size of int type|
|<<|Left shift|a<<1|10|0b1010|
|>>|Right shift|a>>1|2|0b0010|

