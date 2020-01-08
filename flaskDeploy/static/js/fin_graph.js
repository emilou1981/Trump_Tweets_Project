function gdpVStock() {
  var containerDiv = document.getElementById("vizContainer_large"),
  url = "https://public.tableau.com/views/GDPTweetsvsStockData/GDPTweetsvsStockData?:display_count=y&publish=yes&:origin=viz_share_link";

  var viz = new tableau.Viz(containerDiv, url);
}

function gdpVRgdp() {
  var containerDiv = document.getElementById("vizContainer_mid"),
  url = "https://public.tableau.com/views/GDPTeetsvsRGDPGrowth/GDPTweetsvsRGDPGrowth?:display_count=y&publish=yes&:origin=viz_share_link";

  var viz = new tableau.Viz(containerDiv, url);
}

function empVji() {
  var containerDiv = document.getElementById("vizContainer_small"),
  url = "https://public.tableau.com/views/EmploymentTweetsvsJobIncreases/EmploymentTweetsvsJobIncrease?:display_count=y&publish=yes&:origin=viz_share_link";

  var viz = new tableau.Viz(containerDiv, url);
}

gdpVStock();

gdpVRgdp();

empVji();
