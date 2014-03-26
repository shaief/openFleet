
// var margin = {top: 40, right: 20, bottom: 60, left: 40},
//     width = 400 - margin.left - margin.right,
//     height = 300 - margin.top - margin.bottom;

var x = d3.scale.ordinal()
    .rangeRoundBands([0, width], .5);

var y = d3.scale.linear()
    .range([height, 0]);

var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

var yAxis = d3.svg.axis()
    .scale(y)
    .orient("left")
    // .tickFormat(formatPercent);

var tip = d3.tip()
  .attr('class', 'd3-tip')
  .offset([-10, 0])
  .html(function(d) {
    return ("<strong>License ID:</strong> <span style='color:blue'>" + d.car + "</span><br><strong>Liters per month:</strong> <span style='color:red'>" + d.liter_per_month + "</span>");
  })

var svg = d3.select("#chart").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

svg.call(tip);

d3.json(classification, function(error, json) {
  var data = json;
  console.log(data);
  x.domain(data.map(function(d) { return d.car; }));
  y.domain([0, d3.max(data, function(d) { return d.liter_per_month; })]);

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis)
      .selectAll("text")  
            .style("text-anchor", "end")
            .attr("dx", "6em")
            .attr("dy", "-.5em")
            .attr("transform", function(d) {
                return "rotate(90)" 
                });

  svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Liters per month");

  bars = svg.selectAll(".bar")
    .data(data)
    .enter().append("rect")
      .attr("class", "bar")
      .attr("x", function(d) { return x(d.car); })
      .attr("width", x.rangeBand())
      .attr("y", function(d) { return y(d.liter_per_month); })
      .attr("height", function(d) { return height - y(d.liter_per_month); })
      .on('mouseover', tip.show)
      .on('mouseout', tip.hide)

  d3.selectAll("input")
      .on("change", change);

    var timeout = setTimeout(function() {
    d3.select("input[value=\"nis_per_km\"]").property("checked", true).each(change);
  }, 2000);

  function change() {
    var value = this.value;
    clearTimeout(timeout);
    bars.value(function(d) { return d[value]; }); // change the value function
    path = path.data(bars); // compute the new angles
    path.transition().duration(750).attrTween("d", arcTween); // redraw the arcs
  }
});


d3.select('input').on('change', function() {

    var sortByMax = function(a, b) { return a.liter_per_month - b.liter_per_month; };
    // var sortByCar = function(a, b) { return b.carID - a.carID; };
    var sortByCar = function(a, b) { return d3.ascending(a.carID, b.carID); };
    var sortedCars = data.sort(this.checked ? sortByMax : sortByCar)
                      .map(function(d) { return d.car; })
    x.domain(sortedCars)

    var transition = svg.transition().duration(750);
    var delay = function(d, i) { return i * 50; };

    // console.log("changed");

    transition.selectAll(".bar")
        .delay(delay)
        .attr("x", function(d) { return x(d.car); });

    transition.select(".x.axis")
      .call(xAxis)
      .selectAll("g")
      .delay(delay);

 })

});

function type(d) {
  d.liter_per_month = +d.liter_per_month;
  return d;
}
