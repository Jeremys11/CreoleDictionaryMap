# CreoleDictionaryMap
A Web-Based Mapping of Creole Language Dictionaries using Github Pages.

Forked from https://github.com/Al-Rey/cmsc436-Creole-langages

Changes from previous version:

  Flask is no longer used as the web application framework. Web app has transitioned to Javascript with Python only being used for data scraping and cleaning.
  
  Previous web app was hosted on Pythonanywhere. Web app then was migrated to an Azure Static Web App. And finally to Github Pages which can be found here [Link to Github Pages](https://jeremys11.github.io/CreoleDictionaryMap/)
  
  Data was previously read directly from excel files. Now, all dictionaries have been combined into a single .json file.
  
  From previous hosting - Azure requires edits to the web.config file to properly read .json files. The changes required can be found in the web.config file in this repository [web.config](https://github.com/Jeremys11/CreoleDictionaryMap/blob/main/web.config)

  Since this project did not need to use Jekyll - .nojekyll file was included in root, because Github Pages used Jekyll by default
  

![Link to IEEE Paper](https://github.com/Jeremys11/CreoleDictionaryMap/blob/main/Creole%20Dictionay%20Map%20IEEE%20Paper.pdf)

![Poster](https://github.com/Jeremys11/CreoleDictionaryMap/blob/main/CreoleLinguisticsPoster.png?raw=true)
