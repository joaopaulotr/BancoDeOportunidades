<script setup>
import Navbar from './components/Navbar.vue'
</script>

<template>
  <div id="app">
    <Navbar />
    <router-view />  <!-- aqui o Vue mostra Cadastro, Home ou Serviços -->
  </div>
</template>

