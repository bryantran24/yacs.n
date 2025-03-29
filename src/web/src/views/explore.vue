<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import { RouterLink, useRoute } from 'vue-router/auto'
import { getDepartments } from '@/api/class'

interface Department {
  department: string
}

const departments = ref<Department[] | null>(null)

onMounted(async () => {
  try {
    departments.value = await getDepartments()
    console.log("Departments:", departments.value)
  } catch (error) {
    console.error("Error fetching departments:", error)
  }
})

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
    <div v-else-if="!departments">
      Loading departments...
    </div>
  </div>
  <RouterView />
</template>
