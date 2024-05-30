<script setup lang="ts">
import { computed, defineAsyncComponent } from 'vue'
import DiceIcon from "@/components/icons/DiceIcon.vue";

const props = withDefaults(
    defineProps<{
      name: string,
      size?: number
    }>(), {
      size: 3
    }
)

const iconComponent = computed(() =>
  defineAsyncComponent(() => import(`@/components/icons/${props.name}Icon.vue`))
)

const iconStyles = {
  height: `${props.size}rem`
}
</script>

<template>
  <component :is="iconComponent" :style="iconStyles"/>
</template>

<style scoped></style>