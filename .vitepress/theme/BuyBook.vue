<script setup lang="ts">
// "Buy the book": the optional affiliate link from affiliate.ts, or the official site.
import { BOOK_AFFILIATE_URL } from './affiliate'
const official = 'https://csharpplayersguide.com/'
const buy = BOOK_AFFILIATE_URL || official
</script>

<template>
  <div class="cpf-card book">
    <div class="cpf-kicker">The theory companion</div>
    <div class="t">The C# Player's Guide, 5th edition</div>
    <div class="row">
      <a class="cpf-button" :href="buy" target="_blank" rel="noopener sponsored">Buy the book</a>
      <a :href="official" target="_blank" rel="noopener">Official site</a>
      <a href="https://csharpplayersguide.com/TheCSharpPlayersGuide-5thEdition-Sample.pdf" target="_blank" rel="noopener">Free sample (PDF)</a>
    </div>
    <p v-if="BOOK_AFFILIATE_URL" class="disclosure">"Buy the book" is an affiliate link: if you buy through it, this course may earn a small commission, at no extra cost to you.</p>
  </div>
</template>

<style scoped>
.book { margin: 16px 0 24px; padding: 18px 20px; }
.t { font-size: 18px; font-weight: 600; margin: 2px 0 12px; }
.row { display: flex; flex-wrap: wrap; gap: 12px 20px; align-items: center; font-size: 14px; }
.disclosure { font-size: 13px; color: var(--vp-c-text-2); margin: 12px 0 0; }
</style>
