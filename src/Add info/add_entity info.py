  import pandas as pd
  from SPARQLWrapper import SPARQLWrapper, JSON

  def encontrar(strr):
    a="0"
    uri=strr
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)


    sparql.setQuery("""
    PREFIX dbo: <http://dbpedia.org/ontology/>
    PREFIX res: <http://dbpedia.org/resource/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?label
    WHERE { <"""+str(uri)+""">
              dbo:abstract ?label . FILTER (lang(?label) = \'en\')}
      """
    )

    try:
        ret = sparql.queryAndConvert()

        res=ret["results"]["bindings"][0]['label']["value"]
        return(res)
    except Exception as e:
        return(a)


  df = pd.read_csv("../../data/700tokensVal.csv", sep=";")
  df["summary"]=df["1"]
  df["article"]=df["0"]
  df1 = pd.read_json("../../data/val/val/text1.json")
  errores=0
  resultadooo=[]
  for l in range(0,42597):
    texto=str(df["article"][l])
    try:
      df2 = pd.read_json("./val/val/text"+str(l)+".json")
      for j in range(0,len(df2['Resources'])):
        uri = df2['Resources'][j]["@URI"]
        if encontrar(uri)=="0":
          b=0
        else:
          abstract=encontrar(uri)[0:60]
          texto=texto + df2['Resources'][j]['@surfaceForm'] + ": " + abstract
      resultadooo.append(texto)
    except Exception as e:
      resultadooo.append(texto)
  
  pd4=pd.DataFrame(resultadooo,df["summary"])
  pd4.to_csv("../../data/700tokensTrainEnt.csv", sep=';')

  df = pd.read_csv("../../data/700tokens.csv", sep=";")
  df["summary"]=df["1"]
  df["article"]=df["0"]

  resultadooo=[]
  for l in range(0,718113):
    texto=str(df["article"][l])
    try:
      df2 = pd.read_json("../../data/train/train/text"+str(l)+".json")
      for j in range(0,len(df2['Resources'])):
        uri = df2['Resources'][j]["@URI"]
        if encontrar(uri)=="0":
          b=0
        else:
          abstract=encontrar(uri)[0:60]
          texto=texto + df2['Resources'][j]['@surfaceForm'] + ": " + abstract
      resultadooo.append(texto)
    except Exception as e:
      resultadooo.append(texto)
  pd5=pd.DataFrame(resultadooo,df["summary"])
  pd5.to_csv("../../data/700tokensTrainEnti.csv", sep=';')

  df = pd.read_csv("../../data/700tokensTest-i.csv", sep=";")
  df["summary"]=df["1"]
  df["article"]=df["0"]
  resultadooo=[]
  for l in range(0,42597):
    texto=str(df["article"][l])
    try:
      df2 = pd.read_json("../../data/test/test/text"+str(l)+".json")
      for j in range(0,len(df2['Resources'])):
        uri = df2['Resources'][j]["@URI"]
        if encontrar(uri)=="0":
          b=0
        else:
          abstract=encontrar(uri)[0:60]
          texto=texto + df2['Resources'][j]['@surfaceForm'] + ": " + abstract
      resultadooo.append(texto)
    except Exception as e:
      resultadooo.append(texto)
  
  pd4=pd.DataFrame(resultadooo,df["summary"])
  pd4.to_csv("../../data/700tokensTrainEnt.csv", sep=';')

  df = pd.read_csv("../../data/700tokens.csv", sep=";")
  df["summary"]=df["1"]
  df["article"]=df["0"]


  
  pd6=pd.DataFrame(resultadooo,df["summary"])
  pd6.to_csv("../data/700tokensTestiEnt.csv", sep=';')