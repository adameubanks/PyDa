def math(input):
    from espeak import espeak
    import math
    if '+' in input:
        find_add = input.find('+')
        resultAdd = str(float(input[:find_add]) + float(input[find_add+1:]))
        print resultAdd
        espeak.synth(resultAdd)

    if '-' in input:
        find_sub = input.find('-')
        resultSub = str(float(input[:find_sub]) - float(input[find_sub+1:]))
        print resultSub
        espeak.synth(resultSub)

    if '*' in input:
        find_mul = input.find('*')
        resultMul = str(float(input[:find_mul]) * float(input[find_mul+1:]))
        print resultMul
        espeak.synth(resultMul)

    if '/' in input:
        find_div = input.find('/')
        resultDiv = str(float(input[:find_div]) / float(input[find_div+1:]))
        print resultDiv
        espeak.synth(resultDiv)
    if '%' in input:
        find_mod = input.find('%')
        resultMod = str(float(input[:find_mod]) % float(input[find_mod+1:]))
        print resultMod
        espeak.synth(resultMod)
