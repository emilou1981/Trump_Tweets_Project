function daily() {
    var containerDiv = document.getElementById("sent-1"),
    url = "https://public.tableau.com/views/Tweets_15783615078300/Sheet2?:retry=yes&:display_count=y&:origin=viz_share_link";
  
    var viz = new tableau.Viz(containerDiv, url);
  }
  
  function time() {
    var containerDiv = document.getElementById("sent-2"),
    url = "https://public.tableau.com/views/Tweets_15783615078300/Sheet4?:display_count=y&:origin=viz_share_link";
  
    var viz = new tableau.Viz(containerDiv, url);
  }
  
  function favRet() {
    var containerDiv = document.getElementById("sent-3"),
    url = "https://public.tableau.com/views/Tweets_15783615078300/Sheet5?:retry=yes&:display_count=y&:origin=viz_share_link";
  
    var viz = new tableau.Viz(containerDiv, url);
  }
  
  daily();
  
  time();
  
  favRet();