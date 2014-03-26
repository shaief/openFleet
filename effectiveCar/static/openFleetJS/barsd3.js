
// var margin = {top: 40, right: 20, bottom: 30, left: 40},
// width = 960 - margin.left - margin.right,
// height = 500 - margin.top - margin.bottom;

var x = d3.scale.ordinal()
.rangeRoundBands([0, width], .1);

var y = d3.scale.linear()
.range([height, 0]);

var xAxis = d3.svg.axis()
.scale(x)
.orient("bottom");

var yAxis = d3.svg.axis()
.scale(y)
.orient("left")

    var tip = d3.tip()
    .attr('class', 'd3-tip')
    .offset([-10, 0])
    .html(function(d) {
      return "<strong>Liters per month:</strong> <span style='color:red'>" + d.liter_per_month + "</span>";
    })

    var DELAY = 500;
    var DURATION = 750;

    var chartTitle = d3.selectAll("#ChartTitle").append("h1").html("NIS per km: ");

    var svg = d3.select(".chart1").append("svg")
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
      .call(xAxis);

      svg.append("g")
      .attr("class", "y axis")
      .call(yAxis)
    // .append("text")
    //   .attr("transform", "rotate(-90)")
    //   .attr("y", 6)
    //   .attr("dy", ".71em")
    //   .style("text-anchor", "end")
    //   .text("Liters per month");

    var YAXIS = svg.select(".y.axis")

    var bars = svg.selectAll(".bar")
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

    bars.transition()
    .delay(500)
    .duration(DURATION)
    .attr("class", "bar")
    .attr("x", function(d) { return x(d.car); })
    .attr("width", x.rangeBand())
    .attr("y", function(d) { return y(d.nis_per_km); })
    .attr("height", function(d) { return height - y(d.nis_per_km); })
    .ease("back")
    
    var nis_per_kmButton = d3.select("input#nis_per_km")
    // .property("checked", "true")
    .on('change', function(){
      console.log("nis_per_kmButton changed");

      chartTitle.transition()
      .text("NIS per km: ");

      tip.html(function(d) {
        return "<strong>NIS per km</strong> <span style='color:red'>" + d.nis_per_km + "</span>";
      })

      y.domain([0, d3.max(data, function(d) { return d.nis_per_km; })]);

      bars.transition()
      .delay(DELAY)
      .duration(DURATION)
      .attr("class", "bar")
      .attr("x", function(d) { return x(d.car); })
      .attr("width", x.rangeBand())
      .attr("y", function(d) { return y(d.nis_per_km); })
      .attr("height", function(d) { return height - y(d.nis_per_km); })
      .ease("back");

      bars.on('mouseover', tip.show)
      .on('mouseout', tip.hide);

      YAXIS.transition()
      .call(yAxis)
      .selectAll("g")
      .delay(DURATION);

      d3.select('input#sort').on('change', function() {
        var sortByMax = function(a, b) { return a.nis_per_km - b.nis_per_km; };
    // var sortByCar = function(a, b) { return b.carID - a.carID; };
    var sortByCar = function(a, b) { return d3.ascending(a.carID, b.carID); };
    var sortedCars = data.sort(this.checked ? sortByMax : sortByCar)
    .map(function(d) { return d.car; })
    x.domain(sortedCars)

    var transition = svg.transition().duration(DURATION);
    var delay = function(d, i) { return i * 50; };
    console.log("pressed")

    transition.selectAll(".bar")
    .delay(delay)
    .attr("x", function(d) { return x(d.car); });

    transition.select(".x.axis")
    .call(xAxis)
    .selectAll("g")
    .delay(delay);
  })
      svg.call(tip);

    });

var kmButton = d3.select("input#km")
// .property("checked", "false")
.on('change', function(){
  console.log("kmButton changed");

  chartTitle.transition()
  .text("km per month: ");

  tip.html(function(d) {
    return "<strong>km per month: </strong> <span style='color:red'>" + d.km_per_month + "</span>";
  })

  y.domain([0, d3.max(data, function(d) { return d.km_per_month; })]);

  bars.transition()
  .delay(DELAY)
  .duration(DURATION)
  .attr("class", "bar")
  .attr("x", function(d) { return x(d.car); })
  .attr("width", x.rangeBand())
  .attr("y", function(d) { return y(d.km_per_month); })
  .attr("height", function(d) { return height - y(d.km_per_month); })
  .ease("back");

  bars.on('mouseover', tip.show)
  .on('mouseout', tip.hide);

  YAXIS.transition()
  .call(yAxis)
  .selectAll("g")
  .delay(DURATION);

  var transition = svg.transition().duration(DURATION);
  var delay = function(d, i) { return i * 50; };
  console.log("pressed")

  transition.select(".y.axis")
  .call(yAxis)
  .selectAll("g")
  .delay(delay);

  d3.select('input#sort').on('change', function() {
    var sortByMax = function(a, b) { return a.km_per_month - b.km_per_month; };
    var sortByCar = function(a, b) { return d3.ascending(a.carID, b.carID); };
    var sortedCars = data.sort(this.checked ? sortByMax : sortByCar)
    .map(function(d) { return d.car; })
    x.domain(sortedCars)

    var transition = svg.transition().duration(DURATION);
    var delay = function(d, i) { return i * 50; };
    console.log("pressed")

    transition.selectAll(".bar")
    .delay(delay)
    .attr("x", function(d) { return x(d.car); });

    transition.select(".x.axis")
    .call(xAxis)
    .selectAll("g")
    .delay(delay);
  })
});

