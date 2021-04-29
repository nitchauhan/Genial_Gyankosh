$(document).ready(function() {
//toastr.info('Page Loaded!');
    load_chart();
    load_chart_pie();
  });


function load_chart()
{
    var ctx = document.getElementById('myChart').getContext('2d');
    var data_barchart_label = document.getElementById('bar_chart_label');
    var data_barchart_count = document.getElementById('bar_chart_count');
    data_barchart_label.value = data_barchart_label.value.replace(/'/g, '');
    data_barchart_label.value = data_barchart_label.value.replace('[', '');
    data_barchart_label.value = data_barchart_label.value.replace(']', '');
    var arr = data_barchart_label.value.split(',');
//    var arr = JSON.parse("[" + data_barchart_label.value + "]")

    var arr_count = JSON.parse("[" + data_barchart_count.value + "]");

    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'bar',

        // The data for our dataset
        data: {
                labels: arr,
//            labels: arr,
            datasets: [{
//                label: 'My First dataset',
                    backgroundColor: ["#0074D9", "#FF4136", "#2ECC40", "#FF851B", "#7FDBFF", "#B10DC9", "#FFDC00", "#001f3f", "#39CCCC", "#01FF70", "#85144b", "#F012BE", "#3D9970", "#111111", "#AAAAAA"],
//                borderColor: 'rgb(255, 99, 132)',
                data: arr_count[0]
            }]
        },

        // Configuration options go here
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
}

function load_chart_pie()
{
    var ctx = document.getElementById('myChart_pie').getContext('2d');
    var data_barchart_label = document.getElementById('pie_chart_label');
    var data_barchart_count = document.getElementById('pie_chart_count');
    data_barchart_label.value = data_barchart_label.value.replace(/'/g, '');
    data_barchart_label.value = data_barchart_label.value.replace('[', '');
    data_barchart_label.value = data_barchart_label.value.replace(']', '');
    var arr = data_barchart_label.value.split(',');
//    var arr = JSON.parse("[" + data_barchart_label.value + "]")

    console.log(data_barchart_count.value);
    var arr_count = JSON.parse("[" + data_barchart_count.value + "]");

    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'doughnut',

        // The data for our dataset
        data: {
            labels: arr,
            datasets: [{
//                label: 'My First dataset',
backgroundColor: ["#0074D9", "#FF4136", "#2ECC40", "#FF851B", "#7FDBFF", "#B10DC9", "#FFDC00", "#001f3f", "#39CCCC", "#01FF70", "#85144b", "#F012BE", "#3D9970", "#111111", "#AAAAAA"],
//                borderColor: 'rgb(255, 99, 132)',
                data: arr_count[0]
            }]
        },

        // Configuration options go here
        options: {}
    });
}