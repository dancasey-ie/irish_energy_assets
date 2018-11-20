queue()
    .defer(d3.json, 'static/data/json/assets.json')
    .await(makeGraphs);
function makeGraphs(error, assetsData) {
    var ndx = crossfilter(assetsData);

    var type_dim = ndx.dimension(dc.pluck('Type'))
    var total_mec_per_type = type_dim.group().reduceSum(dc.pluck('MEC_MW'));
    dc.pieChart('#per-type-chart')
        .height(330)
        .radius(100)
        .dimension(type_dim)
        .group(total_mec_per_type);

    var county_dim = ndx.dimension(dc.pluck('County'))
    var total_mec_per_county = county_dim.group().reduceSum(dc.pluck('MEC_MW'));
    dc.pieChart('#per-county-chart')
        .height(330)
        .radius(100)
        .dimension(county_dim)
        .group(total_mec_per_county);
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
        .width(500)
        .height(300)
        .dimension(network_dim)
        .group(mecPerConnected, "Transmission")
        .stack(mecPerContracted, "Distribution")
        .x(d3.scale.ordinal())
        .xUnits(dc.units.ordinal)
        .yAxisLabel("MEC (MW)")
        .legend(dc.legend().x(300).y(0).itemHeight(15).gap(5));
    stackedChart.margins().right = 100;
    dc.renderAll();
}