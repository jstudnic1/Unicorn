let vlak = {
    lokomotiva: "parni",
    postovniVagon: "pošta",
    teloVlaku: [
        { typ: "kupe", capacity: 15 },
        { typ: "druha trida", capacity: 15 },
        { typ: "jidelni vuz", capacity: 15 }
    ]
};

console.log("vlak", vlak);

if (vlak.teloVlaku && vlak.teloVlaku.lenght > 0) {
} else {
    console.log("vlak nejede")

    var pocetVagonu;
switch (vlak.teloVlaku.length) {


        case 1:
            pocetVagonu = "jeden";
            break;
        case 2:
            pocetVagonu = "Dva";
            break;
        case 3:
            pocetVagonu = "tři";
            break;
        default:
            pocetVagonu = "moc";
            break;
    }
    console.log("Vlak má " + pocetVagonu + "vagonu pro osoby.");

    var kapacita = 0;

    for (let index = 0; index < vlak.teloVlaku.length; index++) {
        kapacita += vlak.teloVlaku[index].typ === "Jidelni vagon" ? 0 : vlak.teloVlaku[index].capacity;
    }

    console.log("kapacita vlaku je" + kapacita+ "osob")

    console.log(vlak.lokomotiva);
    if (vlak.postovniVagon) {
        console.log(" - ");
        console.log("postovni vagon");
    }

    let vagon = 0;
    while (vagon < vlak.teloVlaku.length) {
        console.log(" - ");

        let sedadel = vlak.teloVlaku[vagon].capacity;
        let rada = "";
        do {
            rada += "h";
            sedadel --;
        } while(sedadel > 0)
        
        console.log(vlak.teloVlaku[vagon].typ);
        vagon ++;
    }
}
