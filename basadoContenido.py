#------------------------------------------------------------------------------
#ALGORITMO BASADO EN CONTENIDO
#------------------------------------------------------------------------------
import restaurant
from restaurant import *
from restaurant.models import *
from restaurant.views import *
import recommendations
from recommendations import *

def basadoContenido(id): #id user.
    #Consulta BD: items del usuario que ha votado con 5.
    highrat = Rating.objects.all().filter(user=id,rating=5)
    #highval contiene la lista de items del usuario activo.
    highval=[]
    if(highrat):       
        [highval.append(i.id_item.id) for i in highrat if i.id_item.id not in highval]
    
    #Consulta BD: la lista de todos los restaurantes.   
    all_ratings = Restaurant.objects.all()
    #Obtengo items de la BD, que no han sido votados por el usuario activo. 
    items = []
    [items.append(item) for item in all_ratings if item.id not in highval]

    #obtenemos los perfiles del usuario activo.
    profiles_user, p_it_user = get_profiles(highval,items, profile_user=True)
    #Obtenemos los perfiles de la todos los restaurantes votados con 5.
    profiles_all, p_it_all = get_profiles(highval,items, profile_user=False)
    
    #---------------------------------------------------------------
    #OBTENER SIMILARIDAD DE COSENOS
    #---------------------------------------------------------------
    #Obtenemos las listas para pasarlas al diccionario.
    #Hace la correlacion entre los items del usuario y los items de la base
    #de datos. Por Ej:si el usuario voto 2 restaurantes con rating 5, 2*177=354 
    #salidas en el vector t. Son 177 restaurantes en la bd.
    sim_cos = simCosenoItems(p_it_user, p_it_all)
    
    #hd: items con alta correlacion, contiene listas:
    #[item_user, item_bd, valor de similaridad]
    hd=[]
    [hd.append(i) for i in sim_cos if i[0]>0.8] 

    #Top-N. Lista de recomendaciones.
    bc_recomendations=[]
    if hd:
        for i in range(len(hd)):
            item = Restaurant.objects.get(item=hd[i][2])
            if item in bc_recomendations:continue #Asegurar que no se repitan.
            bc_recomendations.append(item)
    
    return profiles_user, profiles_all, p_it_user, p_it_all, bc_recomendations, hd, sim_cos


#-----------------------------------------------------------------------------
#OBTENER PERFILES.
#-----------------------------------------------------------------------------
#highval: items con rating 5.
#items: items de la base de datos.
#profile_user: si es del perfil del usuario o no.
#-----------------------------------------------------------------------------
def get_profiles(highval, items, profile_user):
    #Obtenemos los vectores para perfil de usuario activo.
    if profile_user==True:
        #Restaurantes del perfil del usuario activo.
        profiles_user, p_it_user = userProfiles(highval)
        return profiles_user, p_it_user
    else:
        #Se aplica a los rest. obtenidos de a BD.
        profiles_item, p_it_all = itemProfiles(items)
        return profiles_item, p_it_all
    
#-----------------------------------------------------------------------------
#Obtener los perfiles de los items que el usuario voto con 5.
#-----------------------------------------------------------------------------
def userProfiles(highval):
    profiles=[]
    for i in highval:
        #Obtiene el perfil del restaurant.
        r = Restaurant.objects.get(item=i)
        #Obtiene el perfil del restaurant en vector binario.
        p_item = profileItem(r)
        #Agrega el vector binario a la lista de perfiles.
        profiles.append(p_item)
    #Obtener en el diccionario los perfiles de los items valorados por el usuario.
    p_it = dict([(t[0],{}) for t in profiles])
    for t in profiles:
        p_it[t[0]] = (t[1])
    
    return profiles, p_it

#----------------------------------------------------------------------------   
#Obtener los perfiles de items de la bd.
#----------------------------------------------------------------------------
def itemProfiles(items):
    profiles=[]
    for r in items:
        #Obtenemos el perfil del restaurante(item).
        p_item = profileItem(r)
        #Agregamos el perfil a la lista de perfiles.
        profiles.append(p_item)
        
    #Creamos el diccionario.        
    p_it = dict([(t[0],{}) for t in profiles])
    for t in profiles:
        p_it[t[0]] = (t[1])
    
    return profiles, p_it

