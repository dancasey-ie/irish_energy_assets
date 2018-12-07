


var assets_parsed = JSON.parse(assets_json);
var ndx = crossfilter(assets_parsed);

var type_dim = ndx.dimension(dc.pluck('Type'))
var total_mec_per_type = type_dim.group().reduceSum(dc.pluck('MEC_MW'));
dc.pieChart('#per-type-chart')
    .dimension(type_dim)
    .group(total_mec_per_type);

var county_dim = ndx.dimension(dc.pluck('County'))
var total_mec_per_county = county_dim.group().reduceSum(dc.pluck('MEC_MW'));
dc.pieChart('#per-county-chart')
    .dimension(county_dim)
    .group(total_mec_per_county)
var network_dim = ndx.dimension(dc.pluck('Status'));
var mecPerConnected = network_dim.group().reduceSum(function (d) {
    if (d.NetworkType === 'Transmission') {
        return +d.MEC_MW;
    } else {
        return 0;
    }
});
var mecPerContracted = network_dim.group().reduceSum(function (d) {
    if (d.NetworkType === 'Distribution') {
        return +d.MEC_MW;
    } else {
        return 0;
    }
});
var width = document.getElementById('per-status-stacked').getBoundingClientRect().width;
console.log(width)
var stackedChart = dc.barChart("#per-status-stacked");
stackedChart
    .dimension(network_dim)
    .group(mecPerConnected, "Transmission")
    .stack(mecPerContracted, "Distribution")
    .x(d3.scale.ordinal())
    .xUnits(dc.units.ordinal)
    .yAxisLabel("MEC (MW)")
    .width(280)
    .legend(dc.legend().x(50).y(188).itemHeight(15).gap(5).horizontal(true).itemWidth(100))
    .margins().left = 55;
dc.renderAll();


