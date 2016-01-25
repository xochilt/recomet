#!/usr/bin/env python
#!/usr/bin/env python
from FIS import * 
# Variables
#Input
#########################################################

userSimilarity = LinguisticVariable('userSimilarity', range = (0.0,1.0))
userSimilarity.addMF('low',MF.Gaussian(0.3,0.0))
userSimilarity.addMF('high',MF.Gaussian(0.2,1.0))

restSimilarity = LinguisticVariable('restSimilarity', range = (0.0,1.0))
restSimilarity.addMF('low',MF.Gaussian(0.3,0.0))
restSimilarity.addMF('high',MF.Gaussian(0.2,1.0))

participation = LinguisticVariable('participation', range = (0.0,15.0))
participation.addMF('insufficient',MF.Gaussian(2.0,0.0))
participation.addMF('minimum',MF.Gaussian(0.5,7.0))
participation.addMF('sufficient',MF.Gaussian(2.0,15.0))

#Output
############################################################

#expert = LinguisticVariable('expert', type = 'out', range = (0.0,1.0))
#expert.addMF('low',MF.Gaussian(0.3,0.0))
#expert.addMF('high',MF.Gaussian(0.3,1.0))

#userProfile = LinguisticVariable('userProfile', type = 'out', range = (0,1))
#userProfile.addMF('low',MF.Gaussian(0.5,1.0))
#Similarity.addMF('high',MF.Gaussian(1.5,10))

#restProfile = LinguisticVariable('restProfile', type = 'out', range = (0.0,1.0))
#restProfile.addMF('low',MF.Gaussian(0.3,0.0))
#restProfile.addMF('high',MF.Gaussian(0.3,1.0))

correlation = LinguisticVariable('correlation', type = 'out', range = (0.0,1.0))
correlation.addMF('low',MF.Gaussian(0.3,0.0))
correlation.addMF('high',MF.Gaussian(0.3,1.0))


# Rules
r1 = FuzzyRule()
r1.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(userSimilarity,userSimilarity.mfs['low']),FuzzyProposition(restSimilarity,restSimilarity.mfs['low']))),FuzzyProposition(participation,participation.mfs['insufficient']))) #1
r1.consequent.append(FuzzyProposition(correlation,correlation.mfs['low']))

r2 = FuzzyRule()
r2.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(userSimilarity,userSimilarity.mfs['low']),FuzzyProposition(restSimilarity,restSimilarity.mfs['low']))),FuzzyProposition(participation,participation.mfs['sufficient']))) #1
r2.consequent.append(FuzzyProposition(correlation,correlation.mfs['high']))

r3 = FuzzyRule()
r3.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(userSimilarity,userSimilarity.mfs['low']),FuzzyProposition(restSimilarity,restSimilarity.mfs['low']))),FuzzyProposition(participation,participation.mfs['minimum']))) #1
r3.consequent.append(FuzzyProposition(correlation,correlation.mfs['high']))

r4 = FuzzyRule()
r4.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(userSimilarity,userSimilarity.mfs['low']),FuzzyProposition(restSimilarity,restSimilarity.mfs['high']))),FuzzyProposition(participation,participation.mfs['insufficient']))) #1
r4.consequent.append(FuzzyProposition(correlation,correlation.mfs['low']))

r5 = FuzzyRule()
r5.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(userSimilarity,userSimilarity.mfs['low']),FuzzyProposition(restSimilarity,restSimilarity.mfs['high']))),FuzzyProposition(participation,participation.mfs['minimum']))) #1
r5.consequent.append(FuzzyProposition(correlation,correlation.mfs['low']))

r6 = FuzzyRule()
r6.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(userSimilarity,userSimilarity.mfs['low']),FuzzyProposition(restSimilarity,restSimilarity.mfs['high']))),FuzzyProposition(participation,participation.mfs['sufficient']))) #1
r6.consequent.append(FuzzyProposition(correlation,correlation.mfs['low']))

r7 = FuzzyRule()
r7.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(userSimilarity,userSimilarity.mfs['high']),FuzzyProposition(restSimilarity,restSimilarity.mfs['low']))),FuzzyProposition(participation,participation.mfs['insufficient']))) #1
r7.consequent.append(FuzzyProposition(correlation,correlation.mfs['high']))

r8 = FuzzyRule()
r8.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(userSimilarity,userSimilarity.mfs['high']),FuzzyProposition(restSimilarity,restSimilarity.mfs['low']))),FuzzyProposition(participation,participation.mfs['minimum']))) #1
r8.consequent.append(FuzzyProposition(correlation,correlation.mfs['high']))

r9 = FuzzyRule()
r9.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(userSimilarity,userSimilarity.mfs['high']),FuzzyProposition(restSimilarity,restSimilarity.mfs['low']))),FuzzyProposition(participation,participation.mfs['sufficient']))) #1
r9.consequent.append(FuzzyProposition(correlation,correlation.mfs['high']))

r10 = FuzzyRule()
r10.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(userSimilarity,userSimilarity.mfs['high']),FuzzyProposition(restSimilarity,restSimilarity.mfs['high']))),FuzzyProposition(participation,participation.mfs['insufficient']))) #1
r10.consequent.append(FuzzyProposition(correlation,correlation.mfs['high']))

r11 = FuzzyRule()
r11.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(userSimilarity,userSimilarity.mfs['high']),FuzzyProposition(restSimilarity,restSimilarity.mfs['high']))),FuzzyProposition(participation,participation.mfs['minimum']))) #1
r11.consequent.append(FuzzyProposition(correlation,correlation.mfs['high']))

r12 = FuzzyRule()
r12.antecedent.append(FuzzyOperator('and',(FuzzyOperator('and',FuzzyProposition(userSimilarity,userSimilarity.mfs['high']),FuzzyProposition(restSimilarity,restSimilarity.mfs['high']))),FuzzyProposition(participation,participation.mfs['sufficient']))) #1
r12.consequent.append(FuzzyProposition(correlation,correlation.mfs['high']))

reglas = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12]
 
fis = FIS(reglas)
    
def eval(u,r,p):
    userSimilarity.current_value = u
    restSimilarity.current_value = r
    participation.current_value = p
    
    return fis.eval()

#if __name__ == '__main__':
  
#  eval(0.9,100,0.4)

#for pesos in fis.composition():
#	print pesos.degreeOfSupport





