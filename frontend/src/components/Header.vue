<template>
  <header>
    <div class="container clearfix">
      <h1 id="logo">
        Черчение вырезание
      </h1>
      <app-main-menu></app-main-menu>
    </div>
  </header>
</template>

<script>
import MainMenu from './MainMenu.vue';

export default {
  components: {
    appMainMenu: MainMenu
  }
}
</script>

<style lang="css">
</style>
