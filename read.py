i = {"item": "bullet", "num": 100, "type": "extra_item"}
j = i
print("修改前i=", i)
j["num"] = j["num"] * 2
print("修改后i=", i) # 按理说只改了j，i不应该会变化
print("i指针的值", id(i))
print("j指针的值", id(j)) # 但其实i、j都指向同一个字典对象，因此j=i这个步骤本质是将i的指针传给了J

# 如果单独把字典赋值给k(也就是不k=i)，这个过程相当于创建了一个“新”对象，那么k就是一个新的指针
k = {"item": "bullet", "num": 100, "type": "extra_item"}
print("k指针的值", id(k)) 