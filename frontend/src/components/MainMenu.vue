<template>
<div>
    <nav class="nav is-mobile">
        <!-- This "nav-toggle" hamburger menu is only visible on mobile -->
        <!-- You need JavaScript to toggle the "is-active" class on "nav-menu" -->
        <span class="nav-toggle">
          <span></span>
          <span></span>
          <span></span>
        </span>

        <!-- This "nav-menu" is hidden on mobile -->
        <!-- Add the modifier "is-active" to display it on mobile -->
        <div class="nav-center nav-menu">
            <router-link :to="{ name: 'mainPage', params: {} }" class="nav-item" active-class="is-active">
                <span class="icon">
                  <i class="fa fa-home"></i>
                </span>
                Главная
            </router-link>
            <a class="nav-item">
              <span class="icon">
                <i class="fa fa-book"></i>
              </span>
              Обучающие материалы
            </a>
            <a class="nav-item">
              <span class="icon">
                <i class="fa fa-cubes"></i>
              </span>
              CAD* программы
            </a>
            <a class="nav-item">
              <span class="icon">
                <i class="fa fa-gavel"></i>
              </span>
              Инструмент
            </a>
            <a class="nav-item">
              <span class="icon">
                <i class="fa fa-info-circle"></i>
              </span>
              О проекте
            </a>

            <div class="nav-item">
                <div class="field is-grouped">
                  <!--
                    <p class="control">
                        <a class="button">
                            <span class="icon">
                              <i class="fa fa-twitter"></i>
                            </span>
                            <span>Tweet</span>
                        </a>
                    </p>
                  -->
                    <p class="control">
                        <a class="button is-primary">
                            <span class="icon">
                              <i class="fa fa-user-circle"></i>
                            </span>
                            <span>Вход</span>
                        </a>
                    </p>
                </div>
            </div>
        </div>
    </nav>
</div>
</template>

<script>
export default {
    data() {
        return {}
    },
    computed: {
        mainMenuItems() {
            return []
        }
    },
    beforeCreate() {
        console.log('beforecreate hook');
    },
    created() {
        console.log('created hook');
    }
}
</script>

<style lang="css">
</style>