#-----------------------------------------------------------------------------
#Crea el vector binario que representa el perfil del item.
#-----------------------------------------------------------------------------
def profileItem(r):
    #Empieza a crear el perfil...
        #4 PRICE RANGES.
        #Dominio: 1.cheap, 2.regular, 3.expensive 4. Too expensive
        prices = [0,0,0,0]
        #Solo tiene un tipo de precio.
        prices[r.price_range_id-1]=r.price_range_id
        
        #2 formas de pago.
        payment=[0,0]
        if int(r.payment_id)==1:
            payment[0]=1
        else:
            payment[1]=1

        #Alcohol 2 tipos.
        alcohol =[0,0]
        if int(r.alcohol_id)==1:
            alcohol[0]=1
        else:
            alcohol[1]=1
        
        #2 tipos de area de fumadores.
        smoking_area = [0,0]
        if int(r.smoking_area)==1:
            smoking_area[0]=1
        else:
            smoking_area[1]=1
        
        #3 tipos de vestimenta.
        dress_code=[0,0,0]
        for item in range(1,4):
            if(item==int(r.dress_code_id)):
                dress_code[item-1]=1
        
        #3 tipos de estacionamiento.  
        parking =[0,0,0]
        for item in range(1,4):
            if(item==int(r.parking_id)):
                parking[item-1]=1
            
        #4 tipos de instalationes.
        instalation=[0,0,0,0]
        for item in range(1,5):
            if(item==int(r.instalation_id)):
                instalation[item-1]=1
        
        #5 tipos de ambiente.
        atmosphere=[0,0,0,0,0]
        for item in range(1,6):
            if(item==int(r.atmosphere_id)):
                atmosphere[item-1]=1
        
        #39 tipos de comidas(cocina).
        cols_cuisine=39
        cuisine=[]
        #crear el vector binario de cocinas.
        [cuisine.append(0) for i in range(cols_cuisine)]
        #Asigna el tipo de cocina del restaurante.
        for item in range(1,40):
            if(item==int(r.cuisine_id)):
                cuisine[item-1]=1
        #si solo maneja un tipo de cocina:
        #cuisine[r.cuisine_id-1]=r.cuisine_id                
        
        #id del restaurante.
        id_item=r.id
        
        #55 ATTRIBUTES    
        profile_item=[]
        profile_item.insert(0,id_item)
        profile_item.insert(1,prices)
        profile_item[1].extend(payment)
        profile_item[1].extend(alcohol)
        profile_item[1].extend(smoking_area)
        profile_item[1].extend(dress_code)
        #profile_item[1].extend(accessibility)
        profile_item[1].extend(parking)
        profile_item[1].extend(instalation)
        profile_item[1].extend(atmosphere)
        profile_item[1].extend(cuisine)
    
        return profile_item
    
    
#---------------------------------------------------------------------
#Calcula la similaridad entre todos los perfiles de la B.D.
#profileu: perfiles de items del usuario.
#profilei: perfiles de items de la bd.
#---------------------------------------------------------------------
def simCosenoItems(profileu,profilei):
  all_profiles = [] #Lista de todos los perfiles.
  for item in profileu:
    lsim=[]
    for it in profilei:
      if(item==it):continue
      l=[]
      #Calculamos la similaridad de cosenos.
      sim = sim_coseno(profileu,profileu[item],profilei[it])
      l.append(sim) #similaridad entre 2 items.
      l.append(item)#item del usuario
      l.append(it) #Item similar a uno del usuario activo
      lsim.append(l)
    all_profiles.extend(lsim)
  return all_profiles

#----------------------------------------------------------------------------    
#Similaridad de cosenos: Retorna la similaridad de coseno entre dos vectores.
#vc: vector binario del item actual(Current).
#vs: vector binario del item con el que se compara la similaridad(Similarity).
#profiles: perfiles de los restaurantes(items) registrados en la BD.
#---------------------------------------------------------------------------
def sim_coseno(profiles,vc,vs):
  #Producto punto de dos vectores.
  sum = 0
  for i in range(len(vc)):
    sum = sum+(vc[i]*vs[i])
  
  #norma ||v|| de los vectores.
  vc_nor = 0
  vs_nor = 0
  for i in range(len(vc)):
    vc_nor = vc_nor + vc[i]**2
  nc = sqrt(vc_nor)
    
  for i in range(len(vs)):
    vs_nor = vc_nor + vc[i]**2
  ns = sqrt(vs_nor)
  
  #Funcion de utilidad Algoritmo basado en contenido.
  f_util = float(sum) / (nc * ns)
  
  return f_util

