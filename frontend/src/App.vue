<template>
  <div id="app">
    <div class="container">
      <div class="row">
        <div class="col-xs-12">
          <app-header></app-header>
          <router-view></router-view>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Header from './components/Header.vue';

export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  components: {
    appHeader: Header
  }
}
</script>

<style>

</style>
