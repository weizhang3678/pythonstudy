'''
dtype of numpy
bool_	布尔型数据类型（True 或者 False）
int_	默认的整数类型（类似于 C 语言中的 long，int32 或 int64）
intc	与 C 的 int 类型一样，一般是 int32 或 int 64
intp	用于索引的整数类型（类似于 C 的 ssize_t，一般情况下仍然是 int32 或 int64）
int8	字节（-128 to 127）
int16	整数（-32768 to 32767）
int32	整数（-2147483648 to 2147483647）
int64	整数（-9223372036854775808 to 9223372036854775807）
uint8	无符号整数（0 to 255）
uint16	无符号整数（0 to 65535）
uint32	无符号整数（0 to 4294967295）
uint64	无符号整数（0 to 18446744073709551615）
float_	float64 类型的简写
float16	半精度浮点数，包括：1 个符号位，5 个指数位，10 个尾数位
float32	单精度浮点数，包括：1 个符号位，8 个指数位，23 个尾数位
float64	双精度浮点数，包括：1 个符号位，11 个指数位，52 个尾数位
complex_	complex128 类型的简写，即 128 位复数
complex64	复数，表示双 32 位浮点数（实数部分和虚数部分）
complex128	复数，表示双 64 位浮点数（实数部分和虚数部分）
'''
import numpy as np

r1 = np.random.randint(5,10)
print(r1)

r2 = np.random.random()
print(r2)

r_arr = np.random.random((3,3))
print(r_arr)

# popular
r_arr_int = np.random.randint(0,10,(5,5))
print(r_arr_int)

# range
list(range(0,10,2))
print(np.arange(0,10,2))

#linespace
r_arr1 = np.linspace(0, 3, 10)
print(r_arr1)

# n direction
r_arr2 = np.eye(5)
print(r_arr2)