<script setup lang="ts">
import { defineProps, defineEmits } from "vue";
import GenericModal from "@/components/modals/GenericModal.vue";
import type { Course } from "@/types/course";

defineProps<{
  course: Course;
}>();

const emit = defineEmits<{
  close: [];
}>();

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
  <GenericModal 
    :open="true" 
    @close="emit('close')"
  >
    <template #default="{ close }">
      <div class="p-5 bg-on-primary-dark text-primary rounded shadow-lg">
        <h2 v-if="course.full_title" class="text-3xl font-bold mb-1">
          {{ course.full_title }}
        </h2>
        <h2 v-else class="text-3xl font-bold mb-1">
          {{ course.title }}
        </h2>
        <h3 class="mb-2">
          {{ course.name }}
          <span 
            class="inline-block rounded px-2 py-1 text-xs font-semibold text-white ml-2"
            :class="numSectionsFull(course) ? 'bg-red-500' : 'bg-green-500'">
            {{ getNumSections(course) }}
          </span>
        </h3>
        <p class="mb-2">
          <strong>Credits:</strong> {{ course.max_credits }}
        </p>
        <p v-if="course.description" class="mb-2">
          {{ course.description }}
        </p>
        <p v-if="course.frequency" class="mb-2">
          <strong>Frequency:</strong> {{ course.frequency.replace('When Offered:', '').trim() }}
        </p>
        <button
          class="mt-4 rounded bg-blue-500 px-4 py-2 text-white hover:bg-blue-600"
          @click="close()"
        >
          Close
        </button>
      </div>
    </template>
  </GenericModal>
</template>
