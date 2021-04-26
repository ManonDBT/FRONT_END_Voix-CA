# Front-End Voix-CA 

### Voix-CA est une application qui permet aux collaborateurs de 	      rédiger leurs entretiens commerciaux. 
 
Le principe de l'API est la création de la base de donnée ainsi que l'implémentation du modèle de machine learning. L' API est en lien directe avec le Front End Voix-CA. 

L'API est divisé en 3 parties : 
- La conception de la [base de donnée](https://github.com/ManonDBT/API_Voix-CA/blob/main/create_base.py)
- Le modèle de [machine learning](https://github.com/ManonDBT/Flask_VoixCA_API/tree/dev/machine_learning) 
- Les routes pour former l'[API](https://github.com/ManonDBT/API_Voix-CA/blob/main/api.py)

# Base de donnée

La base de données est créée à partir de SQLAlchemy, les liens entre les tables sont dites relationnelles. 
 

![schéma](https://drive.google.com/uc?export=view&id=16mQdSd7UqdwKVERcrHLy4m89FnlTE0hf)


## Table Client 

La table client regroupe tous les clients enregistrés dans le système d'information. 

## Table Data

La table data retourne les comptes rendus avec l'identifiant du client, du collaborateur qui l'a rédigé ainsi que la date de la création du compte rendu. 

## Table Catégorie

La table catégorie centralise les thématiques qui peuvent être abordées lors d'un entretien commercial. 




# Machine learning

La problématique qui se pose ici est une classification. Le modèle devra donc prédire les thématiques abordées lors d'un compte-rendu d'entretien commercial. 

- [Notebook](https://github.com/ManonDBT/API_Voix-CA/blob/main/machine_learning/Multi-label_final.ipynb)
- [MLFlow](https://github.com/ManonDBT/API_Voix-CA/blob/main/machine_learning/ML.py) 



# API

- [Catégorie](https://github.com/ManonDBT/API_Voix-CA/blob/main/docs-swagger/categories.yml)
- [Clients](https://github.com/ManonDBT/API_Voix-CA/blob/main/docs-swagger/clients.yml)
- [Data](https://github.com/ManonDBT/API_Voix-CA/blob/main/docs-swagger/data.yml) 
