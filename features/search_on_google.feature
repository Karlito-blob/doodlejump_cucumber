Feature: Recherche sur Google

  En tant qu'utilisateur, je peux effectuer une recherche sur Google

  Scenario: Un utilisateur effectue une recherche sur Google pour trouver le jeu Doodle Jump sur Google Play
    Given je suis sur la page d'accueil de Google
    When je recherche le jeu 'Doodle Jump'
    Then je trouve le lien Google Play pour 'Doodle Jump' dans les 10 premiers résultats de recherche