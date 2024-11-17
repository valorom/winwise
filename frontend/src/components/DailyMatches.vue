<script setup>
import { ref, onMounted } from 'vue'
import MatchCard from './MatchCard.vue'

// Simulated data - In a real app, this would come from an API
const dailyMatches = ref([
  {
    id: 1,
    league: 'Ligue 1',
    date: '2024-03-20 20:45',
    homeTeam: 'PSG',
    awayTeam: 'Lyon',
    winProbability: 75,
    odds: 1.85,
    analysis: 'PSG montre une forme exceptionnelle à domicile avec 80% de victoires cette saison.',
    history: [
      'PSG 3-1 Lyon',
      'Lyon 0-1 PSG',
      'PSG 4-2 Lyon'
    ]
  },
  {
    id: 2,
    league: 'Premier League',
    date: '2024-03-20 21:00',
    homeTeam: 'Arsenal',
    awayTeam: 'Chelsea',
    winProbability: 68,
    odds: 2.10,
    analysis: 'Arsenal reste invaincu à domicile depuis 12 matchs.',
    history: [
      'Arsenal 2-0 Chelsea',
      'Chelsea 1-2 Arsenal',
      'Arsenal 3-1 Chelsea'
    ]
  },
  // Add more matches here
])

const likedMatches = ref([])

onMounted(() => {
  const stored = localStorage.getItem('likedMatches')
  if (stored) {
    likedMatches.value = JSON.parse(stored)
  }
})
</script>

<template>
  <div class="daily-matches">
    <h2>Paris du Jour 🔥</h2>
    <div class="matches-grid">
      <MatchCard
        v-for="match in dailyMatches"
        :key="match.id"
        :match="match"
      />
    </div>
  </div>
</template>

<style scoped>
.daily-matches {
  margin-top: 3rem;
}

h2 {
  font-size: 1.8rem;
  color: #0f172a;
  margin-bottom: 2rem;
  font-weight: 600;
}

.matches-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
  padding: 1rem;
  justify-items: center;
}

@media (max-width: 640px) {
  .matches-grid {
    grid-template-columns: 1fr;
  }
}
</style>