import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import MarkDone from './MarkDone.vue'
import ProgressPage from './ProgressPage.vue'
import ThemeExercises from './ThemeExercises.vue'
import ExercisesOverview from './ExercisesOverview.vue'
import RoadmapPath from './RoadmapPath.vue'
import ProgressSummary from './ProgressSummary.vue'
import MsLearnPath from './MsLearnPath.vue'
import VideoGallery from './VideoGallery.vue'
import LearnFlow from './LearnFlow.vue'
import HomeVideo from './HomeVideo.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  Layout: () => h(DefaultTheme.Layout, null, { 'doc-before': () => h(MarkDone), 'home-features-before': () => h(HomeVideo) }),
  enhanceApp({ app }) { app.component('ProgressPage', ProgressPage)
    app.component('ThemeExercises', ThemeExercises)
    app.component('ExercisesOverview', ExercisesOverview)
    app.component('RoadmapPath', RoadmapPath)
    app.component('ProgressSummary', ProgressSummary)
    app.component('MsLearnPath', MsLearnPath)
    app.component('VideoGallery', VideoGallery)
    app.component('LearnFlow', LearnFlow) },
}
