<template>
  <div class="card" @click="handleSingleClick">
    <div :class="['card-inner', { flipped: isFlipped }]">
      <!-- Face avant de la carte -->
      <div class="card-face card-front">
        <div class="match-header">
          <span class="league">{{ league }}</span>
          <span class="match-date">{{ date }}</span>
        </div>
        <div class="teams">
          <div class="team-names">
            <span class="team">{{ teamA }}</span>
            <span class="vs">VS</span>
            <span class="team">{{ teamB }}</span>
          </div>
          <div class="team-logos">
            <img :src="teamALogo" alt="Logo de {{ teamA }}" class="team-logo" />
            <img :src="teamBLogo" alt="Logo de {{ teamB }}" class="team-logo" />
          </div>
        </div>
        <div class="confidence-section">
          <div class="risk-meter">
            <div class="risk-fill" :style="{ width: riskLevel + '%', backgroundColor: riskColor }"></div>
          </div>
          <p class="confidence-text">{{ confidence }}% de chances</p>
          <p class="odds">Cote: {{ odds }}</p>
        </div>
        <!-- Affichage des résultats des derniers matchs -->
        <div v-if="matchData" class="recent-results">
          <h4>Derniers résultats de {{ teamA }}</h4>
          <ul>
            <li v-for="(result, index) in matchData[teamA]" :key="index">
              {{ result.date }} - {{ result.opponent }} : {{ result.score }}
            </li>
          </ul>
        </div>
        <!-- Icône de like sur la face avant -->
        <div v-if="liked" class="like-icon">💖</div>
      </div>

      <!-- Face arrière de la carte -->
      <div class="card-face card-back">
        <div class="match-title">Combinaisons et Options</div>
        <ul>
          <li v-for="option in options" :key="option" class="option-item">{{ option }}</li>
        </ul>
        <div class="analysis-button-section">
          <button class="card-button" @click.stop="showDetailedAnalysis">Analyse détaillée</button>
        </div>
        <!-- Icône de like sur la face arrière -->
        <div v-if="liked" class="like-icon like-icon-back">💖</div>
      </div>
    </div>
  </div>
  <button class="login-button search-button-animation">Connexion</button>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PredictionCard',
  props: {
    league: String,
    date: String,
    teamA: String,
    teamB: String,
    confidence: Number,
    odds: String,
    options: Array,
    teamALogo: String,
    teamBLogo: String,
  },
  data() {
    return {
      isFlipped: false,
      liked: false,
      clickTimeout: null,
      matchData: null,
    };
  },
  computed: {
    riskLevel() {
      return Math.min(100, Math.max(0, (this.odds < 1 ? 100 : (1 / this.odds) * 100))); // Remplissage en fonction de la cote
    },
    riskColor() {
      return '#006400'; // Vert foncé pour la barre de chargement
    }
  },
  methods: {
    handleSingleClick() {
      if (this.clickTimeout) {
        clearTimeout(this.clickTimeout);
        this.clickTimeout = null;
        this.toggleLike();
      } else {
        this.clickTimeout = setTimeout(() => {
          this.toggleCard();
          this.clickTimeout = null;
        }, 300); // Délai pour le double clic
      }
    },
    toggleCard() {
      this.isFlipped = !this.isFlipped;
    },
    toggleLike() {
      this.liked = !this.liked;
    },
    showDetailedAnalysis() {
      alert("Affichage de l'analyse détaillée ici.");
    },
    getMatchData(teamName) {
      axios.get(`http://localhost:5000/results/${teamName}`)
        .then(response => {
          this.matchData = response.data;
          console.log(response.data);
        })
        .catch(error => {
          console.error('Error fetching match data:', error);
        });
    }
  },
  mounted() {
    // Fetch data for teamA when the component is mounted
    this.getMatchData(this.teamA);
  }
};
</script>

<style scoped>
.card {
  position: relative;
  width: 250px;
  height: 500px; /* Hauteur augmentée pour accommoder les résultats récents */
  perspective: 1500px;
  cursor: pointer;
  border-radius: 15px;
  transition: transform 0.3s ease;
  box-shadow: none;
}

.card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transition: transform 0.8s;
  transform-style: preserve-3d;
}

.flipped {
  transform: rotateY(180deg);
}

.card-face {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  border-radius: 1rem;
  padding: 1.5rem;
  background: white;
  box-shadow: 0 10px 20px rgba(44, 82, 130, 0.15);
}

.card-front {
  background: linear-gradient(135deg, #fff 0%, #f7fafc 100%);
  border: 2px solid #e2e8f0;
}

.card-back {
  transform: rotateY(180deg);
  background: linear-gradient(135deg, #fff 0%, #f7fafc 100%);
  border: 2px solid #e2e8f0;
  color: #1f2937;
}

.match-header {
  display: flex;
  justify-content: space-between;
  font-size: 0.9rem;
  color: #9aa5b1;
  margin-bottom: 15px;
}

.league {
  font-weight: 700;
  color: #9aa5b1;
}

.match-date {
  font-weight: 600;
  color: #9aa5b1;
}

.teams {
  margin: 25px 0;
  text-align: center;
}

.team-names {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
}

.team {
  font-size: 1.2rem;
  font-weight: 500;
  color: #1f2937;
}

.vs {
  font-size: 1.1rem;
  color: #6b7280;
}

.team-logos {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 10px;
}

.team-logo {
  width: 40px;
  height: 40px;
  margin: 0 10px;
}

.confidence-section {
  position: absolute;
  bottom: 100px;
  left: 2mm;
  right: 2mm;
  height: 3cm;
  background: #e0f7fa;
  padding: 8px;
  border-radius: 8px;
  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.risk-meter {
  width: 100%;
  height: 8px;
  background: #e2e8f0;
  border-radius: 5px;
  margin-bottom: 8px;
}

.risk-fill {
  height: 8px;
  border-radius: 5px;
  background-color: #006400; /* Vert foncé */
}

.recent-results {
  margin-top: 20px;
}

.recent-results h4 {
  font-size: 1.1rem;
  color: #1f2937;
  font-weight: bold;
}

.recent-results ul {
  list-style: none;
  padding: 0;
}

.recent-results li {
  color: #4a5568;
  margin-bottom: 5px;
}

.confidence-text {
  font-size: 1rem;
  font-weight: bold;
  color: #00796b;
}

.odds {
  font-size: 1.1rem;
  color: #4a5568;
}

.option-item {
  color: #1f2937;
  font-weight: 300;
  line-height: 1.5;
}

.analysis-button-section {
  position: absolute;
  bottom: 2mm;
  left: 36px;
  right: 2mm;
  text-align: center;
}

.card-button {
  padding: 0.75rem;
  border: none;
  border-radius: 0.5rem;
  background: #4299e1;
  color: white;
  font-weight: 600;
  cursor: pointer;
  width: calc(100% - 4mm);
}

.like-icon {
  position: absolute;
  bottom: 10px;
  left: 10px;
  font-size: 1.5rem;
  color: #ff4081;
}

.like-icon-back {
  position: absolute;
  bottom: 10px;
  left: 10px;
  font-size: 1.5rem;
  color: #ff4081;
}

.login-button {
  position: absolute;
  top: 10px;
  right: 10px;
  padding: 0.75rem;
  border: none;
  border-radius: 0.5rem;
  background: #007bff;
  color: white;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.login-button:hover {
  background-color: #0056b3;
}
</style>
