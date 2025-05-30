import pandas as pd

df = pd.DataFrame({
    'data':       ['2025-05-18','2025-05-19','2025-05-20'],
    'produto':    ['camisa','calça','boné'],
    'quantidade': [3,2,5],
    'preco':      [59.90,89.50,29.00]
})
print(df)

df = df.drop(0)

print(df)