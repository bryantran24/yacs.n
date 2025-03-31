<script setup lang="ts">
import { useRoute } from "vue-router/auto";
import { onMounted, computed } from 'vue'
import { useClassInfoStore } from "@/stores/classinfo";
import { storeToRefs } from "pinia";

const { current_courses } = storeToRefs(useClassInfoStore());

const currentDepartment = computed(() => useRoute().params.major as string);

onMounted(() => {
  try {
    console.log("Courses:", current_courses.value)
    console.log(filteredCourses.value)
  } catch (error) {
    console.error("Error fetching Courses:", error)
  }
})

const filteredCourses = computed(() => {
  if (!current_courses.value) return [];
  return current_courses.value.filter(course => course.department === currentDepartment.value);
});

function showCourse(prof: Professor) {
  selectedCourse.value = prof;
  isModalOpen.value = true;
}

function closeModal() {
  isModalOpen.value = false;
  selectedCourse.value = null;
}

function updateCourse(selectedOption: string | null) {
  selectedCourse.value = selectedOption;
}

</script>

<template>
  <div>
    <h2>Courses for Department: {{ currentDepartment }}</h2>
    <div v-if="filteredCourses.length > 0" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 px-10 pt-1 sm:pt-4">
      <div 
        v-for="course in filteredCourses"
        :key="course.title"
      >
        {{ course.title }} ({{ course.department }} - {{ course.level }})
      </div>
    </div>
  </div>
</template>
