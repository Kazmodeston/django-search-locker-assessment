<template>
  <div>
    <!-- <home/> -->
    <router-view />
  </div>
</template>

<script>
import home from './components/home.vue'

export default {
  name: 'App',
  components: {
    home
  }
}
</script>