var litersButton = d3.select("input#liters")
//.property("checked", "false")
.on('change', function(){
  console.log("litersButton changed");

  chartTitle.transition()
  .text("Liters per month: ");

  tip.html(function(d) {
    return "<strong>Liters per month: </strong> <span style='color:red'>" + d.liter_per_month + "</span>";
  })

  y.domain([0, d3.max(data, function(d) { return d.liter_per_month; })]);
  var transition = svg.transition().duration(DURATION);
  var delay = function(d, i) { return i * 50; };
  console.log("pressed")

  transition.select(".y.axis")
  .call(yAxis)
  .selectAll("g")
  .delay(delay);

  bars.transition()
  .delay(DELAY)
  .duration(DURATION)
  // .enter().append("rect")
  .attr("class", "bar")
  .attr("x", function(d) { return x(d.car); })
  .attr("width", x.rangeBand())
  .attr("y", function(d) { return y(d.liter_per_month); })
  .attr("height", function(d) { return height - y(d.liter_per_month); })
  .ease("back");

  bars.on('mouseover', tip.show)
  .on('mouseout', tip.hide);

  YAXIS.transition()
  .call(yAxis)
  .selectAll("g")
  .delay(DURATION);

  d3.select('input#sort').on('change', function() {
    var sortByMax = function(a, b) { return a.liter_per_month - b.liter_per_month; };
    // var sortByCar = function(a, b) { return b.carID - a.carID; };
    var sortByCar = function(a, b) { return d3.ascending(a.carID, b.carID); };
    var sortedCars = data.sort(this.checked ? sortByMax : sortByCar)
    .map(function(d) { return d.car; })
    x.domain(sortedCars)

    var transition = svg.transition().duration(DURATION);
    var delay = function(d, i) { return i * 50; };
    console.log("pressed")
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


var costButton = d3.select("input#cost")
//.property("checked", "false")
.on('change', function(){
  console.log("costButton changed");

  chartTitle.transition()
  .text("Cost per month: ");

  tip.html(function(d) {
    return "<strong>Cost per month: </strong> <span style='color:red'>" + d.cost_per_month + "</span>";
  })

  y.domain([0, d3.max(data, function(d) { return d.cost_per_month; })]);
  var transition = svg.transition().duration(DURATION);
  var delay = function(d, i) { return i * 50; };
  console.log("pressed")

  transition.select(".y.axis")
  .call(yAxis)
  .selectAll("g")
  .delay(delay);

  bars.transition()
  .delay(DELAY)
  .duration(DURATION)
  // .enter().append("rect")
  .attr("class", "bar")
  .attr("x", function(d) { return x(d.car); })
  .attr("width", x.rangeBand())
  .attr("y", function(d) { return y(d.cost_per_month); })
  .attr("height", function(d) { return height - y(d.cost_per_month); })
  .ease("back");

  bars.on('mouseover', tip.show)
  .on('mouseout', tip.hide);

  YAXIS.transition()
  .call(yAxis)
  .selectAll("g")
  .delay(DURATION);

  d3.select('input#sort').on('change', function() {
    var sortByMax = function(a, b) { return a.cost_per_month - b.cost_per_month; };
    // var sortByCar = function(a, b) { return b.carID - a.carID; };
    var sortByCar = function(a, b) { return d3.ascending(a.carID, b.carID); };
    var sortedCars = data.sort(this.checked ? sortByMax : sortByCar)
    .map(function(d) { return d.car; })
    x.domain(sortedCars)

    var transition = svg.transition().duration(DURATION);
    var delay = function(d, i) { return i * 50; };
    console.log("pressed")
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

});

function type(d) {
  d.liter_per_month = +d.liter_per_month;
  return d;
}
