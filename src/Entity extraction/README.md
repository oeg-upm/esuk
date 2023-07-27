
# Usage
1. Once Docker is installed run (or dowload if its the first use) the following comand to run the dbpedia spolight entity extractor
```bash
docker run -tid --restart unless-stopped --name dbpedia-spotlight.es --mount source=spotlight-model,target=/opt/spotlight -p 2222:80 dbpedia/dbpedia-spotlight spotlight.sh es
```
2. Run the .py scripts