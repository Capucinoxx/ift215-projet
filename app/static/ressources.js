const data = {
  ressources_generales: [
    {
      nom: "Anciens Combattants Canada",
      description:
        "Cette ressource est réservée aux anciens combattants et à leur famille immédiate.",
      téléphone: "1 800 268-7708",
    },
    {
      nom: "LigneParents",
      téléphone: "1 800 361-5085",
      description:
        "Ce service d’intervention est confidentiel, gratuit et accessible jour et nuit.",
    },
    {
      nom: "Tel-jeunes",
      téléphone: "1 800 263-2266",
      description:
        "Ce service est destiné aux jeunes de 5 à 20 ans et offert par des professionnels. Il est confidentiel, gratuit et accessible jour et nuit.",
    },
    {
      nom: "Association des centres d’écoute téléphonique du Québec ",
      description: "Trouvez un centre d’écoute téléphonique dans votre région.",
      site_web:
        "https://www.lignedecoute.ca/centres-decoute-telephonique-par-region/",
    },
    {
      nom: "Centres de crise",
      description:
        "Regroupement des Services d’Intervention de Crise du Québec",
      site_web: "https://www.centredecrise.ca/",
    },
    {
      nom: "Relief ",
      description:
        "Association québécoise de soutien aux personnes souffrant de troubles anxieux, dépressifs ou bipolaires",
      site_web: "https://relief.ca/",
    },
    {
      nom: "Réseau Avant de craquer",
      description:
        "Fédération d’organismes voués au mieux-être de l’entourage d’une personne vivant avec un problème de santé mentale",
      site_web: "https://www.avantdecraquer.com/",
    },
    {
      nom: "Réseau d’entendeurs de voix du Québec ",
      description:
        "Ressource pour les personnes qui entendent des voix et celles qui les appuient",
      site_web: "https://www.aqrp-sm.org/entente-de-voix",
    },
  ],
};

function genererRessources(data) {
  let section = document.getElementById("pdv-flex");

  let innerHTML = "";
  for (let indice in data.ressources_generales) {
    let ressource = data.ressources_generales[indice];
    innerHTML +=
      "<li>" +
      "<h3>" +
      ressource.nom +
      "</h3>" +
      "<p>" +
      ressource.description +
      "</p>" +
      "<p>" +
      (ressource.téléphone || "") +
      "</p>" +
      "<p>" +
      (ressource.site_web
        ? `<a href="${ressource.site_web}" target="_blank">
          ${ressource.site_web}
        </a>`
        : "") +
      "</p>" +
      "</li>";
  }

  section.innerHTML = innerHTML;
}

genererRessources(data);
