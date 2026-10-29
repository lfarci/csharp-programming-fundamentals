import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import MarkDone from './MarkDone.vue'
import ProgressPage from './ProgressPage.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  Layout: () => h(DefaultTheme.Layout, null, { 'doc-before': () => h(MarkDone) }),
  enhanceApp({ app }) { app.component('ProgressPage', ProgressPage) },
}
