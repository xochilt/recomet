#!/usr/bin/env python
#!/usr/bin/env python
from FIS import * 

# Variable
# Input
rating = LinguisticVariable('rating', range = (0.0,5.0))
rating.addMF('low',MF.Gaussian(1.0,0.0))  
rating.addMF('high',MF.Gaussian(1.0,5.0))

price = LinguisticVariable('price', range = (0.0,5.0))
price.addMF('low',MF.Gaussian(1.0,0.0))
price.addMF('high',MF.Gaussian(1.0,5.0)) 

votes = LinguisticVariable('votes', range = (0.0, 10.0))
votes.addMF('insufficient',MF.Gaussian(2.0,0.0))
votes.addMF('sufficient',MF.Gaussian(3.0,10.0))   

#Output
recommendation = LinguisticVariable('recommendation', type = 'out', range = (0.0,5.0))
recommendation.addMF('low',MF.Gaussian(0.5,1.0))
recommendation.addMF('medium',MF.Gaussian(0.4,3.0)) 
recommendation.addMF('high',MF.Gaussian(0.5,5.0)) 

#Rules
r1 = FuzzyRule()
r1.antecedent.append(FuzzyOperator('and',FuzzyProposition(rating,rating.mfs['high']),FuzzyProposition(price,price.mfs['low'])))
r1.consequent.append(FuzzyProposition(recommendation,recommendation.mfs['high']))

r2 = FuzzyRule()
r2.antecedent.append(FuzzyOperator('and',FuzzyProposition(rating,rating.mfs['high']),FuzzyProposition(votes,votes.mfs['sufficient'])))
r2.consequent.append(FuzzyProposition(recommendation,recommendation.mfs['high']))

r3 = FuzzyRule()
r3.antecedent.append(FuzzyOperator('and',FuzzyProposition(rating,rating.mfs['high']),FuzzyProposition(votes,votes.mfs['insufficient'])))
r3.consequent.append(FuzzyProposition(recommendation,recommendation.mfs['medium']))

r4 = FuzzyRule()
r4.antecedent.append(FuzzyOperator('and',FuzzyProposition(rating,rating.mfs['low']),FuzzyProposition(price,price.mfs['high'])))
r4.consequent.append(FuzzyProposition(recommendation,recommendation.mfs['low']))

r5 = FuzzyRule()
r5.antecedent.append(FuzzyOperator('and',FuzzyProposition(rating,rating.mfs['low']),FuzzyProposition(votes,votes.mfs['insufficient'])))
r5.consequent.append(FuzzyProposition(recommendation,recommendation.mfs['low']))


reglas = [r1,r2,r3,r4,r5]
 
fis = FIS(reglas)
    
def eval(r,p,v):
        rating.current_value = r
        price.current_value = p
        votes.current_value = v
        return fis.eval()

if __name__ == '__main__':
    pass
    #eval(5.0,0.0,5.0)
