taxRate = 0.06

def calculateSalesTax(total):
    salesTax = total * taxRate
    return round(salesTax, 2)

def calculateTotalAfterTax(total):
    salesTax = calculateSalesTax(total)
    totalAfterTax = total + salesTax
    return round(totalAfterTax, 2)
