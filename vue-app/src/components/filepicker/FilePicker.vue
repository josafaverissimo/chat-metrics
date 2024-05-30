<script setup lang="ts">
import { ref } from 'vue'

const emit = defineEmits<{
  (event: 'change', file: File): void
}>()

const fileInput = ref<HTMLInputElement>()
const file = ref<File>()

const changeHandler = () => {
  file.value = fileInput.value.files[0]

  change()
}

const clickHandler = () => {
  fileInput.value.click()
}

const dropHandler = (event: DragEvent) => {
  event.preventDefault()

  const validateItems = (items) => {
    return items.length == 1 && items[0].kind === 'file'
  }

  const itemsDropped = event.dataTransfer.items

  if(!validateItems(itemsDropped)) {
    return
  }

  file.value = itemsDropped[0].getAsFile()
  change()
}

const allowDragOver = (event: DragEvent) => {
  event.preventDefault()
}

const change = () => {
  if(!file.value) {
    return
  }

  emit('change', file.value)
}
</script>

<template>
  <div class="dropFileBoxWrapper">
    <div
      class="dropFileBox"
      @click="clickHandler"
      @drop="dropHandler"
      @dragover="allowDragOver"
    >
      <input type="file" hidden ref="fileInput" @change="changeHandler">
      <span>Selecione ou Solte um arquivo</span>
    </div>
  </div>
</template>

<style scoped>
.dropFileBoxWrapper {
  width: 100%;
  display: flex;
  justify-content: center;

  .dropFileBox {
    width: 50%;
    display: flex;
    justify-content: center;
    padding: 5rem 0;
    border: .5rem dashed #eee;
    border-radius: 1rem;
    cursor: pointer;

    span {
      font-size: 1.5rem;
      color: #555;
    }
  }
}
</style>