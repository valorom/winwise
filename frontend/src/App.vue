<template>
  <div id="app">
    <header class="header">
      <h1>WinWise</h1>
      <div class="search-container">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Recherchez une équipe ou une rencontre"
          class="search-input"
        />
        <button @click="searchMatches" class="search-button">Goaaaaal</button>
      </div>
      <h2>Paris du Jour <span class="emoji">🔥</span></h2>
    </header>

    <div class="cards-container">
      <PredictionCard
        v-for="(prediction, index) in filteredPredictions"
        :key="index"
        :league="prediction.league"
        :date="prediction.matchDate"
        :teamA="prediction.teamA"
        :teamB="prediction.teamB"
        :confidence="prediction.confidence"
        :odds="prediction.odds"
        :options="prediction.options"
      />
    </div>
  </div>
</template>

<script>
import PredictionCard from "./components/PredictionCard.vue";

export default {
  name: "App",
  components: {
    PredictionCard,
  },
  data() {
    return {
      searchQuery: "",
      predictions: [
        {
          league: "Ligue 1",
          matchDate: "2024-03-20 20:45",
          teamA: "PSG",
          teamB: "Lyon",
          confidence: 75,
          odds: "1.85",
          options: [
            "Pari combiné : PSG gagne & Over 2.5",
            "Buteur : Kylian Mbappé",
            "Score exact : 3-1",
          ],
        },
        {
          league: "Premier League",
          matchDate: "2024-03-20 21:00",
          teamA: "Arsenal",
          teamB: "Chelsea",
          confidence: 68,
          odds: "2.10",
          options: [
            "Pari combiné : Arsenal gagne & Under 3.5",
            "Buteur : Bukayo Saka",
            "Score exact : 2-1",
          ],
        },
      ],
    };
  },
  computed: {
    filteredPredictions() {
      if (!this.searchQuery) {
        return this.predictions;
      }
      const query = this.searchQuery.toLowerCase();
      return this.predictions.filter(
        (prediction) =>
          prediction.teamA.toLowerCase().includes(query) ||
          prediction.teamB.toLowerCase().includes(query) ||
          prediction.league.toLowerCase().includes(query)
      );
    },
  },
  methods: {
    searchMatches() {
      console.log("Recherche effectuée pour:", this.searchQuery);
    },
  },
};
</script>

<style scoped>
#app {
  text-align: center;
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f4f4f9;
}

.header {
  margin-bottom: 30px;
}

h1 {
  font-size: 3rem;
  color: #1a1a1a;
  margin-bottom: 0.5rem;
}

h2 {
  font-size: 1.5rem;
  color: #555;
}

.emoji {
  font-size: 1.5rem;
}

.search-container {
  margin-top: 20px;
  display: flex;
  justify-content: center;
  gap: 10px;
}

.search-input {
  padding: 10px;
  font-size: 1rem;
  border-radius: 8px;
  border: 1px solid #ddd;
  width: 400px;
}

.search-button {
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.search-button:hover {
  background-color: #0056b3;
}

.cards-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}
</style>
