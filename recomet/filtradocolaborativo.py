#------------------------------------------------------
#ALGORTIMO DE FILTRADO COLABORATIVO                  
#------------------------------------------------------
import restaurant
from restaurant import *
from restaurant.models import *
from restaurant.views import *
import recommendations
from recommendations import *

def filtradoColaborativo(iduser):
    #Armar la matriz de usuarios, extraer las listas en una sola lista de tuplas de usuarios. 
    r = Rating.objects.values_list('user','id_item','rating')
    list_ratings=[]
    if(r):#Valida matriz de ratings.
        [list_ratings.append(i) for i in r]

    #Crea diccionario para utilizarlo en las recomendaciones.
    us_it = dict([(t[0],{}) for t in list_ratings])
    for t in list_ratings:
        us_it[t[0]][t[1]]=float(t[2])
    
    #Obtiene los vecinos cercanos por simililaridad(preferencias, usuario)
    pearsonCorrelationUser = topMatches(us_it,iduser)

    #Cambian las recomendaciones con cada diccionario generado por el sistema.
    pearson_recs = getRecommendations(us_it,iduser,similarity=sim_pearson)
    euclidean_recs = getRecommendations(us_it,iduser,similarity=sim_distance)
        
    #print 'pearson_recs', pearson_recs
    #print 'euclidean_recs', euclidean_recs

    list_items=[]  
    if pearson_recs:
        if len(pearson_recs)>5:#Si es mayor a 5 solo obtenemos los 5 primeros items.
            for i in range(5):
                    item = Restaurant.objects.get(item=pearson_recs[i][1])
                    list_items.append(item)#Agregamos el item a la lista.
        else:#Si no es mayor a 5, obtenemos los items recomendados.
            for i in range(len(pearson_recs)):
                    item = Restaurant.objects.get(item=pearson_recs[i][1])
                    list_items.append(item)#Agregamos el item a la lista.
            
    return pearsonCorrelationUser, pearson_recs, euclidean_recs, list_items  


# Regresa los mejores vecinos observados para el usuario en el diccionario de preferencias.  
# Numero de resultados(n) y similaridad(similarity) son parametros opcionales.
def topMatches(prefs,person,n=20,similarity=sim_distance):
  scores=[(similarity(prefs,person,other),other)
            for other in prefs if other!=person]
  scores.sort()
  scores.reverse()
  return scores[0:n]

#------------------------------------------------------------------------------
# Obtiene recomendaciones para una persona usando el Promedio de los Pesos.
#------------------------------------------------------------------------------
def getRecommendations(prefs,person,similarity=sim_distance):
  rankings=''
  if person in prefs:
    totals={}
    simSums={}
    for other in prefs:
      # No compararme conmigo mismo.
      if other==person: continue
      sim=similarity(prefs,person,other)
      # Ignora similaridad de cero o menor.
      if sim<=0: continue
      for item in prefs[other]:
        # Solo items que todavia no he valorado.
        if item not in prefs[person] or prefs[person][item]==0:
          # Similarity * Score
          totals.setdefault(item,0)
          totals[item]+=prefs[other][item]*sim
          # Suma de similaridades.
          simSums.setdefault(item,0)
          simSums[item]+=sim
    # Crear la lista normalizada.
    rankings=[(total/simSums[item],item) for item,total in totals.items()]
    #Regresa la lista ordenada.
    rankings.sort()
    rankings.reverse()
    return rankings
  else:
    return rankings


#----------------------------------------------------------------------------------
#Regresa el valor de la distancia basada en similaridad para la persona1 y persona2.
#----------------------------------------------------------------------------------
def sim_distance(prefs,person1,person2):
  # Obtene la  lista de items compartidos.
  #Verificamos que el usuario se encuentre en el diccionario.
  if person1 in prefs and person2 in prefs:
    si={}
    for item in prefs[person1]: 
      if item in prefs[person2]: si[item]=1
  
    # Si ellos no tienen ratings en comun, regresa 0.
    if len(si)==0: return 0
  
    # Agrega la raiz de todas las diferencias.
    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) 
                        for item in prefs[person1] if item in prefs[person2]])
    return 1/(1+sum_of_squares)
  else:
     return 0
    
