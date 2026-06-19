"""
讓用戶輸入一段5個字的內容，
將其中大/小寫互換，不是英文則不變
orgStr = input("輸入五個字: ")
newStr = (orgStr[0] if orgStr[0].upper() == orgStr[0].lower() else \
          orgStr[0].lower() if orgStr[0] == orgStr[0].upper() else orgStr[0].upper()) + \
         (orgStr[1] if orgStr[1].upper() == orgStr[1].lower() else \
          orgStr[1].lower() if orgStr[1] == orgStr[1].upper() else orgStr[1].upper()) + \
         (orgStr[2] if orgStr[2].upper() == orgStr[2].lower() else \
          orgStr[2].lower() if orgStr[2] == orgStr[2].upper() else orgStr[2].upper()) + \
         (orgStr[3] if orgStr[3].upper() == orgStr[3].lower() else \
          orgStr[3].lower() if orgStr[3] == orgStr[3].upper() else orgStr[3].upper()) + \
         (orgStr[4] if orgStr[4].upper() == orgStr[4].lower() else \
          orgStr[4].lower() if orgStr[4] == orgStr[4].upper() else orgStr[4].upper())
"""

"""
讓用戶輸入一段英文字，輸出每個字母第一次出現的位置和共出現幾次
範例: ABCAA
char_info = {
    'A': {'index': 0, 'count': 3},
    'B': {'index': 1, 'count': 1},
    'C': {'index': 2, 'count': 1}
}
輸出:
C Ndx Tot 
- --- ---
X 123 123
A   0   3
B   1   1
C   2   1
"""
orgStr = input("請輸入一段文字: ")

# 字典記錄每個字母的資訊
# { 'A': {'index': 0, 'count': 3}, 'B': {...} }
char_info = {}
for index, char in enumerate(orgStr):
    if char not in char_info:
        # 如果是第一次遇到，記錄位置與初始次數
        char_info[char] = {"index": index, "count": 1}
    else:
        # 如果不是第一次遇到，只增加次數
        char_info[char]["count"] += 1

print("C Ndx Tot")
print("- --- ---")
for key, value in char_info.items():
    print(f"{key} {value['index']:3d} {value['count']:3d}")
