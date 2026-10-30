<script setup lang="ts">
// A numbered list of page cards (Roadmap look) for index pages: the cookbook recipes, the projects, the study skills.
import { computed } from 'vue'
import { withBase } from 'vitepress'
import course from '../course.json'

const props = defineProps<{ list: 'recipes' | 'skills' | 'projects' }>()
const items = computed(() => (course as any)[props.list] as { num: number; title: string; text: string; link: string }[])
</script>

<template>
  <ol class="cards">
    <li v-for="c in items" :key="c.link">
      <a class="cpf-card cpf-link item" :href="withBase(c.link)">
        <span class="cpf-num" aria-hidden="true">{{ c.num }}</span>
        <span><span class="title">{{ c.title }}</span><span class="text">{{ c.text }}</span></span>
      </a>
    </li>
  </ol>
</template>

<style scoped>
.cards { list-style: none; padding: 0; margin: 16px 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 12px; }
.cards li { margin: 0; }
.item { display: flex; gap: 14px; align-items: flex-start; height: 100%; }
.title { display: block; font-weight: 600; font-size: 16px; color: var(--vp-c-text-1); }
.text { display: block; font-size: 14px; color: var(--vp-c-text-2); margin-top: 2px; }
</style>
