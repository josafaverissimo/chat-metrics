<script setup lang="ts"></script>

<template>
  <div class="sheetWrapper">
    <div class="sheetWrapper__content">
      <slot/>
    </div>
  </div>
</template>

<style scoped>
.sheetWrapper {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;

  .sheetWrapper__content {
    width: 90%;
  }
}
</style>