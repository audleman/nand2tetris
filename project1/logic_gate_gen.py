
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
upper = [l.upper() for l in letters]


# for j in range(len(letters)):
#     low = letters[j]
#     up = upper[j]
#     print('')
#     print(f'    // Process {up} wires')
#     for i in range(16):
#         print(f'    And(a={low}[{i}], b=sel{up}, out=out{up}{i});')

# print('')
# print('    // Intermediate Ors')
# for j in range(0, len(letters), 2):
#     print('')
#     up0 = letters[j].upper()
#     up1 = letters[j+1].upper()
#     for i in range(16):
#         print(f'    Or(a=out{up0}{i}, b=out{up1}{i}, out=or{up0}{up1}{i});')


# print('    //')
# print('    // Intermediate Ors 2')
# print('    //')
# for j in range(0, len(letters), 4):
#     print('')
#     up0 = letters[j].upper()
#     up1 = letters[j+1].upper()
#     up2 = letters[j+2].upper()
#     up3 = letters[j+3].upper()
#     for i in range(16):
#         print(f'    Or(a=or{up0}{up1}{i}, b=or{up2}{up3}{i}, out=or{up0}{up1}{up2}{up3}{i});')



for i in range(16):
    print(f'    Or(a=or{upper[0]}{upper[1]}{upper[2]}{upper[3]}{i}, b=or{upper[4]}{upper[5]}{upper[6]}{upper[7]}{i}, out=out[{i}]);')
