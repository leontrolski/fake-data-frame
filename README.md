# See `fake_data_frame.py`

```python
df = FakeDataFrame({
    'a': [4, 5, 6],
    'b': [7, 8, 9]

})
print(df)
#     a |     b
# -------------
#     4 |     7
#     5 |     8
#     6 |     9

print(df['b'] > 7)
# <FakeSeries: b {0: False, 1: True, 2: True}>

print(df['a'][df['b'] > 7])
# <FakeSeries: a {1: 5, 2: 6}>

df['mult'] = df['a'][df['b'] > 7] * 2
print(df)
#     a |     b |  mult
# ---------------------
#     4 |     7 |   NaN
#     5 |     8 |    10
#     6 |     9 |    12
```
