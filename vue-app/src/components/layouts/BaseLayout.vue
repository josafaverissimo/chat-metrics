<script setup lang="ts"></script>

<template>
  <div>
    <p class="pageTitle"><slot name="title"/></p>

    <main>
      <slot name="content" />
    </main>
  </div>
</template>

<style scoped>
.pageTitle {
  font-size: 2rem;
}
</style>