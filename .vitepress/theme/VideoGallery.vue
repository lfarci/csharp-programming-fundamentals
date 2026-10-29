<script setup lang="ts">
// The kept Absolute Beginners episodes as a gallery of cards with the official thumbnails, grouped like the roadmap.
import { withBase } from 'vitepress'
import course from '../course.json'
const groups = (course as any).videos as { group: string; episodes: { num: number; title: string; minutes: number; page: string; thumb: string | null; themes: string[] }[] }[]
</script>

<template>
  <div>
    <section v-for="g in groups" :key="g.group">
      <div class="cpf-kicker part-kicker">{{ g.group.split(': ')[0] }}</div>
      <h2 :id="'videos-' + g.group.split(': ')[1].toLowerCase().replace(/ /g, '-')" class="part-name">{{ g.group.split(': ')[1] }}</h2>
      <ul class="gallery">
        <li v-for="e in g.episodes" :key="e.page">
          <a class="cpf-card cpf-link card" :href="withBase(e.page)">
            <span class="pic">
              <img v-if="e.thumb" :src="e.thumb" alt="" loading="lazy" />
              <span v-else class="nopic">{{ e.title }}</span>
              <span class="cpf-num on badge" aria-hidden="true">{{ e.num }}</span>
              <span class="dur">{{ e.minutes }} min</span>
            </span>
            <span class="body"><span class="title">{{ e.title }}</span><span class="then">Then: {{ e.themes.join(', ') }}</span></span>
          </a>
        </li>
      </ul>
    </section>
  </div>
</template>

<style scoped>
.part-kicker { margin-top: 28px; }
.part-name { border-top: none; margin: 2px 0 12px; padding-top: 0; font-size: 20px; color: var(--vp-c-brand-1); }
.gallery { list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
.gallery li { margin: 0; }
.card { padding: 0; overflow: hidden; height: 100%; }
.pic { position: relative; display: block; aspect-ratio: 16 / 9; background: #1e2a4a; }
.pic img { width: 100%; height: 100%; object-fit: cover; display: block; }
.nopic { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; padding: 16px; text-align: center; color: #fff; font-weight: 600; font-size: 15px; background: linear-gradient(135deg, #3451b2, #1e2a4a); }
.badge { position: absolute; left: 10px; top: 10px; width: 30px; height: 30px; font-size: 13px; border-color: #fff; }
.dur { position: absolute; right: 8px; bottom: 8px; background: rgba(0,0,0,.75); color: #fff; font-size: 12px; border-radius: 4px; padding: 1px 6px; }
.body { display: block; padding: 10px 14px 12px; }
.title { display: block; font-weight: 600; font-size: 15px; color: var(--vp-c-text-1); line-height: 1.35; }
.then { display: block; font-size: 13px; color: var(--vp-c-text-2); margin-top: 4px; }
</style>