#-------------------------------------------------------------------------------    
#Regresa el coheficiente de correlacion de Pearson para p1 y p2.
#-------------------------------------------------------------------------------
def sim_pearson(prefs,p1,p2):
  # Obtiene la lista de items mutuamente valorados.
  r=0
  if p1 in prefs and p2 in prefs:
    si={}
    for item in prefs[p1]: 
      if item in prefs[p2]: si[item]=1
  
    # Si no hay ratings en comun, regresa 0.
    if len(si)==0: return 0
  
    # Suma de los calculos.
    n=len(si)
    
    # Suma de todas las preferencias.
    sum1=sum([prefs[p1][it] for it in si])
    sum2=sum([prefs[p2][it] for it in si])
    
    # Suma de las raices cuadradas.
    sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
    sum2Sq=sum([pow(prefs[p2][it],2) for it in si])	
    
    # Suma de los productos.
    pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
    
    # Calcular r (Pearson score)
    num=pSum-(sum1*sum2/n)
    den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0: return 0
  
    r=num/den
    return r
  else:
    return r
  
  
critics={'1':{'Aki Sushi de Playas':5.0,'Arbio Restaurante':5.0,'Tai Ki Shi':4.0,'Rincon San Roman':2.0, 'Italianisimo':3.0,'Lorca':4.0},
'2': {'Aki Sushi de Playas':4.0,'Yogurt Place':3.0,'Akira Terriyaqui':1.0,'Arbio Restaurante':5.0,'Lorca':5.0,'Italianisimo':3.0,'Tai Ki Shi':4.0},
'3':{'Aki Sushi de Playas':3.0,'Yogurt Place':3.0,'Akira Terriyaqui':2.0,'Arbio Restaurante':5.0,'Rincon San Roman':3.0,'Italianisimo':3.0,'Tai Ki Shi':4.0},
'4':{'Yogurt Place':3.0,'Akira Terriyaqui':2.0,'Rincon San Roman':3.0,'Italianisimo':3.0},
'5':{'Aki Sushi de Playas':4.0,'Yogurt Place':3.0,'Arbio Restaurante':4.0,'Lorca':5.0,'Rincon San Roman':3.0,'Tai Ki Shi':4.0},
'6':{'Aki Sushi de Playas':3.0,'Yogurt Place':4.0,'Akira Terriyaqui':3.0,'Arbio Restaurante':5.0,'Lorca':5.0,'Rincon San Roman':3.0,'Italianisimo':3.0,'Tai Ki Shi':4.0},
'7':{'Akira Terriyaqui':3.0,'Lorca':5.0,'Rincon San Roman':3.0,'Italianisimo':3.0,'Tai Ki Shi':4.0},
'8':{'Yogurt Place':5.0,'Akira Terriyaqui':2.0,'Arbio Restaurante':5.0,'Lorca':5.0,'Rincon San Roman':2.0,'Italianisimo':4.0,'Tai Ki Shi':5.0},
'9':{'Aki Sushi de Playas':3.0,'Yogurt Place':5.0,'Akira Terriyaqui':3.0,'Arbio Restaurante':4.0,'Rincon San Roman':2.0,'Italianisimo':4.0,'Tai Ki Shi':4.0},
'10':{'Aki Sushi de Playas':3.0,'Yogurt Place':4.0,'Arbio Restaurante':5.0,'Italianisimo':4.0,'Tai Ki Shi':5.0},
'11':{'Aki Sushi de Playas':3.0,'Yogurt Place':4.0,'Akira Terriyaqui':3.0,'Arbio Restaurante':4.0,'Lorca':5.0,'Rincon San Roman':4.0,'Italianisimo':4.0,'Tai Ki Shi':4.0},
'12':{'Yogurt Place':4.0,'Akira Terriyaqui':2.0,'Lorca':5.0,'Rincon San Roman':4.0,'Italianisimo':3.0,'Tai Ki Shi':5.0},
'13':{'Aki Sushi de Playas':5.0,'Yogurt Place':5.0,'Akira Terriyaqui':2.0,'Arbio Restaurante':5.0,'Lorca':5.0,'Rincon San Roman':2.0,'Italianisimo':5.0},
'14':{'Akira Terriyaqui':3.0,'Lorca':4.0,'Rincon San Roman':3.0,'Italianisimo':5.0,'Tai Ki Shi':3.0},
'15':{'Aki Sushi de Playas':4.0,'Yogurt Place':5.0,'Arbio Restaurante':4.0,'Lorca':4.0,'Rincon San Roman':4.0,'Italianisimo':3.0,'Tai Ki Shi':3.0},
'16':{'Akira Terriyaqui':3.0,'Arbio Restaurante':4.0,'Lorca':4.0,'Rincon San Roman':2.0,'Italianisimo':3.0,'Tai Ki Shi':3.0},
'17':{'Aki Sushi de Playas':3.0,'Yogurt Place':3.0,'Akira Terriyaqui':5.0,'Arbio Restaurante':4.0,'Rincon San Roman':3.0,'Italianisimo':3.0,'Tai Ki Shi':3.0},
'18':{'Yogurt Place':3.0,'Arbio Restaurante':3.0,'Lorca':4.0,'Rincon San Roman':3.0,'Italianisimo':3.0,'Tai Ki Shi':3.0},
'19':{'Aki Sushi de Playas':1.0,'Yogurt Place':3.0,'Arbio Restaurante':5.0,'Lorca':4.0,'Rincon San Roman':3.0,'Italianisimo':3.0,'Tai Ki Shi':3.0},
'20':{'Yogurt Place':3.0,'Akira Terriyaqui':3.0,'Lorca':4.0,'Rincon San Roman':2.0,'Italianisimo':3.0,'Tai Ki Shi':3.0},
'21':{'Akira Terriyaqui':2.0,'Arbio Restaurante':3.0,'Lorca':5.0,'Rincon San Roman':4.0,'Italianisimo':3.0,'Tai Ki Shi':3.0},
'22':{'Aki Sushi de Playas':3.0,'Arbio Restaurante':5.0,'Lorca':4.0,'Rincon San Roman':5.0,'Italianisimo':3.0,'Tai Ki Shi':3.0},
'23':{'Aki Sushi de Playas':4.0,'Arbio Restaurante':5.0,'Lorca':5.0,'Rincon San Roman':4.0,'Italianisimo':3.0},
'24':{'Yogurt Place':3.0,'Akira Terriyaqui':2.0,'Lorca':4.0,'Rincon San Roman':4.0,'Italianisimo':3.0,'Tai Ki Shi':4.0},
'25':{'Aki Sushi de Playas':4.0,'Yogurt Place':5.0,'Akira Terriyaqui':1.0,'Arbio Restaurante':5.0,'Lorca':5.0,'Rincon San Roman':4.0,'Italianisimo':4.0,'Tai Ki Shi':4.0},
'26':{'Yogurt Place':5.0,'Akira Terriyaqui':2.0,'La vuelta del rodeo':5.0,'Arbio Restaurante':5.0,'Lorca':4.0,'Rincon San Roman':4.0,'Italianisimo':4.0,'Tai Ki Shi':4.0},
'27':{'Akira Terriyaqui':3.0,'Arbio Restaurante':5.0,'Lorca':5.0,'Rincon San Roman':3.0,'Italianisimo':4.0,'Tai Ki Shi':4.0},
'28':{'Yogurt Place':5.0,'Arbio Restaurante':5.0,'Lorca':4.0,'Rincon San Roman':3.0,'Italianisimo':4.0},
'29':{'Aki Sushi de Playas':2.0,'Yogurt Place':5.0, 'Akira Terriyaqui':1.0,'Lorca':5.0,'Rincon San Roman':3.0,'Italianisimo':4.0,'Tai Ki Shi':5.0},
'30':{'Yogurt Place':2.0,'Arbio Restaurante':4.0,'Lorca':4.0,'Rincon San Roman':4.0,'Tai Ki Shi':4.0},
'31':{'Aki Sushi de Playas':3.0,'Yogurt Place':3.0,'Akira Terriyaqui':3.0,'Arbio Restaurante':4.0,'Rincon San Roman':4.0,'Italianisimo':2.0,'Tai Ki Shi':4.0},
'32':{'Aki Sushi de Playas':3.0,'Arbio Restaurante':3.0,'Rincon San Roman':4.0,'Italianisimo':2.0},
'33':{'Yogurt Place':3.0,'Akira Terriyaqui':2.0,'Arbio Restaurante':5.0,'Lorca':5.0,'Italianisimo':3.0,'Tai Ki Shi':4.0},
'34':{'Aki Sushi de Playas':5.0,'Akira Terriyaqui':3.0,'Ricardos':3.0,'Arbio Restaurante':2.0,'Lorca':5.0,'Rincon San Roman':4.0,'Italianisimo':2.0,'Tai Ki Shi':3.0},
'35':{'Arbio Restaurante':3.0,'Lorca':5.0,'Rincon San Roman':5.0,'La Querencia':2.0,'Italianisimo':3.0},
'36':{'Aki Sushi de Playas':2.0,'La vuelta del rodeo':5.0,'Akira Terriyaqui':2.0,'Lorca':3.0,'Italianisimo':2.0},
'37':{'Aki Sushi de Playas':3.0,'Yogurt Place':3.0,'Arbio Restaurante':3.0,'Lorca':3.0,'Rincon San Roman':3.0,'Italianisimo':3.0,'Tai Ki Shi':4.0},
'38':{'Yogurt Place':3.0,'Arbio Restaurante':4.0,'Lorca':3.0,'La vuelta del rodeo':5.0,'Rincon San Roman':2.0,'Tai Ki Shi':3.0},
'39':{'Aki Sushi de Playas':4.0,'Yogurt Place':3.0,'Akira Terriyaqui':3.0,'Lorca':5.0,'Rincon San Roman':4.0,'Italianisimo':2.0,'Tai Ki Shi':3.0},
'40':{'Aki Sushi de Playas':5.0,'Lorca':4.0,'Rincon San Roman':2.0,'Italianisimo':2.0,'Tai Ki Shi':5.0},
'41':{'Yogurt Place':3.0,'Lorca':5.0,'Rincon San Roman':3.0,'La Querencia':4.0,'Italianisimo':2.0},
'42':{'Aki Sushi de Playas':3.0,'Yogurt Place':3.0, 'Ricardos':2.0,'Akira Terriyaqui':2.0,'Arbio Restaurante':2.0,'Lorca':3.0,'Rincon San Roman':3.0},
'43':{'Yogurt Place':3.0,'Arbio Restaurante':2.0,'Lorca':5.0,'Rincon San Roman':3.0,'Italianisimo':3.0},
'44':{'Yogurt Place':3.0,'Akira Terriyaqui':5.0,'Lorca':4.0,'Rincon San Roman':2.0,'Italianisimo':3.0,'Tai Ki Shi':3.0},
'45':{'Aki Sushi de Playas':5.0,'Akira Terriyaqui':4.0,'Arbio Restaurante':2.0,'Lorca':3.0,'Tai Ki Shi':3.0},
'46':{'Aki Sushi de Playas':4.0,'Yogurt Place':3.0,'Arbio Restaurante':2.0,'Lorca':5.0,'Rincon San Roman':4.0,'Italianisimo':3.0,'Tai Ki Shi':3.0},
'47':{'Yogurt Place':3.0,'Akira Terriyaqui':2.0,'Rincon San Roman':2.0,'Italianisimo':3.0,'Tai Ki Shi':3.0},
'48':{'Yogurt Place':4.0,'Akira Terriyaqui':2.0,'Ricardos':4.0,'Arbio Restaurante':2.0,'Italianisimo':3.0,'Tai Ki Shi':3.0},
'49':{'Aki Sushi de Playas':5.0,'Akira Terriyaqui':3.0,'Lorca':4.0,'Rincon San Roman':4.0,'Italianisimo':3.0,'Tai Ki Shi':3.0},
'50':{'Yogurt Place':4.0,'Lorca':5.0,'Ricardos':2.0,'Sotano suizo':4.0,'La Querencia':2.0, 'La vuelta del rodeo':5.0, 'Lorca':5.0, 'Yogurt Place':5.0}}
 
