from tokenise import cal
#from collection import OrderedDict

tokenizedwords = cal()
d = dict()

for data in tokenizedwords:
    for token in data['text']:
        if token in d.keys():
            if data['id'] == d[token][-1]:
                continue
            d[token].append(data['id'])
        else:
            d[token] = [data['id']]

for key in sorted(d.keys()):
    print(key, d[key])
