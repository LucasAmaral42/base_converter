digits = "0123456789ABCDEF"

def to_base_div(number, base_inicial, base_saida):
    resto = []
    raw_resto = []
    quocientes = []

    string_number = ""
    for i in number:
        if not i.isnumeric():
            string_number += str(int(i, base_inicial))
        else:
            string_number += i

    number_aux = int(string_number)
    while number_aux >= base_saida:
        resto_aux = number_aux % base_saida
        number_aux = int(number_aux / base_saida)
        quocientes.append(number_aux)

        if resto_aux >= 10:
            resto.append(str(digits[resto_aux]))
            raw_resto.append(str(resto_aux))
        else:
            resto.append(str(resto_aux))
            raw_resto.append(str(resto_aux))

        if number_aux < base_saida:
            resto.append(str(number_aux))
            raw_resto.append(str(number_aux))

    result = "".join(resto)
    return [result, quocientes, raw_resto]

def expo(base_inicial):
    return base_inicial in [2 ** 1, 2 ** 2, 2 ** 3, 2 ** 4]

def dec_to_base(num,base):
    base_num = ""
    while num > 0:
        dig = int(num%base)
        if dig < 10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10)
        num //= base
    return base_num

def mult_base(number, base_inicial):
    number_aux = number[::-1]
    result = 0

    for index, value in enumerate(number_aux):
        value = digits.index(value)
        result += (int(value) * (base_inicial ** index))

    return result

def run_calc(number, base_inicial, base_saida):
    quocientes = None
    resto      = None
    if base_saida != 10:
        if expo(base_inicial):
            dec = int(number, base_inicial)
            result = dec_to_base(dec, base_saida)
        else:
            data = to_base_div(number, base_inicial, base_saida)
            result       = data[0]
            quocientes   = data[1]
            resto        = data[2]
    else:
        result = mult_base(number, base_inicial)
        return number, base_inicial, base_saida, quocientes, result, resto
    return number, base_inicial, base_saida, quocientes, result[::-1], resto
