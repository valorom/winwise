<script setup>
import { ref } from 'vue'

const searchQuery = ref('')

const handleSearch = () => {
  // TODO: Implement search functionality
  console.log('Searching for:', searchQuery.value)
}
</script>

<template>
  <div class="search-container">
    <input
      type="text"
      v-model="searchQuery"
      class="search-input"
      placeholder="Recherchez une équipe ou une rencontre"
      @keyup.enter="handleSearch"
    />
    <button @click="handleSearch" class="search-button">
      Rechercher
    </button>
  </div>
</template>

<style scoped>
.search-container {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-bottom: 2rem;
}

.search-input {
  width: 100%;
  max-width: 500px;
  padding: 0.8rem 1rem;
  font-size: 1rem;
  border: 2px solid #e2e8f0;
  border-radius: 0.5rem;
  outline: none;
  transition: all 0.2s ease;
  background-color: white;
  color: #334155;
}

.search-input:focus {
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.search-button {
  padding: 0.8rem 1.5rem;
  font-size: 1rem;
  color: white;
  background-color: #3b82f6;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: all 0.2s ease;
  font-weight: 500;
}

.search-button:hover {
  background-color: #2563eb;
  transform: translateY(-1px);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.search-button:active {
  transform: translateY(0);
}
</style>