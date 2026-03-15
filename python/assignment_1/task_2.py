categories = ["Electronics", "Electronics", "Audio", "Accessories", "Accessories", "Electronics"]

#create set
categories_set = set(categories)

print(categories_set)

#Added duplicate category and it would be ignored
categories_set.add("Video")
categories_set.add("Audio")

print(categories_set)

# check if category exists

def isExists(category):
    if category in categories_set:
     return True
    else:
     return False


cat = "Audio"
exist = isExists(cat)
print(f"{cat} is present :", exist)

cat = "Short Video"
exist = isExists(cat)
print(f"{cat} is present :", exist)
