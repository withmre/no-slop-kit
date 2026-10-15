# No Slop Kit pour Claude Code

Des règles globales et sept skills pour Claude Code. Avec eux, Claude écrit moins de code, n'invente rien, consomme moins de tokens et arrête de produire les textes et les designs qui font dire « ça, c'est une IA ».

![Licence : MIT](https://img.shields.io/badge/license-MIT-blue) ![PR bienvenues](https://img.shields.io/badge/PRs-welcome-brightgreen) ![Claude Code](https://img.shields.io/badge/for-Claude%20Code-d97757) ![Étoiles GitHub](https://img.shields.io/github/stars/withmre/no-slop-kit?style=social)

[English version](README.md)

![Animation : /deslop surligne un à un les 11 marqueurs d'écriture IA d'un paragraphe, puis affiche la version réécrite avec toutes les idées gardées](assets/deslop-demo-fr.gif)

## Pourquoi ce kit

Je crée des sites avec l'IA tous les jours, et elle me fait gagner des heures. Elle me ressortait aussi toujours les mêmes choses : des tirets cadratins partout, des « ce n'est pas X, c'est Y », des dégradés violets, trois cartes avec une icône au-dessus, de faux témoignages, un paquet qui n'existe pas, 400 lignes réécrites pour corriger une ligne.

Je suis contre le slop pour une raison simple. L'IA devrait nous rendre du temps pour les idées et la création. Le slop fait l'inverse : il nous laisse arrêter de réfléchir, et tous les sites, tous les textes finissent par se ressembler.

J'ai donc noté chaque règle que je répétais à Claude et j'en ai fait un kit que tout le monde peut installer en quelques minutes. Il est gratuit et ouvert. J'accepte toutes les propositions : ouvre une issue, ou envoie directement une pull request.

## La preuve par l'exemple

Voici ce que fait `/deslop` sur un paragraphe typique écrit par une IA. L'animation en haut de page rejoue cet exemple à partir du rapport du skill.

**Avant**

> Dans un monde en constante évolution, créer un site web ne se résume plus au code — c'est avant tout une expérience. Que vous soyez freelance ou grande entreprise, notre solution innovante vous permet de booster votre visibilité. Le résultat ? Plus de clients, plus de temps, plus de sérénité. Ce n'est pas un outil. C'est un véritable levier de croissance.

**Après**

> Un site web doit aussi être agréable à utiliser. Notre solution aide les freelances comme les grandes entreprises à se faire connaître : vous y gagnez des clients, du temps et de la sérénité, et votre activité grandit.

**Le rapport du skill : « Ce que j'ai retiré »**

| Avant | Après | Pourquoi |
|---|---|---|
| « Dans un monde en constante évolution » | supprimé | Généralité qui irait dans n'importe quel texte |
| « — » | phrase reconstruite | Tiret cadratin, toujours retiré |
| « ne se résume plus au code, c'est avant tout une expérience », « Ce n'est pas un outil. C'est un véritable levier de croissance. » | « doit aussi être agréable à utiliser », « votre activité grandit » | « Ce n'est pas X, c'est Y », deux fois. L'idée de croissance est gardée, la formule part |
| « Que vous soyez freelance ou grande entreprise » | « les freelances comme les grandes entreprises » | Ouverture toute faite |
| « innovante », « booster », « véritable », « levier » | retirés | Vocabulaire banni et intensif creux |
| « Le résultat ? » | supprimé | Question rhétorique suivie de sa réponse |
| « Plus de clients, plus de temps, plus de sérénité. » | « des clients, du temps et de la sérénité », dans une phrase | Anaphore en trois temps par réflexe : l'énumération reste, la formule martelée part |

Marqueurs : 11 avant, 0 après.

Toutes les idées de départ sont encore là. Le skill change la forme, garde les exemples de l'auteur et signale ce qu'il ne peut pas vérifier. Il n'invente jamais un chiffre pour muscler une phrase.

Ce README est passé par le même skill avant publication.

## Même brief, avec et sans le kit

![Animation : trois pages faites avec les réflexes par défaut des sites générés par IA, chacune balayée pour révéler la version faite avec le skill ui-design, qui joue sa propre animation puis défile jusqu'en bas](assets/web-before-after.gif)

Trois briefs simples : la page d'accueil d'une appli de facturation, une boulangerie de quartier, le portfolio d'une designer. Chacun apparaît deux fois. La première version reproduit les réflexes que vise le skill `ui-design`, ceux qu'on obtient quand rien ne guide le modèle : dégradés violets, héros centré, emojis en guise d'icônes, chiffres inventés. La seconde suit le skill, à partir d'un brief avec une référence réelle : le carnet à souches et ses copies carbone pour l'appli de facturation, les devantures peintes du vieux Lyon pour la boulangerie, un carnet de recherche annoté au crayon bleu pour le portfolio. Chacune a sa structure, sa palette et sa paire de polices, et sa seule animation montre quelque chose de vrai sur le produit : la facture reçoit son tampon « payée », les horaires du four indiquent la prochaine fournée, les annotations expliquent la méthode de la designer.

Les six pages sont en HTML simple dans [`assets/src/pages`](assets/src/pages). Ouvre-les et compare le code. Les polices sont auto-hébergées sous licence SIL Open Font. Les marques, les personnes et les prix sont fictifs.

## Ce qu'il contient

| Fichier | Rôle | Chargé quand |
|---|---|---|
| `CLAUDE.md` | Règles globales : ne rien inventer, dev paresseux, économie de tokens, socle de sécurité, style d'écriture | À chaque session |
| `settings.json` | Empêche les outils de lecture de Claude d'ouvrir les `.env`, les lockfiles et les dossiers de build, et demande avant quelques commandes destructrices | À chaque session |
| `skills/deslop` | En mode relecture, réécrit un texte et montre ce qui a été retiré. En mode écriture, applique les mêmes règles sans rien dire. Catalogues français et anglais | Sur les textes à publier, ou `/deslop` |
| `skills/ui-design` | Brief et structure de page, catalogue des tics, mise en page, couleur, typo, tokens, plancher mobile, composants, auto-évaluation notée, mode audit et checklist de lancement | Sur tout travail d'interface, ou `/ui-design` |
| `skills/security` | 19 sections, des secrets aux webhooks et aux paiements, plus un audit avant mise en ligne avec des commandes concrètes | Sur l'auth, les données, les API, les paiements, ou `/security` |
| `skills/reliability` | Limites de requêtes, plafonds d'API, délais d'attente, états vides et d'erreur, index, cache, surveillance, sauvegardes restaurables | Sur les données, les API et le déploiement |
| `skills/container-security` | Vérifications des images et de l'exécution Docker, Compose et Kubernetes, avec ports, secrets, privilèges et limites de ressources | Sur les conteneurs ou le déploiement |
| `skills/production-readiness` | Oriente un audit de mise en ligne vers les skills utiles, avec modèle de menace, capacité et rapport partagé P0/P1/P2 | Avant une mise en ligne publique, une forte affluence ou `/production-readiness` |
| `skills/project-setup` | Écrit le `CLAUDE.md` d'un projet à partir des fichiers du dépôt, sans rien inventer | Seulement avec `/project-setup` |

## Ce que ça change

### Le code

Claude vérifie la version installée d'une bibliothèque avant d'utiliser son API, et vérifie qu'un paquet existe avant de l'installer : un nom halluciné peut correspondre à un paquet malveillant. Il cite `fichier:ligne` quand il parle de ton code. Avant d'écrire, il descend une échelle : supprimer, réutiliser, fonction native de la plateforme, bibliothèque standard, dépendance déjà installée. Le nouveau code arrive en dernier. Le diff reste le plus petit possible, sans refactorisation bonus, et Claude n'affirme jamais avoir testé ce qu'il n'a pas lancé.

« Paresseux » veut dire ici paresseux sur le code : moins Claude écrit, moins tu as à relire. La réflexion, elle, reste ton travail.

### Les tokens

Claude cherche avant de lire, ignore les lockfiles et les dossiers de build, lance un seul fichier de test pendant qu'il itère et la suite complète une fois, et termine une tâche en trois lignes. Le `CLAUDE.md` principal reste sous les 200 lignes recommandées par Anthropic. Un skill ne coûte que sa description tant qu'une tâche n'en a pas besoin.

### Le design

Pour un nouveau site ou une refonte, Claude rédige un court brief avec une référence réelle avant de coder, et propose deux directions si rien n'est fixé. Il choisit une structure de page adaptée au contenu (une lettre, un index, le produit montré d'abord) au lieu du rythme héros, trois atouts, appel à l'action. Il écarte son premier réflexe de police et de couleur, parce que ce réflexe est le même sur tous les projets, et note ses choix dans un `DESIGN.md` pour que les pages suivantes restent cohérentes.

Avant de montrer une page, il se note sur six axes (intention, hiérarchie, exécution, spécificité, retenue, variété) et reprend tout ce qui est sous 3. Puis il liste chaque motif par défaut encore présent : « choisi, parce que… », ou retiré. `/ui-design audit` fait les mêmes vérifications sur un site existant et rend une liste classée, sans toucher au code.

### Les textes

Pas de tiret cadratin, pas de « ce n'est pas X, c'est Y », pas de « plongeons », pas de question rhétorique suivie de sa réponse. La liste complète est dans les catalogues de deslop.

### Sécurité et fiabilité

Vérifications côté serveur sur chaque route, sécurité au niveau des lignes sur chaque table, prix calculés sur le serveur, commandes validées sur un webhook vérifié, délai d'attente sur chaque appel externe, limites explicites pour les conteneurs, et des sauvegardes dont la restauration a été testée. Avant une mise en ligne publique ou une forte affluence, `/production-readiness` rassemble ces vérifications et classe les écarts en P0, P1 et P2.

## Installer

### Laisser Claude Code s'en charger

```bash
git clone https://github.com/withmre/no-slop-kit.git
cd no-slop-kit
claude
```

Puis tape :

```
Lis INSTALL.md et installe ce kit.
```

Claude sauvegarde ta configuration actuelle, demande avant de remplacer quoi que ce soit, fusionne ton `settings.json` au lieu de l'écraser, puis vérifie le résultat.

### À la main (macOS, Linux, WSL)

```bash
mkdir -p ~/.claude/skills
cp -r claude-home/skills/* ~/.claude/skills/
[ -e ~/.claude/CLAUDE.md ] || cp claude-home/CLAUDE.md ~/.claude/
[ -e ~/.claude/settings.json ] || cp claude-home/settings.json ~/.claude/
```

Les deux dernières lignes ne copient `CLAUDE.md` et `settings.json` que si tu ne les as pas déjà. Sinon, fusionne-les à la main. La copie des skills écrase ceux qui portent le même nom.

Ouvre une nouvelle session, tape `/` pour voir les skills, et lance `/context` pour vérifier que les règles sont chargées.

## Utiliser

La plupart du temps, tu n'as rien à faire : Claude charge chaque skill quand la tâche le demande. Tu peux aussi les appeler toi-même :

- `/deslop` suivi de ton texte, ou du chemin d'un fichier ;
- `/ui-design` avant de commencer une page ou une refonte, `/ui-design audit` sur un site existant ;
- `/security` pour un audit avant mise en ligne, `/reliability` pour vérifier limites, erreurs et sauvegardes ;
- `/container-security` pour Docker, Compose ou Kubernetes, `/production-readiness` avant une mise en ligne publique ou une forte affluence ;
- `/project-setup` une fois dans chaque nouveau dépôt.

## L'adapter

Claude répond en anglais par défaut. Le kit est public et ses consignes sont en anglais : c'est la langue par défaut qui convient au plus grand nombre et coûte le moins de tokens. Pour répondre en français, remplace la ligne « Reply in English by default » de `CLAUDE.md` par « Always reply in French ». La section 8 du même fichier contient les règles d'écriture, avec des exemples en français et en anglais.

Les mots bannis sont dans `skills/deslop/fr.md` et `skills/deslop/en.md`. Ajoute les tiens.

Chaque ligne de `CLAUDE.md` coûte des tokens à chaque session : retire ce qui ne te sert pas.

Les consignes sont écrites en anglais parce que le même texte y prend moins de tokens. Tout ce qui touche au français (mots bannis, tournures, typographie, mentions légales) reste en français.

## Les habitudes qui économisent le plus

- `/clear` entre deux tâches sans rapport ;
- `/compact` avec une consigne quand une session s'allonge : `/compact garde les décisions sur le schéma` ;
- le mode plan (`Shift+Tab`) pour une grosse tâche, et `Échap` dès que Claude part dans la mauvaise direction ;
- `/mcp` pour couper les serveurs inutiles ;
- des demandes précises, avec le nom du fichier.

## Contribuer

J'accepte toutes les propositions, et les pull requests sont bienvenues sans demander avant. L'objectif est d'aider le plus de monde possible à bien utiliser l'IA.

Ce qui aiderait le plus :

- un catalogue deslop dans ta langue : espagnol, allemand, portugais, italien ;
- les tics d'IA que tu croises et que les catalogues ratent ;
- les réflexes de design des dernières galeries de composants ;
- des vérifications de sécurité, de fiabilité ou de conteneurs pour une stack pas encore couverte ;
- les faux positifs : une règle qui a rendu Claude moins bon. Ils comptent autant que les nouvelles règles.

Le détail est dans [CONTRIBUTING.md](CONTRIBUTING.md).

Si le kit t'a évité une réécriture, une étoile aide d'autres personnes à le trouver.

## Merci

Deux skills open source ont aiguisé ce kit : [Hallmark](https://github.com/nutlope/hallmark), pour l'idée de varier la structure des pages, l'auto-évaluation notée et beaucoup de tics de design précis, et [anti-ai-slop-writing](https://github.com/jalaalrd/founder-toolkit), pour les règles sur la parataxe, la balance prudente et l'écriture sans rien inventer. Leurs idées sont réécrites ici avec les mots du kit et adaptées à ses règles. Les deux sont sous licence MIT et valent le détour.

## Évolution des étoiles

[![Courbe des étoiles](https://api.star-history.com/svg?repos=withmre/no-slop-kit&type=Date)](https://star-history.com/#withmre/no-slop-kit&Date)

## Licence

[MIT](LICENSE). Utilise-le et modifie-le comme tu veux.
