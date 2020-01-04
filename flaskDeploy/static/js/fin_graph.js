function initVizLarge() {
  var containerDiv = document.getElementById("vizContainer_large"),
  url = "https://public.tableau.com/views/Large-CapStocks/Large-capStockPriceChangesEmploymentSituations?:display_count=y&:origin=viz_share_link";

  var viz = new tableau.Viz(containerDiv, url);
}

function initVizMid() {
  var containerDiv = document.getElementById("vizContainer_mid"),
  url = "https://public.tableau.com/views/Mid-capStocks/Mid-capStockPriceChangesandEmploymentSituations?:display_count=y&:origin=viz_share_link";

  var viz = new tableau.Viz(containerDiv, url);
}

function initVizSmall() {
  var containerDiv = document.getElementById("vizContainer_small"),
  url = "https://public.tableau.com/views/Small-CapStocks/Small-capStockPriceChangesEmploymentSituation?:display_count=y&:origin=viz_share_link";

  var viz = new tableau.Viz(containerDiv, url);
}

initVizLarge();

initVizMid();

initVizSmall();
