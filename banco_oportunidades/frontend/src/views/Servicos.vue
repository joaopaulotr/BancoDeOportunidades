<script setup>
import { useRoute } from 'vue-router'
import { computed } from 'vue'

import Jardinagem from '../components/categorias/Jardinagem.vue'
import Limpeza from '../components/categorias/Limpeza.vue'
import Pintura from '../components/categorias/Pintura.vue'
import MestreDeObras from '../components/categorias/MestreDeObras.vue'
import Baba from '../components/categorias/Baba.vue'
import Cozinheiro from '../components/categorias/Cozinheiro.vue'

const route = useRoute()

const mapa = {
  jardinagem: Jardinagem,
  limpeza: Limpeza,
  pintura: Pintura,
  mestredeobras: MestreDeObras,
  baba: Baba,
  cozinheiro: Cozinheiro
}

const componenteDaCategoria = computed(() => {
  const nome = route.params.categorias?.toLowerCase()
   console.log('servicos -> categorias:', nome)
   console.log('parametros:', route.params)
  return mapa[nome] || Jardinagem
})


</script>

<template>
  <component :is="componenteDaCategoria":key="route.params.categorias  || 'default'"/>
</template>
