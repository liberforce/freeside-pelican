Title: Communiquer avec un baladeur MTP sous Linux
Date: 2007-10-21 23:03
Author: LM2153-GANDI
Category: Computers / Informatique
Tags: baladeur numérique, matériel, linux
Slug: communiquer-avec-un-baladeur-mtp-sous-linux
Status: published

<a href="http://www.figuiere.net/" hreflang="en">Hub</a> m'a fait remarquerque le <a href="http://en.wikipedia.org/wiki/Media_Transfer_Protocol" hreflang="en">MTP</a> était mieux géré<a href="/post/2007/10/12/Choisir-son-baladeur-numerique-compatible-Linux-et-Ogg/Vorbis" hreflang="fr">que je ne le pensais</a> sous Linux. J'en conclus par conséquent que si l'on nesouhaite pas vraiment faire une utilisation "clé USB", un baladeur MTP est unesolution acceptable.

Il semble qu'il y a principalement deux bibliothèques qui permettent ledialogue avec des périphériques MTP: <a href="http://www.gphoto.org/proj/libgphoto2/" hreflang="en">libgphoto2</a> et <a href="http://libmtp.sourceforge.net/" hreflang="en">libmtp</a>. ~~Ces deux projets sontdes forks~~ libmtp est un fork d'un autre projet, toujours actif,<a href="http://libptp.sourceforge.net/" hreflang="en">libptp2</a>.

Pour chaque projet, vous consulter une liste des périphériques gérés.

- <a href="http://www.gphoto.org/proj/libgphoto2/support.php" hreflang="en">Liste de compatibilitélibgphoto2</a>
- <a href="http://libmtp.sourceforge.net/index.php?page=compatibility" hreflang="en">Liste decompatibilité libmtp</a>

Mais il est parfois difficile de savoir quels baladeurs sont rajoutés dansles toutes dernières versions (surtout pour des modèles très récents). Vouspouvez alors si le coeur vous en dit voir dans le source si votre modèle estgéré, et envoyer un patch ou les quelques informations nécessaires dans le casoù il ne l'est pas.

- <a href="http://gphoto.svn.sourceforge.net/viewvc/gphoto/trunk/libgphoto2/camlibs/ptp2/library.c?view=markup" hreflang="en">Liste de compatibilité libgphoto2 (SVN)</a>
- <a href="http://libmtp.cvs.sourceforge.net/libmtp/libmtp/src/libusb-glue.c?revision=1.231&amp;view=markup" hreflang="en">Liste de compatibilité libmtp (CVS)</a>

Au niveau des lecteurs utilisant ces bibliothèques, on peut citer (entreautres) <a href="http://www.banshee-project.org" hreflang="en">Banshee</a> quiutilise libgphoto2, et <a href="http://www.gnome.org/projects/rhythmbox/" hreflang="en">rhythmbox</a> qui utiliselibmtp.

</p>
