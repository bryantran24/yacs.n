<script setup lang="ts">
import { computed, onMounted } from 'vue'
import { RouterLink, useRoute } from 'vue-router/auto'
import { useClassInfoStore } from "@/stores/classinfo";
import { storeToRefs } from "pinia";

const { departments } = storeToRefs(useClassInfoStore());
const route = useRoute()
const showDepartments = computed(() => !route.params.major)

const json = {
  "schools": [
    {
      "longname": "Humanities, Arts and Social Sciences",
      "subjects": [
        { "shortname": "ARTS", "longname": "Arts" },
        { "shortname": "COGS", "longname": "Cognitive Science" },
        { "shortname": "STSH", "longname": "Science and Technology Studies - Humanities" },
        { "shortname": "STSS", "longname": "Science and Technology Studies - Social Sciences" },
        { "shortname": "COMM", "longname": "Communication" },
        { "shortname": "ECON", "longname": "Economics" },
        { "shortname": "GSAS", "longname": "Games and Simulations Arts and Sciences" },
        { "shortname": "IHSS", "longname": "Interdisciplinary H&SS" },
        { "shortname": "LANG", "longname": "Languages" },
        { "shortname": "LITR", "longname": "Literature" },
        { "shortname": "PHIL", "longname": "Philosophy" },
        { "shortname": "PSYC", "longname": "Psychology" },
        { "shortname": "WRIT", "longname": "Writing" }
      ]
    },
    {
      "longname": "Engineering",
      "subjects": [
        { "shortname": "BMED", "longname": "Biomedical Engineering" },
        { "shortname": "CHME", "longname": "Chemical Engineering" },
        { "shortname": "ECSE", "longname": "Electrical and Computer Systems Engineering" },
        { "shortname": "ENVE", "longname": "Environmental and Energy Engineering" },
        { "shortname": "MANE", "longname": "Mechanical, Aerospace, and Nuclear Engineering" },
        { "shortname": "MTLE", "longname": "Materials Science and Engineering" },
        { "shortname": "CIVL", "longname": "Civil Engineering" },
        { "shortname": "ENGR", "longname": "Core Engineering" },
        { "shortname": "ISYE", "longname": "Industrial and Systems Engineering" },
        { "shortname": "EPOW", "longname": "Electric Power Engineering" }
      ]
    },
    {
      "longname": "Science",
      "subjects": [
        { "shortname": "BCBP", "longname": "Biochemistry and Biophysics" },
        { "shortname": "CSCI", "longname": "Computer Science" },
        { "shortname": "ERTH", "longname": "Earth and Environmental Science" },
        { "shortname": "IENV", "longname": "Interdisciplinary Environmental" },
        { "shortname": "ISCI", "longname": "Interdisciplinary Science" },
        { "shortname": "MATP", "longname": "Math Programming, Probability, and Statistics" },
        { "shortname": "PHYS", "longname": "Physics" },
        { "shortname": "ASTR", "longname": "Astronomy" },
        { "shortname": "BIOL", "longname": "Biology" },
        { "shortname": "CHEM", "longname": "Chemistry" },
        { "shortname": "MATH", "longname": "Mathematics" },
        { "shortname": "ITWS", "longname": "Information Technology and Web Science" }
      ]
    },
    {
      "longname": "Architecture",
      "subjects": [
        { "shortname": "ARCH", "longname": "Architecture" },
        { "shortname": "LGHT", "longname": "Lighting" }
      ]
    },
    {
      "longname": "Business Management",
      "subjects": [
        { "shortname": "MGMT", "longname": "Management" }
      ]
    },
    {
      "longname": "Other",
      "subjects": [
        { "shortname": "ADMN", "longname": "Administrative Courses" },
        { "shortname": "USAF", "longname": "Aerospace Studies (Air Force ROTC)" },
        { "shortname": "USNA", "longname": "Naval Science (Navy ROTC)" },
        { "shortname": "USAR", "longname": "Military Science (Army ROTC)" }
      ]
    }
  ]
}

const schoolMap = computed(() => {
  const map = new Map<string, [string, string][]>();

  json.schools.forEach(school => {
    const subjectsTuples: [string, string][] = school.subjects.map(subject => [subject.shortname, subject.longname]);
    map.set(school.longname, subjectsTuples);
  });

  return map;
});


onMounted(() => {
  console.log(schoolMap);
});
</script>

<template>
  <div 
    v-if="showDepartments && departments"
    class = "columns-2"
  >
    <div 
      v-for="([school, subjects]) in Array.from(schoolMap.entries())" 
      :key="school" 
      class="break-inside-avoid border border-black"
    >
      <h3 class="font-bold">{{ school }}</h3>
      <div 
        v-for="([shortname, longname]) in subjects" 
        :key="shortname"
      >
        <RouterLink
          v-if="departments.some(d => d.department === shortname)"
          :to="`/explore/${shortname}`"
          class="text-primary rounded-sm p-1"
        >
          {{ shortname }} - {{ longname }}
        </RouterLink>
      </div>
    </div>
  </div>
  <RouterView />
</template>
