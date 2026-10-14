---
date: 20240731
---

# Quelques notes sur un test intégration du service altimétrie de la Géoplateforme dans ChatGPT

> **DÉPRÉCIÉ** : L'intégration d'un appel d'API sous forme d'une action ChatGPT est aujourd'hui remplacée par l'utilisation de serveurs MCP ou de skills.

## Objectif

Tester l'intégration du service altimétrie de la Géoplateforme dans ChatGPT sous forme d'une action.

## Principe

* [gpf-altitude.yaml](gpf-altitude.yaml) - Rédaction d'une document OpenAPI minimale pour le [service Géoplateforme de calcul altimétrique](https://geoservices.ign.fr/documentation/services/services-geoplateforme/altimetrie)

* Intégration sous forme d'une action ChatGPT :

![alt text](2024-07-31-gpf-altimetrie.png) 

* Prompt pour test :

```
Tu es un assistant fournissant diverses informations à l'aide d'appel aux API géoplateforme (data.geopf.fr). Au besoin, tu récupères les positions en faisant appels aux services de géocodage de google map.

Remarques : 

- Pour l'altimétrie, tu utiliseras resource=ign_rge_alti_wld
- Tu préciseras les sources des informations dans tes réponses
```

