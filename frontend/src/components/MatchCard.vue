<script setup>
import { ref } from 'vue'

const props = defineProps({
  match: {
    type: Object,
    required: true
  }
})

const isFlipped = ref(false)
const isLiked = ref(false)

const toggleCard = () => {
  isFlipped.value = !isFlipped.value
}

const toggleLike = (event) => {
  event.stopPropagation()
  isLiked.value = !isLiked.value
  const likedMatches = JSON.parse(localStorage.getItem('likedMatches') || '[]')
  
  if (isLiked.value) {
    likedMatches.push(props.match.id)
  } else {
    const index = likedMatches.indexOf(props.match.id)
    if (index > -1) likedMatches.splice(index, 1)
  }
  
  localStorage.setItem('likedMatches', JSON.stringify(likedMatches))
}
</script>

<template>
  <div class="card" :class="{ 'is-flipped': isFlipped }" @click="toggleCard">
    <div class="card-inner">
      <div class="card-front">
        <div class="card-header">
          <span class="league">{{ match.league }}</span>
          <span class="date">{{ match.date }}</span>
        </div>
        <div class="teams">
          <span class="team">{{ match.homeTeam }}</span>
          <span class="vs">VS</span>
          <span class="team">{{ match.awayTeam }}</span>
        </div>
        <div class="odds">
          <div class="win-probability">
            {{ match.winProbability }}% de chances
          </div>
          <div class="odds-value">
            Cote: {{ match.odds }}
          </div>
        </div>
        <button class="like-btn" :class="{ 'liked': isLiked }" @click="toggleLike">
          ❤
        </button>
      </div>
      <div class="card-back">
        <h3>Analyse détaillée</h3>
        <div class="stats">
          <p>{{ match.analysis }}</p>
          <div class="historical">
            <h4>Dernières rencontres</h4>
            <ul>
              <li v-for="(result, index) in match.history" :key="index">
                {{ result }}
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card {
  width: 300px;
  height: 400px;
  perspective: 1000px;
  cursor: pointer;
  margin: 1rem;
}

.card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transform-style: preserve-3d;
  transition: transform 0.6s;
}

.card.is-flipped .card-inner {
  transform: rotateY(180deg);
}

.card-front, .card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  border-radius: 15px;
  padding: 1.5rem;
  background: linear-gradient(145deg, #ffffff 0%, #f0f4f8 100%);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
}

.card-back {
  transform: rotateY(180deg);
  overflow-y: auto;
}

.card-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 1.5rem;
  color: #64748b;
  font-size: 0.9rem;
}

.teams {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 2rem;
}

.team {
  font-size: 1.2rem;
  font-weight: 600;
  color: #1e293b;
}

.vs {
  color: #94a3b8;
  font-weight: 500;
}

.odds {
  margin-top: auto;
  padding: 1rem;
  background: #f1f5f9;
  border-radius: 10px;
}

.win-probability {
  color: #059669;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.odds-value {
  color: #1e293b;
  font-weight: 500;
}

.like-btn {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: none;
  border: none;
  font-size: 1.5rem;
  color: #cbd5e1;
  cursor: pointer;
  transition: transform 0.2s;
  padding: 0.5rem;
}

.like-btn.liked {
  color: #ef4444;
  transform: scale(1.1);
}

.stats {
  text-align: left;
  color: #334155;
}

.historical {
  margin-top: 1rem;
}

.historical h4 {
  color: #0f172a;
  margin-bottom: 0.5rem;
}

.historical ul {
  list-style: none;
  padding: 0;
}

.historical li {
  padding: 0.3rem 0;
  border-bottom: 1px solid #e2e8f0;
  font-size: 0.9rem;
}
</style>