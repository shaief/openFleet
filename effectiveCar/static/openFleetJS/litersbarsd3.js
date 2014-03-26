
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

var litersSvg = d3.select("#literschart").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

litersSvg.call(tip);

d3.json(classification, function(error, json) {
  var data = json;
  console.log(data);
  x.domain(data.map(function(d) { return d.car; }));
  y.domain([0, d3.max(data, function(d) { return d.liter_per_month; })]);

  litersSvg.append("g")
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

  litersSvg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Liters per month");

  litersSvg.selectAll(".bar")
    .data(data)
    .enter()
    .append("a")
    .attr("xlink:href", function(d){return d.url;})
    .append("rect")
      .attr("class", "bar")
      .attr("x", function(d) { return x(d.car); })
      .attr("width", x.rangeBand())
      .attr("y", function(d) { return y(d.liter_per_month); })
      .attr("height", function(d) { return height - y(d.liter_per_month); })
      .on('mouseover', tip.show)
      .on('mouseout', tip.hide)

d3.select('input').on('change', function() {

    var sortByMax = function(a, b) { return a.liter_per_month - b.liter_per_month; };
    // var sortByCar = function(a, b) { return b.carID - a.carID; };
    var sortByCar = function(a, b) { return d3.ascending(a.carID, b.carID); };
    var sortedCars = data.sort(this.checked ? sortByMax : sortByCar)
                      .map(function(d) { return d.car; })
    x.domain(sortedCars)

    var transition = litersSvg.transition().duration(750);
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
