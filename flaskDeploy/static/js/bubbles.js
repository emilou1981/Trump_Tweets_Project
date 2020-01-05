
function wordcnt_create() {
  // Word BUBBLE CHART
  // // console.log(junkdataset)
  var diameter = 600;
  var color = d3.scaleOrdinal(d3.schemeCategory20);

  var tooltip = d3.select("body")
    .append("div")
    .style("position", "absolute")
    .style("z-index", "10")
    .style("visibility", "hidden")


  // Create array of objects of search results to be used by D3
  var data = [];
  d3.json("/api/wordcnt/", function (result) {
    result.forEach(function (i) {
      // console.log('foreach:' + i.word)   
      data.push({

        // cnt_word: i.cnt_word
        count: i.cnt_word,
        keyword: i.word
      });
    });
    // console.log(data);

    //convert numerical values from strings to numbers
    // data = data.map(function(d){ d.value = +d["count"]; return d; });
    // console.log(data)
    //bubbles needs very specific format, convert data to this.
    //var nodes = bubble.nodes({children:data}).filter(function(d) { return !d.children; }); 
    var dataset = {};
    dataset = {
      "children": data
    };
    // console.log(dataset)


    var bubble = d3.pack(dataset)
      .size([diameter, diameter])
      .padding(1.5);

    var svg = d3.select("#wordbubble_chart")
      .append("svg")
      .attr("width", diameter)
      .attr("height", diameter)
      .attr("class", "bubble");

    var nodes = d3.hierarchy(dataset)

      .sum(function (d) {
        // console.log('d.count:' + d.count)
        return d.count;
      });

    var node = svg.selectAll(".node")
      .data(bubble(nodes).descendants())
      .enter()
      .filter(function (d) {
        return !d.children
      })
      .append("g")
      .attr("class", "node")
      .attr("transform", function (d) {
        return "translate(" + d.x + "," + d.y + ")";
      });

    node.append("title")
      .text(function (d) {
        strTitle = d.data.keyword + ' : ' + d.data.count
        return strTitle;
      });

    circles = node.append("circle")
      // .on("mouseover", function(d){return tooltip.text(d.data.word).style("visibility", "visible");})
      .attr("r", function (d) {
        return d.r;
      })
      .style("fill", function (d, i) {
        return color(i);
      });
    circles
      .on('mouseover', function (d) {
        coordinates = d3.mouse(this);

        d3.select("#tooltip")
          .style("left", coordinates[0] + 10 + "px")
          .style("top", coordinates[1] + 10 + "px")
          // .select("#info")
          .text(d.word);

        d3.select("#tooltip").classed("hidden", false);
      })
      .on("mouseout", function () {
        d3.select("#tooltip").classed("hidden", true);
      })

    node.append("text")
      .attr("dy", ".2em")
      .style("text-anchor", "middle")
      .text(function (d) {
        return d.data.keyword;
      })
      .attr("font-family", "sans-serif")
      .attr("font-size", function (d) {
        return d.r / 5;
      })
      .attr("fill", "white");

    node.append("text")
      .attr("dy", "1.3em")
      .style("text-anchor", "middle")
      .text(function (d) {
        return d.data.count;
      })
      .attr("font-family", "Gill Sans", "Gill Sans MT")
      .attr("font-size", function (d) {
        return d.r / 5;
      })
      .attr("fill", "white");

    d3.select(self.frameElement)
      .style("height", diameter + "px");

  });
  return (true);
}

function phrasecnt_create() {
  // Phrase BUBBLE CHART
  // // console.log(junkdataset)
  var diameter = 600;
  var color = d3.scaleOrdinal(d3.schemeCategory20);

  var tooltip = d3.select("body")
    .append("div")
    .style("position", "absolute")
    .style("z-index", "10")
    .style("visibility", "hidden")


  // Create array of objects of search results to be used by D3
  var data = [];
  d3.json("/api/phrasecnt/", function (result) {
    result.forEach(function (i) {
      // console.log('foreach:' + i.word)   
      data.push({

        // cnt_word: i.cnt_word
        count: i.cnt_phrase,
        keyword: i.phrase
      });
    });
    // console.log(data);
    //  This is a change
    //convert numerical values from strings to numbers
    // data = data.map(function(d){ d.value = +d["count"]; return d; });
    // console.log(data)
    //bubbles needs very specific format, convert data to this.
    //var nodes = bubble.nodes({children:data}).filter(function(d) { return !d.children; }); 
    var dataset = {};
    dataset = {
      "children": data
    };
    // console.log(dataset)


    var bubble = d3.pack(dataset)
      .size([diameter, diameter])
      .padding(1.5);

    var svg = d3.select("#phrasebubble_chart")
      .append("svg")
      .attr("width", diameter)
      .attr("height", diameter)
      .attr("class", "bubble");

    var nodes = d3.hierarchy(dataset)

      .sum(function (d) {
        // console.log('d.count:' + d.count)
        return d.count;
      });

    var node = svg.selectAll(".node")
      .data(bubble(nodes).descendants())
      .enter()
      .filter(function (d) {
        return !d.children
      })
      .append("g")
      .attr("class", "node")
      .attr("transform", function (d) {
        return "translate(" + d.x + "," + d.y + ")";
      });

    node.append("title")
      .text(function (d) {
        strTitle = d.data.keyword + ' : ' + d.data.count
        return strTitle;
      });

    circles = node.append("circle")
      // .on("mouseover", function(d){return tooltip.text(d.data.word).style("visibility", "visible");})
      .attr("r", function (d) {
        return d.r;
      })
      .style("fill", function (d, i) {
        return color(i);
      });
    circles
      .on('mouseover', function (d) {
        coordinates = d3.mouse(this);

        d3.select("#tooltip")
          .style("left", coordinates[0] + 10 + "px")
          .style("top", coordinates[1] + 10 + "px")
          // .select("#info")
          .text(d.word);

        d3.select("#tooltip").classed("hidden", false);
      })
      .on("mouseout", function () {
        d3.select("#tooltip").classed("hidden", true);
      })

    node.append("text")
      .attr("dy", ".2em")
      .style("text-anchor", "middle")
      .text(function (d) {
        return d.data.keyword;
      })
      .attr("font-family", "sans-serif")
      .attr("font-size", function (d) {
        return d.r / 5;
      })
      .attr("fill", "white");

    node.append("text")
      .attr("dy", "1.3em")
      .style("text-anchor", "middle")
      .text(function (d) {
        return d.data.count;
      })
      .attr("font-family", "Gill Sans", "Gill Sans MT")
      .attr("font-size", function (d) {
        return d.r / 5;
      })
      .attr("fill", "white");

    d3.select(self.frameElement)
      .style("height", diameter + "px");

  });
  return (true);
}