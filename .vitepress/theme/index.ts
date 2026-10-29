import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import ProgressPage from './ProgressPage.vue'
import ThemeExercises from './ThemeExercises.vue'
import ThemeGroups from './ThemeGroups.vue'
import ExerciseHeader from './ExerciseHeader.vue'
import ExercisesOverview from './ExercisesOverview.vue'
import DrillSets from './DrillSets.vue'
import CardList from './CardList.vue'
import LearnCard from './LearnCard.vue'
import RoadmapPath from './RoadmapPath.vue'
import ProgressSummary from './ProgressSummary.vue'
import MsLearnPath from './MsLearnPath.vue'
import VideoGallery from './VideoGallery.vue'
import LearnFlow from './LearnFlow.vue'
import HomeVideo from './HomeVideo.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  Layout: () => h(DefaultTheme.Layout, null, { 'home-features-before': () => h(HomeVideo) }),
  enhanceApp({ app }) {
    for (const [name, c] of Object.entries({ ProgressPage, ThemeExercises, ThemeGroups, ExerciseHeader, ExercisesOverview, DrillSets, CardList,
      LearnCard, RoadmapPath, ProgressSummary, MsLearnPath, VideoGallery, LearnFlow })) app.component(name, c)
  },
}
