<script setup lang="ts">
import MainHeader from '@/components/header/MainHeader.vue'
import Sheet from "@/components/sheet/Sheet.vue";

</script>

<template>
  <div class="globalWrapper">
    <main-header />

    <sheet>
      <router-view />
    </sheet>
  </div>
</template>

<style scoped>
.globalWrapper {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}
</style>