  import pandas as pd

  def encontrar(df1,j,suport):
    cont=0;
    ofset=0;
    if int(df1['Resources'][j]['@support'])>suport:
      for k in range(0,len(df1['Resources'][j]['@types'])):
        if df1['Resources'][j]['@types'][k] == "S":
          if df1['Resources'][j]['@types'][k+1] == "c":
            if df1['Resources'][j]['@types'][k+2] == "h":
              if df1['Resources'][j]['@types'][k+3] == "e":
                if df1['Resources'][j]['@types'][k+4] == "m":
                  if df1['Resources'][j]['@types'][k+5] == "a":
                    if df1['Resources'][j]['@types'][k+6] == ":":
                      ofset=k+6
                      if df1['Resources'][j]['@types'][k+7] != ",":
                        cont=cont+1
                        if df1['Resources'][j]['@types'][k+8] != ",":
                          cont=cont+1
                          if df1['Resources'][j]['@types'][k+9] != ",":
                            cont=cont+1
                            if df1['Resources'][j]['@types'][k+10] != ",":
                              cont=cont+1
                              if df1['Resources'][j]['@types'][k+11] != ",":
                                cont=cont+1
                                if df1['Resources'][j]['@types'][k+12] != ",":
                                  cont=cont+1
                                  if df1['Resources'][j]['@types'][k+13] != ",":
                                    cont=cont+1
                                    if df1['Resources'][j]['@types'][k+14] != ",":
                                      cont=cont+1
                                      if df1['Resources'][j]['@types'][k+15] != ",":
                                        cont=cont+1
                                        if df1['Resources'][j]['@types'][k+16] != ",":
                                          cont=cont+1
                                          if df1['Resources'][j]['@types'][k+17] != ",":
                                            cont=cont+1
                                            if df1['Resources'][j]['@types'][k+18] != ",":
                                              cont=cont+1
                                              if df1['Resources'][j]['@types'][k+19] != ",":
                                                  cont=cont+1
                                                  if df1['Resources'][j]['@types'][k+20] != ",":
                                                    cont=cont+1
                                                    if df1['Resources'][j]['@types'][k+21] != ",":
                                                      cont=cont+1
                                                      if df1['Resources'][j]['@types'][k+22] != ",":
                                                        cont=cont+1
                                                        if df1['Resources'][j]['@types'][k+23] != ",":
                                                          cont=cont+1
                                                          if df1['Resources'][j]['@types'][k+24] != ",":
                                                            cont=cont+1
                                                            if df1['Resources'][j]['@types'][k+25] != ",":
                                                              cont=cont+1
                                                              if df1['Resources'][j]['@types'][k+26] != ",":
                                                                cont=cont+1
                                                                if df1['Resources'][j]['@types'][k+27] != ",":
                                                                  cont=cont+1
                                                                  if df1['Resources'][j]['@types'][k+28] != ",":
                                                                    cont=cont+1
                                                                    if df1['Resources'][j]['@types'][k+29] != ",":
                                                                      cont=cont+1
                                                                      if df1['Resources'][j]['@types'][k+30] != ",":
                                                                        cont=cont+1
                                                                        if df1['Resources'][j]['@types'][k+31] != ",":
                                                                            cont=cont+1
                                                                        else:
                                                                          return (cont,ofset)
                                                                      else:
                                                                        return (cont,ofset)
                                                                    else:
                                                                      return (cont,ofset)
                                                                  else:
                                                                    return (cont,ofset)
                                                                else:
                                                                  return (cont,ofset)
                                                              else:
                                                                return (cont,ofset)
                                                            else:
                                                              return (cont,ofset)
                                                          else:
                                                            return (cont,ofset)
                                                        else:
                                                          return (cont,ofset)
                                                      else:
                                                        return (cont,ofset)
                                                    else:
                                                      return (cont,ofset)
                                                  else:
                                                    return (cont,ofset)
                                              else:
                                                return (cont,ofset)
                                            else:
                                              return (cont,ofset)
                                          else:
                                            return (cont,ofset)
                                        else:
                                          return (cont,ofset)
                                      else:
                                        return (cont,ofset)
                                    else:
                                      return (cont,ofset)
                                  else:
                                    return (cont,ofset)
                                else:
                                  return (cont,ofset)
                              else:
                                return (cont,ofset)
                            else:
                              return (cont,ofset)
                          else:
                            return (cont,ofset)
                        else:
                          return (cont,ofset)
                      else:
                        return (cont,ofset)


    return 0
  def reemplazar(strr):
    strr=str(strr)
    strr=strr.replace('SportsTeam',"equipo deportivo")
    strr=strr.replace('SportsEvent',"evento deportivo")
    strr=strr.replace('Place', "lugar")
    strr=strr.replace('Organization',"organización")
    strr=strr.replace('CreativeWork',"trabajo creativo")
    strr=strr.replace('WebSite',"página web")
    strr=strr.replace('Movie',"película")
    strr=strr.replace('Person',"persona")
    strr=strr.replace('StadiumOrArena',"estadio")
    strr=strr.replace('Event',"evento")
    strr=strr.replace('TelevisionStation',"canal de televisión")
    strr=strr.replace('RadioStation',"canal de radio")
    strr=strr.replace('Language'," idioma")
    strr=strr.replace('Product',"producto")
    strr=strr.replace('Airport',"aeropuerto")
    strr=strr.replace('School',"colegio")
    strr=strr.replace('MusicAlbum',"disco de música")
    strr=strr.replace('RiverBodyOfWater'," río")
    strr=strr.replace('Painting',"cuadro")
    strr=strr.replace('TVEpisode',"episodio de televisión")
    return strr


  df = pd.read_csv("../data/700tokensVal.csv", sep=";")
  df["summary"]=df["1"]
  df["article"]=df["0"]
  df1 = pd.read_json("../data/val/val/text1.json")
  errores=0
  resultadooo=[]
  for l in range(0,42597):
    try:
      df2 = pd.read_json("./val/val/text"+str(l)+".json")
      resultadoM=[]
      final=[]
      final2=[]
      for j in range(0,len(df2['Resources'])):
        a=encontrar(df2,j,200)
        if len(str(a))>1:
          b=a[1]
          c=a[1]+a[0]
          resultadoM.append((df2['Resources'][j]['@types'][b+1:c+1],df2['Resources'][j]['@surfaceForm']))
          #print(resultadoM)
      texto=str(df["article"][l])
      texto="Texto:{ " + texto + " }" + "Entidades: { "
      for y in range(0,len(resultadoM)):
        #print(resultadoM[y])
        if final.count(resultadoM[y][1])==0:
          final.append(resultadoM[y][1])
          final2.append(resultadoM[y][0])
      #print(final)
      for x in range(0,len(final)):
        texto = texto + str(final[x]) + " es " + reemplazar(str(final2[x])) + ", "
      texto = texto + "}"
      resultadooo.append(texto)
    except Exception as e:
      texto=str(df["article"][l])
      errores=errores+1
      texto="Texto:{ " + texto + " }" + "Entidades: {}"
      resultadooo.append(texto)
      print(e)
  errores
  
  pd4=pd.DataFrame(resultadooo,df["summary"])
  pd4.to_csv("../data/700tokensTrainEnt.csv", sep=';')

  df = pd.read_csv("../data/700tokens.csv", sep=";")
  df["summary"]=df["1"]
  df["article"]=df["0"]

  errores=0
  resultadooo=[]
  for l in range(0,718113):
    try:
      df2 = pd.read_json("./train/train/text"+str(l)+".json")
      resultadoM=[]
      final=[]
      final2=[]
      for j in range(0,len(df2['Resources'])):
        a=encontrar(df2,j,200)
        if len(str(a))>1:
          b=a[1]
          c=a[1]+a[0]
          resultadoM.append((df2['Resources'][j]['@types'][b+1:c+1],df2['Resources'][j]['@surfaceForm']))
      texto=str(df["article"][l])
      texto="Texto:{ " + texto + " }" + "Entidades: { "
      for y in range(0,len(resultadoM)):
        if final.count(resultadoM[y][1])==0:
          final.append(resultadoM[y][1])
          final2.append(resultadoM[y][0])
      for x in range(0,len(final)):
        texto = texto + str(final[x]) + " es " + reemplazar(str(final2[x])) + ", "
      texto = texto + "}"
      resultadooo.append(texto)
    except Exception as e:
      texto=str(df["article"][l])
      errores=errores+1
      texto="Texto:{ " + texto + " }" + "Entidades: {}"
      resultadooo.append(texto)
      print(e)
  errores
  pd5=pd.DataFrame(resultadooo,df["summary"])
  pd5.to_csv("../data/700tokensTrainEnti.csv", sep=';')

  df = pd.read_csv("700tokensTest-i.csv", sep=";")
  df["summary"]=df["1"]
  df["article"]=df["0"]

  errores=0
  resultadooo=[]
  for l in range(0,42559):
    try:
      df2 = pd.read_json("./test/test/text"+str(l)+".json")
      resultadoM=[]
      final=[]
      final2=[]
      for j in range(0,len(df2['Resources'])):
        a=encontrar(df2,j,200)
        if len(str(a))>1:
          b=a[1]
          c=a[1]+a[0]
          resultadoM.append((df2['Resources'][j]['@types'][b+1:c+1],df2['Resources'][j]['@surfaceForm']))
          #print(resultadoM)
      texto=str(df["article"][l])
      texto="Texto:{ " + texto + " }" + "Entidades: { "
      for y in range(0,len(resultadoM)):
        #print(resultadoM[y])
        if final.count(resultadoM[y][1])==0:
          final.append(resultadoM[y][1])
          final2.append(resultadoM[y][0])
      #print(final)
      for x in range(0,len(final)):
        texto = texto + str(final[x]) + " es " + reemplazar(str(final2[x])) + ", "
      texto = texto + "}"
      resultadooo.append(texto)
    except Exception as e:
      texto=str(df["article"][l])
      errores=errores+1
      texto="Texto:{ " + texto + " }" + "Entidades: {}"
      resultadooo.append(texto)
      print(e)
  errores
  
  pd6=pd.DataFrame(resultadooo,df["summary"])
  pd6.to_csv("../data/700tokensTestiEnt.csv", sep=';')