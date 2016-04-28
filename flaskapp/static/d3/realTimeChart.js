function getDonut(data) {
    $('#dropdown-terms').highcharts({
        chart: {
            type: 'pie',
            options3d: {
                enabled: true,
                alpha: 45
            }
        },
        title: {
            text: 'Count of Disaster Keywords'
        },
        subtitle: {
            text: '3D Donut'
        },
        plotOptions: {
            pie: {
                innerSize: 100,
                depth: 45
            }
        },
        series: [{
            name: 'KeyWord Count',
            data: data
        }]
    });
};
