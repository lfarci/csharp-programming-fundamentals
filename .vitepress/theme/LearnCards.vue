<script setup lang="ts">
// The theory resources, as roadmap-style cards. Microsoft Learn first: it is the main companion.
import { withBase } from 'vitepress'
const cards = [
  { num: 1, title: 'Microsoft Learn: Get started with C#', text: 'The main companion: 6 free parts of short modules. Each part has its themes here.', link: '/learn/microsoft-learn' },
  { num: 2, title: 'C# Fundamentals for Absolute Beginners', text: 'The video series on Microsoft Learn: one episode per idea, then the matching theme.', link: '/learn/microsoft-learn#the-videos' },
  { num: 3, title: 'Foundational C# with Microsoft', text: 'A free certification by freeCodeCamp and Microsoft, built on the same 6 parts.', link: '/learn/microsoft-learn#the-free-certification' },
  { num: 4, title: 'Extra exercises', text: 'More practice, tracked with XP in the C# Quest Tracker.', link: '/learn/quest-tracker' },
]
</script>

<template>
  <ol class="cards">
    <li v-for="c in cards" :key="c.num">
      <a class="cpf-card cpf-link item" :href="withBase(c.link)">
        <span class="cpf-num" aria-hidden="true">{{ c.num }}</span>
        <span><span class="title">{{ c.title }}</span><span class="text">{{ c.text }}</span></span>
      </a>
    </li>
  </ol>
</template>

<style scoped>
.cards { list-style: none; padding: 0; margin: 16px 0; display: grid; gap: 12px; }
.cards li { margin: 0; }
.item { display: flex; gap: 14px; align-items: flex-start; }
.title { display: block; font-weight: 600; font-size: 16px; color: var(--vp-c-text-1); }
.text { display: block; font-size: 14px; color: var(--vp-c-text-2); margin-top: 2px; }
</style>
