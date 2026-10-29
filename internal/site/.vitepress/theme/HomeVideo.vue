<script setup lang="ts">
// The VS Code demo, full width right under the hero, so the terminal text is readable.
import { withBase } from 'vitepress'
</script>

<template>
  <section class="home-demo">
    <div class="cpf-kicker">See it in action</div>
    <p class="lead">You write the code in VS Code. The checker tells you what is wrong, then says DONE.</p>
    <video class="home-video" controls muted playsinline preload="metadata" :poster="withBase('/vscode-demo-poster.jpg')"
      aria-label="Demo in VS Code: start an exercise, see the check fail with a clear message, fix the loop, see DONE.">
      <source :src="withBase('/vscode-demo.mp4')" type="video/mp4">
      Your browser cannot play this video. It shows VS Code: ./ex start creates the file, ./ex check says NOT YET, a small fix to the loop, then DONE.
    </video>
  </section>
</template>

<style scoped>
.home-demo { max-width: 1152px; margin: 8px auto 40px; padding: 0 24px; }
@media (min-width: 640px) { .home-demo { padding: 0 48px; } }
@media (min-width: 960px) { .home-demo { padding: 0 64px; max-width: 1280px; } }
.lead { margin: 4px 0 16px; color: var(--vp-c-text-2); font-size: 16px; }
.home-video { display: block; width: 100%; border-radius: 12px; border: 1px solid var(--vp-c-divider); box-shadow: 0 12px 40px rgba(0,0,0,.12); background: #1e1e1e; }
</style>
