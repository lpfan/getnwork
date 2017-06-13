<template>
  <div id="app">
      <app-header></app-header>
      <app-footer></app-footer>
  </div>
</template>

<script>
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';

export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  components: {
    appHeader: Header,
    appFooter: Footer
  }
}
</script>

<style lang="scss">
  @import '~bulma/bulma.sass';
</style>
