var data = [1, 2, 4, 8, 16, 8, 4, 2, 1]

var svg = d3.select("#d3-test").append('svg')
    .attr('width', 400)
    .attr('height', 200);

svg.selectAll('circle')
    .data(data)
    .enter()
    .append('circle')
    .attr("cx", function(d, i) {return 40 * (i + 1);})
    .attr("cy", function(d, i) {return 100 + 30 * (i % 3 - 1);})
    .style("fill", "#1570a4")
    .on("mouseover", mouseover)
    .transition().duration(2000)
    .attr("r", function(d) {return 2*d;})

function mouseover(dd) {

  d3.select(this)
    .transition()
      .style("fill", "red")
      .attr("r", function(d) {return 2.2*d;})
        .duration(200)
    .transition()
      .style("fill", "#1570a4")
      .attr("r", function(d) {return 2*d;})
      .duration(200)
}
