#!/usr/bin/env python
from FIS import *

# Variables
# Input
service = LinguisticVariable('service')
service.addMF('poor',MF.Gaussian(1.5,0.0))
service.addMF('good',MF.Gaussian(1.5,5.0))
service.addMF('excellent',MF.Gaussian(1.5,10))

food = LinguisticVariable('food')
food.addMF('rancid',MF.Trapezoidal(0.0, 0.0, 1.0, 4.0))
food.addMF('good',MF.Trapezoidal(3.0, 4.0, 6.0, 8.0))
food.addMF('delicious',MF.Trapezoidal(7.0, 9.0, 10.0, 10.0))

price = LinguisticVariable('price')
price.addMF('low',MF.Gaussian(1.5,0.0))
price.addMF('medium',MF.Gaussian(1.5,5.0))
price.addMF('heigth',MF.Gaussian(1.5,10))

#Output
tip = LinguisticVariable('tip', type = 'out', range = (0,30))
tip.addMF('bad',MF.Triangular(0.0,5.0,10.0))
tip.addMF('good',MF.Triangular(10.0,15.0,20.0))
tip.addMF('excellent',MF.Triangular(20.0,25.0,30.0))

#Rules
r1 = FuzzyRule()
r1.antecedent.append(FuzzyOperator('and', FuzzyOperator('and',FuzzyProposition(service,service.mfs['poor']), FuzzyProposition(food,food.mfs['rancid'])),FuzzyProposition(price,price.mfs['low']))) #1
r1.consequent.append(FuzzyProposition(tip,tip.mfs['bad']))

r2 = FuzzyRule()
r2.antecedent.append(FuzzyOperator('and',FuzzyOperator('and',FuzzyProposition(service,service.mfs['poor']),FuzzyProposition(food,food.mfs['rancid'])),FuzzyProposition(price,price.mfs['medium'])))#2
r2.consequent.append(FuzzyProposition(tip,tip.mfs['bad']))

r3 = FuzzyRule()
r3.antecedent.append(FuzzyOperator('and',FuzzyOperator('and',FuzzyProposition(service,service.mfs['poor']),FuzzyProposition(food,food.mfs['rancid'])),FuzzyProposition(price,price.mfs['heigth'])))#3
r3.consequent.append(FuzzyProposition(tip,tip.mfs['bad']))

r4 = FuzzyRule()
r4.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(service,service.mfs['poor']),FuzzyProposition(food,food.mfs['good']))),FuzzyProposition(price,price.mfs['low'])))#4
r4.consequent.append(FuzzyProposition(tip,tip.mfs['good']))

r5 = FuzzyRule()
r5.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(service,service.mfs['poor']),FuzzyProposition(food,food.mfs['good']))),FuzzyProposition(price,price.mfs['medium']))) #5
r5.consequent.append(FuzzyProposition(tip,tip.mfs['good']))

r6 = FuzzyRule()
r6.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(service,service.mfs['poor']),FuzzyProposition(food,food.mfs['good']))),FuzzyProposition(price,price.mfs['heigth'])))#6
r6.consequent.append(FuzzyProposition(tip,tip.mfs['bad']))

r7 = FuzzyRule()
r7.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(service,service.mfs['good']),FuzzyProposition(food,food.mfs['good']))),FuzzyProposition(price,price.mfs['low']))) #7
r7.consequent.append(FuzzyProposition(tip,tip.mfs['good']))

r8 = FuzzyRule()
r8.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(service,service.mfs['good']),FuzzyProposition(food,food.mfs['good']))),FuzzyProposition(price,price.mfs['medium'])))#8
r8.consequent.append(FuzzyProposition(tip,tip.mfs['good']))

r9 = FuzzyRule()
r9.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(service,service.mfs['good']),FuzzyProposition(food,food.mfs['good']))),FuzzyProposition(price,price.mfs['heigth'])))#9
r9.consequent.append(FuzzyProposition(tip,tip.mfs['good']))

r10 = FuzzyRule()
r10.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(service,service.mfs['excellent']),FuzzyProposition(food,food.mfs['good']))),FuzzyProposition(price,price.mfs['low'])))#10
r10.consequent.append(FuzzyProposition(tip,tip.mfs['good']))

r11 = FuzzyRule()
r11.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(service,service.mfs['excellent']),FuzzyProposition(food,food.mfs['good']))),FuzzyProposition(price,price.mfs['medium'])))#11
r11.consequent.append(FuzzyProposition(tip,tip.mfs['good']))

r12 = FuzzyRule()
r12.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(service,service.mfs['poor']),FuzzyProposition(food,food.mfs['delicious']))),FuzzyProposition(price,price.mfs['medium'])))#12
r12.consequent.append(FuzzyProposition(tip,tip.mfs['good']))

r13 = FuzzyRule()
r13.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(service,service.mfs['poor']),FuzzyProposition(food,food.mfs['delicious']))),FuzzyProposition(price,price.mfs['heigth'])))#13
r13.consequent.append(FuzzyProposition(tip,tip.mfs['good']))

r14 = FuzzyRule()
r14.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(service,service.mfs['good']),FuzzyProposition(food,food.mfs['delicious']))),FuzzyProposition(price,price.mfs['heigth'])))#14
r14.consequent.append(FuzzyProposition(tip,tip.mfs['good']))

r15 = FuzzyRule()
r15.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(service,service.mfs['good']),FuzzyProposition(food,food.mfs['delicious']))),FuzzyProposition(price,price.mfs['medium'])))#15
r15.consequent.append(FuzzyProposition(tip,tip.mfs['good']))

r16 = FuzzyRule()
r16.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(service,service.mfs['good']),FuzzyProposition(food,food.mfs['delicious']))),FuzzyProposition(price,price.mfs['low'])))#16
r16.consequent.append(FuzzyProposition(tip,tip.mfs['good']))

r17 = FuzzyRule()
r17.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(service,service.mfs['excellent']),FuzzyProposition(food,food.mfs['delicious']))),FuzzyProposition(price,price.mfs['low'])))#17
r17.consequent.append(FuzzyProposition(tip,tip.mfs['excellent']))

r18 = FuzzyRule()
r18.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(service,service.mfs['excellent']),FuzzyProposition(food,food.mfs['delicious']))),FuzzyProposition(price,price.mfs['medium'])))#18
r18.consequent.append(FuzzyProposition(tip,tip.mfs['excellent']))

r19 = FuzzyRule()
r19.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(service,service.mfs['excellent']),FuzzyProposition(food,food.mfs['delicious']))),FuzzyProposition(price,price.mfs['heigth']))) #19
r19.consequent.append(FuzzyProposition(tip,tip.mfs['excellent']))

reglas = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19]

fis = FIS(reglas)

def eval(s, f, p):
    service.current_value = s
    food.current_value = f
    price.current_value = p

    return fis.eval()

if __name__ == '__main__':
    print eval(8.86,7.53,7.65)
