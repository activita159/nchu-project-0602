# 讓用戶輸入一個整數秒，計算?天?時?分?秒
# 輸出格式: xxxx秒 = x天x時x分x秒

sec = int(input("請輸入秒數："))
temp_sec = sec
day = temp_sec // 86400
temp_sec %= 86400
hour = temp_sec // 3600
temp_sec %= 3600
minute = temp_sec // 60
temp_sec %= 60
second = temp_sec % 60
print(f"{sec} 秒 = {day}天{hour}時{minute}分{second}秒")


# 台幣幣值有 2000、1000、500、200、50、20、10、5、1
# 使用者輸入一個整數金額，計算每一種幣值所需數量
# 輸入必須對齊如下
# 2000元， XXX張 = XXXXX元
# 500元， XXX張 = XXXXX元
# 10元， XXX枚 = XXXXX元

amount = int(input("請輸入金額："))
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

total_count = tw_2000 + tw_1000 + tw_500 + tw_200 + tw_100 + tw_50 + tw_20 + tw_10 + tw_5 + tw_1

print(f"{2000:4d} 元, {tw_2000:4d} 張= {2000 * tw_2000:7d} 元")
print(f"{1000:4d} 元, {tw_1000:4d} 張= {1000 * tw_1000:7d} 元")
print(f"{500:4d} 元, {tw_500:4d} 張= {500 * tw_500:7d} 元")
print(f"{200:4d} 元, {tw_200:4d} 張= {200 * tw_200:7d} 元")
print(f"{100:4d} 元, {tw_100:4d} 張= {100 * tw_100:7d} 元")
print(f"{50:4d} 元, {tw_50:4d} 枚= {50 * tw_50:7d} 元")
print(f"{20:4d} 元, {tw_20:4d} 枚= {20 * tw_20:7d} 元")
print(f"{10:4d} 元, {tw_10:4d} 枚= {10 * tw_10:7d} 元")
print(f"{5:4d} 元, {tw_5:4d} 枚= {5 * tw_5:7d} 元")
print(f"{1:4d} 元, {tw_1:4d} 枚= {1 * tw_1:7d} 元")
print("--------  --------  --------")
print(f"{'合計':>4s} : {total_count:4d} 張= {amount:7d} 元")