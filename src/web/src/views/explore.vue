<script setup lang="ts">
import { computed } from 'vue'
import { RouterLink, useRoute } from 'vue-router/auto'
import { useClassInfoStore } from "@/stores/classinfo";
import { storeToRefs } from "pinia";

const { departments } = storeToRefs(useClassInfoStore());
const route = useRoute()
const showDepartments = computed(() => !route.params.major)

</script>

<template>
  <div>
    <div v-if="showDepartments && departments" class="grid grid-cols-3 gap-4">
      <RouterLink
        v-for="major in departments"
        :key="major.department"
        :to="`/explore/${major.department}`"
        class="text-primary rounded-sm p-1"
      >
        {{ major.department }}
      </RouterLink>
    </div>
  </div>
  <RouterView />
</template>
