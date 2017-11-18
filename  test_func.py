def get_vat(price, vat_rate):
    vat = price / 100 * vat_rate
    price_no_vat = price - vat
    print(price_no_vat)

def get_summ(one, two, delimeter=' '):
    return str(one) + str(delimeter) + str(two)

price1 = 100
vat_rate1 = 18
get_vat(price1, vat_rate1)


print(get_summ('Hello', 'world!'))
