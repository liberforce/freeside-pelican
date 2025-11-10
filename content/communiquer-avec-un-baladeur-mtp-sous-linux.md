Title: Communiquer avec un baladeur MTP sous Linux
Date: 2007-10-12 09:31
Author: liberforce
Category: Computers / Informatique
Tags: baladeur numérique, matériel, linux
Slug: communiquer-avec-un-baladeur-mtp-sous-linux
Status: published

<a href="\%22http://www.figuiere.net/\%22" hreflang="\&quot;en\&quot;">Hub</a> m'a fait remarquerque le <a href="\%22http://en.wikipedia.org/wiki/Media_Transfer_Protocol\%22" hreflang="\&quot;en\&quot;">MTP</a> était mieux géré<a href="\%22/post/2007/10/12/Choisir-son-baladeur-numerique-compatible-Linux-et-Ogg/Vorbis\%22" hreflang="\&quot;fr\&quot;">que je ne le pensais</a> sous Linux. J'en conclus par conséquent que si l'on nesouhaite pas vraiment faire une utilisation "clé USB", un baladeur MTP est unesolution acceptable.

Il semble qu'il y a principalement deux bibliothèques qui permettent ledialogue avec des périphériques MTP: <a href="\%22http://www.gphoto.org/proj/libgphoto2/\%22" hreflang="\&quot;en\&quot;">libgphoto2</a> et <a href="\%22http://libmtp.sourceforge.net/\%22" hreflang="\&quot;en\&quot;">libmtp</a>. ~~Ces deux projets sontdes forks~~ libmtp est un fork d'un autre projet, toujours actif,<a href="\%22http://libptp.sourceforge.net/\%22" hreflang="\&quot;en\&quot;">libptp2</a>.

Pour chaque projet, vous consulter une liste des périphériques gérés.

- <a href="\%22http://www.gphoto.org/proj/libgphoto2/support.php\%22" hreflang="\&quot;en\&quot;">Liste de compatibilitélibgphoto2</a>
- <a href="\%22http://libmtp.sourceforge.net/index.php?page=compatibility\%22" hreflang="\&quot;en\&quot;">Liste decompatibilité libmtp</a>

Mais il est parfois difficile de savoir quels baladeurs sont rajoutés dansles toutes dernières versions (surtout pour des modèles très récents). Vouspouvez alors si le coeur vous en dit voir dans le source si votre modèle estgéré, et envoyer un patch ou les quelques informations nécessaires dans le casoù il ne l'est pas.

- <a href="\%22http://gphoto.svn.sourceforge.net/viewvc/gphoto/trunk/libgphoto2/camlibs/ptp2/library.c?view=markup\%22" hreflang="\&quot;en\&quot;">Liste de compatibilité libgphoto2 (SVN)</a>
- <a href="\%22http://libmtp.cvs.sourceforge.net/libmtp/libmtp/src/libusb-glue.c?revision=1.231&amp;view=markup\%22" hreflang="\&quot;en\&quot;">Liste de compatibilité libmtp (CVS)</a>

Au niveau des lecteurs utilisant ces bibliothèques, on peut citer (entreautres) <a href="\%22http://www.banshee-project.org\%22" hreflang="\&quot;en\&quot;">Banshee</a> quiutilise libgphoto2, et <a href="\%22http://www.gnome.org/projects/rhythmbox/\%22" hreflang="\&quot;en\&quot;">rhythmbox</a> qui utiliselibmtp.

</p>
