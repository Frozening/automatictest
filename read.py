i = {"item": "bullet", "num": 100, "type": "extra_item"}
j = i
print(i)
j["num"] = j["num"] * 2
print(i) # 按理说只改了j，i不应该会变化