<script setup lang="ts">
import BaseLayout from "@/components/layouts/BaseLayout.vue";
import FilePicker from "@/components/filepicker/FilePicker.vue";

const fileChange = (file: File) => {
  console.log(file)
}
</script>

<template>
  <base-layout>
    <template v-slot:title>Banco de Dados</template>

    <template v-slot:content>
      <file-picker @change="fileChange" />
    </template>
  </base-layout>
</template>

<style scoped></style>