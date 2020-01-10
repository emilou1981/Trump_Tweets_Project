document.addEventListener('DOMContentLoaded', (event) => {

function initViz() {
    var containerDiv = document.getElementById("vizContainer"),
    url = "https://public.tableau.com/profile/areerat.kichkha#!/vizhome/FinancialImpacts/Sheet1";

    var viz = new tableau.Viz(containerDiv, url);
}

initViz();
});