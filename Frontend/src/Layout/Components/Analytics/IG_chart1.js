//Importing Line class from the vue-chartjs wrapper
import {Line,mixins} from 'vue-chartjs'
const { reactiveProp } = mixins
//Exporting this so it can be used in other components
export default {
    extends: Line,
    data() {
        return {

            datacollection: {
                //Data to be represented on x-axis
                
                //labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',],
                labels : this.$store.state.IG_chart_labels,
                datasets: [
                    {
                        label: '내 포트폴리오',
                        // fill: true,
                        lineTension: 0.5,
                        borderColor: '#f7b924',
                        //borderCapStyle: 'round',
                        // borderDash: [],
                        // borderWidth: 4,
                        // borderDashOffset: 0.0,
                        // borderJoinStyle: 'round',
                        // pointBorderColor: '#f7b924',
                        // pointBackgroundColor: '#ffffff',
                        // pointBorderWidth: 5,
                        // pointHoverRadius: 6,
                        // pointHoverBackgroundColor: '#ffffff',
                        // pointHoverBorderColor: '#f7b924',
                        // pointHoverBorderWidth: 2,
                        // pointRadius: 4,
                        // pointHitRadius: 10,
                        //data: [65, 59, 80, 81, 46, 55, 38, 59, 80, 72]
                        data : this.$store.state.IG_chart_data2
                    },
                    {
                        label: '코스피 인덱스 추종',
                        // fill: true,
                        lineTension: 0.5,
                        borderColor: '#05CBE1',
                        //borderCapStyle: 'round',
                        borderDash: [],
                        // borderWidth: 4,
                        // borderDashOffset: 0.0,
                        // borderJoinStyle: 'round',
                        // pointBorderColor: '#f7b924',
                        // pointBackgroundColor: '#ffffff',
                        // pointBorderWidth: 5,
                        // pointHoverRadius: 6,
                        // pointHoverBackgroundColor: '#ffffff',
                        // pointHoverBorderColor: '#f7b924',
                        // pointHoverBorderWidth: 2,
                        // pointRadius: 4,
                        // pointHitRadius: 10,
                        //data: [65, 59, 80, 81, 46, 55, 38, 59, 80, 72]
                        data : this.$store.state.IG_chart_data1
                    }
                ]
            },
            //Chart.js options that controls the appearance of the chart
            options: {
                layout: {
                    padding: {
                        left: 0,
                        right: 8,
                        top: 0,
                        bottom: 0
                    }
                },
                scales: {
                    yAxes: [{
                        ticks: {
                            display: true,
                            beginAtZero: false
                        },
                        gridLines: {
                            display: false
                        }
                    }],
                    xAxes: [{
                        ticks: {
                            display: false
                        },
                        gridLines: {
                            display: false
                        }
                    }]
                },
                legend: {
                    display: false
                },
                responsive: true,
                maintainAspectRatio: true
            }
        }
    },
    async mounted() {
        //renderChart function renders the chart with the datacollection and options object.
        this.renderChart(this.datacollection, this.options)
    },
}