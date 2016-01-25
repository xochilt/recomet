#!/usr/bin/env python
from FIS import * 
# Variables

#########################################################

Item = LinguisticVariable('Item')
Item.addMF('New',MF.Trapezoidal(-0.36, -0.04, 0.4193, 0.597))
Item.addMF('Old',MF.Trapezoidal(0.4061, 0.538, 1.04, 1.36))
#service.addMF('excelent',MF.Gaussian(1.5,10))

###############################################################

User = LinguisticVariable('User')
User.addMF('Closer',MF.Trapezoidal(-50.4, -5.6, 53.5, 60.2))
User.addMF('Far',MF.Trapezoidal(56.42, 73.15, 145.6, 190.4))

##############################################################

Instructor = LinguisticVariable('Instructor')
Instructor.addMF('Low', MF.Trapezoidal(-0.36, -0.04, 0.4775, 0.602))
Instructor.addMF('High', MF.Trapezoidal(0.406, 0.5595, 1.04, 1.36))

############################################################

Correlation= LinguisticVariable('Correlation', type = 'out', range = (0,1))
Correlation.addMF('Low',MF.Trapezoidal(-0.36, -0.04, 0.4299, 0.599))
Correlation.addMF('Half',MF.Triangular(0.298, 0.495, 0.694))
Correlation.addMF('High',MF.Trapezoidal(0.403, 0.5516, 1.04, 1.36))
#tip.addMF('generous',MF.Triangular(20.0,25.0,30.0)) 

################################################################

Similarity= LinguisticVariable('Similarity', type = 'out', range = (0,1))
Similarity.addMF('Low',MF.Trapezoidal(-0.357, -0.0374, 0.4246, 0.599))
Similarity.addMF('Half',MF.Triangular(0.298, 0.495, 0.694))
Similarity.addMF('High',MF.Trapezoidal(0.403, 0.5225, 1.04, 1.36))

###############################################################

InstructorRating= LinguisticVariable('InstructorRating', type = 'out', range = (0,1))
InstructorRating.addMF('Low',MF.Trapezoidal(-0.36, -0.04, 0.4431, 0.597))
InstructorRating.addMF('High',MF.Trapezoidal(0.403, 0.541, 1.04, 1.36))



# Rules
r1 = FuzzyRule()
r1.antecedent.append(FuzzyOperator('and',FuzzyProposition(Item,Item.mfs['New']),FuzzyProposition(User,User.mfs['Closer'])))
r1.consequent.append(FuzzyProposition(Similarity,Similarity.mfs['High']))


r2 = FuzzyRule()
r2.antecedent.append(FuzzyOperator('and',FuzzyProposition(Item,Item.mfs['Old']),FuzzyProposition(User,User.mfs['Closer'])))
r2.consequent.append(FuzzyProposition(Similarity,Similarity.mfs['Half']))


r3 = FuzzyRule()
r3.antecedent.append(FuzzyOperator('and',FuzzyProposition(Item,Item.mfs['New']),FuzzyProposition(User,User.mfs['Far'])))
r3.consequent.append(FuzzyProposition(InstructorRating,InstructorRating.mfs['High']))


r4 = FuzzyRule()
r4.antecedent.append(FuzzyOperator('and',FuzzyProposition(Item,Item.mfs['Old']),FuzzyProposition(User,User.mfs['Far'])))
r4.consequent.append(FuzzyProposition(Correlation,Correlation.mfs['High']))




reglas = [r1,r2,r3,r4]
 
fis = FIS(reglas)
    
def eval(It, Us, In):
    Item.current_value = It
    User.current_value = Us
    Instructor.current_value = In 	
 
    return fis.eval()

if __name__ == '__main__':
  
  eval(0.9,100,0.4)

for pesos in fis.composition():
	print pesos.degreeOfSupport

