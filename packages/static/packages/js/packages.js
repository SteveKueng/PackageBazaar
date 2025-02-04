document.addEventListener("DOMContentLoaded", function() {
    // Ersten Tab aktiv setzen
    let defaultTab = document.querySelector(".tablinks");
    if (defaultTab) {
        defaultTab.click();
    }

    // Event-Listener für die Suchfunktion
    document.getElementById("searchInput").addEventListener("keyup", filterPackages);
});

function openTab(evt, catalogName) {
    let tabcontent = document.getElementsByClassName("tabcontent");
    let tablinks = document.getElementsByClassName("tablinks");

    // Verstecke alle Tab-Inhalte
    for (let i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Entferne die aktive Klasse von allen Tabs
    for (let i = 0; i < tablinks.length; i++) {
        tablinks[i].classList.remove("bg-customYellow", "text-black");
    }

    // Aktuellen Tab anzeigen und aktiv setzen
    document.getElementById(catalogName).style.display = "block";
    evt.currentTarget.classList.add("bg-customYellow", "text-black");

    // Suche nach Tab-Wechsel erneut anwenden
    filterPackages();
}

function filterPackages() {
    let query = document.getElementById("searchInput").value.toLowerCase();
    let catalogs = document.getElementsByClassName("tabcontent");
    let activeTab = document.querySelector(".tablinks.bg-customYellow");

    if (!activeTab) return;

    let activeTabName = activeTab.textContent.trim();
    let activeCatalog = document.getElementById(activeTabName);

    if (!activeCatalog) return;

    let packageCards = activeCatalog.getElementsByClassName("package-card");
    let hasVisiblePackages = false;

    for (let card of packageCards) {
        let packageName = card.getAttribute("data-name").toLowerCase();
        let packageDesc = card.getAttribute("data-desc").toLowerCase();

        if (packageName.includes(query) || packageDesc.includes(query)) {
            card.style.display = "flex"; // Paket anzeigen
            hasVisiblePackages = true;
        } else {
            card.style.display = "none"; // Paket ausblenden
        }
    }

    // Zeigt oder versteckt den gesamten Tab, wenn keine passenden Pakete gefunden wurden
    activeCatalog.style.display = hasVisiblePackages ? "block" : "none";
}