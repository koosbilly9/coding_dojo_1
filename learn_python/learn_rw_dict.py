a={}

a['1'] = {}

a['1']= {1:2}
a['1']= {2:{}}
a['1'][2] = {10:10}

a['2'] = []

a['2'].append('koos')
a['2'].append('Piet')
a['2'].append({'name':'jan'})

if 'name' in a['2'][2]:
    print(a['2'][2])
    print(a['2'][2]['name'])
    for k, v in a['2'][2].items():
        print("Key   :", k)
        print("Value :", v)

print(a.keys())
print(a.values())
print(a)