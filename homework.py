# 讓用戶輸入一個整數秒，計算?天?時?分?秒
# 輸出格式: xxxx秒 = x天x時x分x秒

sec = int(input('請輸入秒數：'))
temp_sec = sec
day = temp_sec // 86400
temp_sec %= 86400 
hour = temp_sec // 3600
temp_sec %= 3600
minute = temp_sec // 60
temp_sec %= 60
second = temp_sec % 60
print(f'{sec} 秒 = {day}天{hour}時{minute}分{second}秒')


# 台幣幣值有 2000、1000、500、200、50、20、10、5、1
# 使用者輸入一個整數金額，計算每一種幣值所需數量
# 輸入必須對齊如下
# 2000元， XXX張 = XXXXX元
# 500元， XXX張 = XXXXX元
# 10元， XXX枚 = XXXXX元

amount = int(input('請輸入金額：'))
temp_amount = amount
tw_2000 = temp_amount // 2000
temp_amount %= 2000
tw_1000 = temp_amount // 1000
temp_amount %= 1000
tw_500 = temp_amount // 500
temp_amount %= 500
tw_200 = temp_amount // 200
temp_amount %= 200
tw_100 = temp_amount // 100
temp_amount %= 100
tw_50 = temp_amount // 50
temp_amount %= 50
tw_20 = temp_amount // 20
temp_amount %= 20
tw_10 = temp_amount // 10
temp_amount %= 10
tw_5 = temp_amount // 5
temp_amount %= 5
tw_1 = temp_amount // 1

print(
    f'{2000:4d}元{tw_2000:4d}張\n' 
    f'{1000:4d}元{tw_1000:4d}張\n' 
    f'{500:4d}元{tw_500:4d}張\n' 
    f'{200:4d}元{tw_200:4d}張\n' 
    f'{100:4d}元{tw_100:4d}張\n' 
    f'{50:4d}元{tw_50:4d}枚\n' 
    f'{20:4d}元{tw_20:4d}枚\n' 
    f'{10:4d}元{tw_10:4d}枚\n' 
    f'{5:4d}元{tw_5:4d}枚\n' 
    f'{1:4d}元{tw_1:4d}枚'
)