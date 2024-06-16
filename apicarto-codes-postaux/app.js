document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const postalCode = document.getElementById('postalCode').value;
    const resultsList = document.getElementById('results');
    resultsList.innerHTML = '';

    /*
     * NOTE : GPT-4o doit être en mesure de lire les spécifications OpenAPI pour découvrir cet appel
     */ 
    fetch(`https://apicarto.ign.fr/api/codes-postaux/communes/${postalCode}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            /*
             * NOTE : GPT-4o traite la gestion des erreurs
             */
            if (data.length === 0) {
                resultsList.innerHTML = '<li>Aucun code INSEE trouvé pour ce code postal.</li>';
            } else {
                data.forEach(commune => {
                    const listItem = document.createElement('li');
                    /*
                     * NOTE : GPT-4o doit être en mesure de lire la structure de la réponse dans ces spécifications
                     * Il prend l'initiative de présenter le nom de la commune.
                     */
                    listItem.textContent = `Commune: ${commune.nomCommune} - Code INSEE: ${commune.codeCommune}`;
                    resultsList.appendChild(listItem);
                });
            }
        })
        .catch(error => {
            resultsList.innerHTML = `<li>Une erreur s'est produite: ${error.message}</li>`;
        });
});