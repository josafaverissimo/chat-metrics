<script setup lang="ts">
import Icon from '@/components/Icon.vue'

</script>

<template>
  <nav class="navbar">
    <ul class="navbar__linksWrapper">
      <li>
        <router-link to="/">
          <icon name="Home" />
        </router-link>
      </li>
      <li>
        <router-link to="database">
          <icon name="Dice" />
        </router-link>
      </li>
    </ul>
  </nav>
</template>

<style scoped>
.navbar {
  width: 50%;

  .navbar__linksWrapper {
    list-style: none;
    display: flex;
    justify-content: center;
    gap: 2rem;
    background: #eee;
    border-radius: 0 0 1rem 1rem;
  }
}
</style>