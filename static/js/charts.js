


var assets_parsed = JSON.parse(assets_json);
var ndx = crossfilter(assets_parsed);
var type_dim = ndx.dimension(dc.pluck('Type'))
var all = ndx.groupAll().reduceSum(dc.pluck('MEC_MW'));
var total_mec_per_type = type_dim.group().reduceSum(dc.pluck('MEC_MW'));
dc.pieChart('#per-type-chart')
    .dimension(type_dim)
    .group(total_mec_per_type)
    .title(function (d) {
        return d.key + ':\n' + Math.round(d.value / all.value() * 100) + '%\n' + Math.round(d.value) + 'MW';
    });

var county_dim = ndx.dimension(dc.pluck('County'))
var total_mec_per_county = county_dim.group().reduceSum(dc.pluck('MEC_MW'));

dc.pieChart('#per-county-chart')
    .dimension(county_dim)
    .group(total_mec_per_county)
    .title(function (d) {
        return d.key + ':\n' + Math.round(d.value / all.value() * 100) + '%\n' + Math.round(d.value) + 'MW';
    });
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
    .title(function (d) {
        return d.key + ':\n' + Math.round(d.value / all.value() * 100) + '%\n' + Math.round(d.value) + 'MW';
    })
    .margins().left = 55
dc.renderAll();

