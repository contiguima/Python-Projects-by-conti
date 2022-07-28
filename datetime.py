import datetime

while (True):
  ## Obtengo el nombre de la ciudad por parte del usuario
  city = input("Enter city: ")

  ## Obtengo el tiempo actual

  current_time = datetime.datetime.now()

  ## Creo variables para las horas minutos segundos

  hour = current_time.hour
  minute = current_time.minute
  second = current_time.second

  ## Planteo casos dependiendo de las ciudades que me interesan
  ## Basar el proyecto en LATAM.  (para usar or) y Europa
  ## Mi programa analiza caso por caso dependiendo de lo que
  ## ingrese el usuario en el input

  if city == "Buenos Aires" or "Asunción" or "Brasilia":
    hour = hour

  elif city == "La Paz":
    hour = hour - 1

  elif city == "Bogotá":
    hour = hour - 2

  elif city == "Madrid":
    hour = hour + 4

  elif city == "Lisboa":
    hour = hour + 3
  
  elif city == "Caracas":
    hour = hour - 1
  
  elif city == "exit":
    break

  else:
    print (city, "is not added")
    city = "GMT"

  # print the name of the city and the its corresponding time
  print(city, str(hour) + ":" + str(minute) + ":" + str(second))
  print ("if you want to end the program, please type exit")
 

