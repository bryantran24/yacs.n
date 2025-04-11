<script setup lang="ts">
import { RouterLink, useRoute } from "vue-router/auto";
import { computed, ref } from 'vue'
import { useClassInfoStore } from "@/stores/classinfo";
import CourseModal from "@/components/modals/CourseModal.vue";
import { storeToRefs } from "pinia";
import type { Course } from "@/types/course";

const { current_courses } = storeToRefs(useClassInfoStore());

const route = useRoute();
const currentDepartment = computed(() => route.params.major as string);

const selectedCourse = ref<Course | null>(null);
const isModalOpen = ref(false);

const filteredCourses = computed(() => {
  if (!current_courses.value) return [];
  return current_courses.value.filter(course => course.department === currentDepartment.value);
});

function showCourse(course: Course) {
  selectedCourse.value = course;
  isModalOpen.value = true;
}

function closeModal() {
  isModalOpen.value = false;
  selectedCourse.value = null;
}

function getNumSections(course : Course) {
  let num_sections = 0;
  for (const section of course.sections) {
    if (section.seats_open == section.seats_total) {
      num_sections++;
    }
  }
  if (num_sections == course.sections.length) {
    return "All Sections full";
  }
  else {
    return `${num_sections}/${course.sections.length} Sections Open`;
  }
}

function numSectionsFull(course: Course) {
  let num_sections = 0;
  for (const section of course.sections) {
    if (section.seats_open == section.seats_total) {
      num_sections++;
    }
  }
  return num_sections == course.sections.length;
}

</script>

<template>
  <div>
    <RouterLink to="/explore">
      <h2 class="cursor-pointer text-blue-600 hover:underline bg-on-primary-dark inline-block px-2 rounded-b-md ml-2 mb-2">
        ← All Departments
      </h2>
    </RouterLink>

    <div v-if="filteredCourses.length > 0" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 px-10 pt-1 sm:pt-4">
      <div 
        v-for="course in filteredCourses"
        :key="course.title"
      >
        <button
          class="border border-gray-300 rounded hover:bg-green-600 transition-colors duration-200 
            hover:text-white text-500 hover:underline text-center w-full p-4"
          @click="showCourse(course)"
        >
          {{ course.title }} <br />
          {{ course.department }} - {{ course.level }}
          <span 
            class="inline-block rounded px-2 py-1 text-xs font-semibold text-white no-underline ml-2"
            :class="numSectionsFull(course) ? 'bg-red-500' : 'bg-green-500'"
          >
            {{ getNumSections(course) }}
          </span>
        </button>
      </div>
    </div>
  </div>

  <CourseModal
    v-if="selectedCourse"
    :course="selectedCourse"
    :open="isModalOpen"
    @close="closeModal"
  />
</template>
