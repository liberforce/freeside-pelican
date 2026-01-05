---
title: "De retour !"
date: "2026-01-05 11:18"
author: "liberforce"
category: "Life / Vie quotidienne"
tags: "life, job"
slug: "de-retour"
lang: "fr"
status: "published"
---

Après une longue période hors ligne, ce blog est de retour ! Un blog en 2026,
quel intérêt me direz vous ? Les réseaux sociaux les ont rendus obsolètes.

Le but initial était surtout d'archiver mon
ancien blog dotclear qui avait fermé après l'arrêt du service par mon hébergeur
de l'époque. Pour conserver une trace du passé. Mais en vrai, il y a aussi une
valeur à un blog, pas que affective pour les articles qui me manquaient.
Celle de journal de bord pour décrire une tâche qu'on
a effectué et dont on a besoin des mois plus tard en se disant « mais comment
j'avais fait à l'époque » ?

J'avais déjà fait une tentative de migration vers un blog statique
[pelican](https://getpelican.com), mais leur outil de migration a vite trouvé
ses limites. J'ai donc profité de ma lecture du livre de Martin Fowler et Kent
Beck, [Refactoring: Improving the design of existing
code](https://martinfowler.com/books/refactoring.html) pour réusiner le code de
l'outil de migration tout en lui donnant plus de souplesse.

# Qu'ai-je appris sur le chemin ?

## Pandoc pour les conversions entre formats

Pelican utilise pandoc pour la conversion de fichiers RST ou Markdown. Pandoc a
un écosystème assez particulier, du fait qu'il est développé en Haskell. Ma
distribution Linux, [Mageia](https://www.mageia.org) ne fournit pas de paquets
pour l'installer. J'ai d'abord utilisé une image Docker officielle (pas sûr
qu'elle existait en 2017).

## Markdown et sa floppée de variantes

Pandoc a sa propre variante de Markdown: le [Pandoc's
Markdown](https://pandoc.org/MANUAL.html#pandocs-markdown). Cela lui permet de
cibler des conversions encore plus riches entre divers formats. J'ai donc fait
le choix de faire l'impasse sur le Markdown GitHub (appelé gfm chez pandoc:
GitHub-flavored Markdown), car le Markdown de Pandoc ouvre plus de possibilités
en tant que format pivot... Et que j'avais d'autres projets qui pouvaient en
bénéficier à l'avenir.

## Conda

Pandoc via Docker était pratique, mais il fallait gérer le cycle de vie de
l'image manuellement, garder l'exécutable accessible pour éviter l'overhead
entre chaque appel... ce n'était pas le plus pratique. Au final j'ai installé
pandoc dans un environnement virtuel dédié grâce à
[Conda](https://anaconda.org/channels/anaconda/packages/conda/overview), qui me
permet de l'avoir facilement dans mon `PATH`, sans gestion supplémentaire.
Comme quoi c'est utile de regarder sur les petites annonce d'emploi les stacks
utilisées. Je n'avais jamais utilisé Conda, mais il m'a permis d'installer
pandoc très facilement.

## Un cas concret de refactoring

L'outil officiel permettant de convertir un blog au format pelican, c'est
`pelican-import`. Mais le code de ce dernier n'est spécialement bien découpé,
on va au plus simple. La contrepartie c'est qu'il est difficile de le
personnaliser à ses propres besoins (alors que cette personnalisation est
essentielle, car les formats sources sont multiples et les options changent
leur interprétation), et de comprendre à quelle étape de l'import est-ce qu'il
y a un problème.

L'ajout de tests a permis de vérifier les différentes hypotèses et d'avancer
sereinement dans le refactoring. Apporter des noms sur des concepts au fur et à
mesure que je comprenais la base de code. Et au final de trouver les quelques
bugs qui cassaient le formatage.

# Réutilisation des connaissances

## Pandoc pour la génération de quittance de loyer

J'avais déjà travaillé sur ce genre de problématiques dans le cadre
professionnel. Un exemple me vient en tête: la génération de release notes.
J'avais effectué cela en utilisant Jinja2, le moteur de template, et secretary,
un module python pour la gestion de l'OpenDocument. Je me rends compte a
postériori que cela aurait été un parfait candidat pour de la génération par
pandoc, qui gère aussi l'OpenDocument.

J'ai depuis utilisé pandoc pour un autre petit projet: `quittance`, un
générateur de quittances de loyer, qui transforme un template markdown en
quittance PDF pré-signée.

## Conda pour gérer un python legacy

Conda de son côté m'a servi aussi servi par la suite. Comme beaucoup j'ai
changé d'hébergeur quand [Gandi](https://www.gandi.net) a augmenté ses tarifs il y
a une paire d'années, pour atterrir chez [OVHcloud](http://ovhcloud.com). Je
l'utilise pour avoir des adresses email perso et pro associées à mon propre nom
de domaine, plus que pour l'hébergement d'ailleurs. Mais quitte à payer
l'hébergement, autant s'en servir, ce qui a aussi un peu servi de motivation à
la résurrection de ce blog. Or l'hébergement OVHcloud pour leur offre la moins
chère ne fournit que python 3.7, qui est si vieux que `uv`, mon gestionnaire de
projets python de prédilection ne le fournit même plus. C'est là que conda
entre en jeu, fournissant facilement un environnement avec python 3.7, et me
permettant de reproduire à l'identique localement l'environnement de mon
hébergement.

# Conclusion

Même de modestes projets on des choses à enseigner. J'ai fini par me prendre au
jeu, et trouvé de nouvelles manières de résoudre des problèmes du quotidien.
Étant aussi syndic bénévole, je pense par exemple à la génération automatique
de procès verbaux d'assemblées générales avec pandoc et ses templates.
