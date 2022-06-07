<template>
  <SideBar :key-data="keyData" @update-index="(i) => getDataBackend(i)" :selectedIndex="selectedIndex" />
  <ChartView :chartData="chartData" />
</template>

<script>
import axios from 'axios';
import SideBar from './components/SideBar.vue';
import ChartView from './components/ChartView.vue';


export default {
  name: 'BarChart',
  components: { SideBar, ChartView },
  data() {
    return {
      chartData: {
        labels: [],
        datasets: [],
      },
      keyData: [],
      allData: [],
      selectedIndex: 0
    }
  },
  mounted() {
    axios
      .get('http://localhost:8000/')
      .then(response => {
        console.log(response.data)
        this.allData = response.data;
        this.keyData = response.data.finalData
        this.chartData.labels = response.data.label[0];
        this.chartData.datasets = [{
          label: 'World Development Indicators (in %)',
          backgroundColor: 'rgb(9, 113, 241)',
          data: response.data.finalData[0][1],
          hoverBackgroundColor: 'rgba(29,191,115)'


        }]
      })
  },
  methods: {
    getDataBackend(index) {
      this.chartData.datasets = [{
        label: 'World Development Indicators', backgroundColor: 'rgb(9 113 241)',
        data: this.allData.finalData[index][1],
        hoverBackgroundColor: 'rgba(29,191,115)'
      }]
      this.selectedIndex = index
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  align-items: center;
}
</style>
