<script setup lang="ts">
// The three theory resources, as cards (same style as the roadmap).
import { withBase } from 'vitepress'
const cards = [
  { num: 1, title: "The C# Player's Guide", text: 'The book: short levels, from zero. The main theory companion.', link: '/learn/players-guide' },
  { num: 2, title: 'Microsoft Learn', text: 'Free modules and videos from Microsoft, with a free certification path.', link: '/learn/microsoft-learn' },
  { num: 3, title: 'Extra exercises', text: "The book's own challenges, tracked with XP in the C# Quest Tracker.", link: '/learn/quest-tracker' },
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
