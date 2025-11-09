<template>
  <section class="categoria-container">

    <h2 class="titulo">Serviços de Jardinagem</h2>

    <!-- Lista -->
    <div class="cards-list">
      <div v-for="servico in servicos" :key="servico.idServicos" class="card-servico">
        <h3>{{ servico.titulo }}</h3>
        <p class="desc">{{ servico.descricao }}</p>

        <div class="info">
          <span class="cidade">{{ servico.cidade }}</span>
          <span class="preco">R$ {{ servico.preco.toFixed(2) }}</span>
        </div>

        <button class="btn-contratar">Contratar</button>
      </div>
    </div>

  </section>
</template>

<script setup>
import { ref, onMounted } from "vue"
import axios from "axios"

const servicos = ref([])

onMounted(async () => {
  // Busca todos serviços
  const response = await axios.get("http://localhost:8000/servicos")

  // Filtra apenas categoria 1 (jardinagem)
  servicos.value = response.data.filter(s => s.Categorias_idCategorias === 1)
})
</script>

<style scoped>
.categoria-container {
  padding: 80px 40px;
}

.titulo {
  font-size: 26px;
  font-weight: 600;
  margin-bottom: 28px;
}

.cards-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 22px;
}

.card-servico {
  border: 1px solid #e6e6e6;
  border-radius: 12px;
  padding: 18px;
  background: #fff;
  transition: 0.3s;
}

.card-servico:hover {
  transform: translateY(-4px);
  box-shadow: 0 3px 12px rgba(0,0,0,0.08);
}

.card-servico h3 {
  font-size: 18px;
  margin-bottom: 10px;
}

.desc {
  font-size: 14px;
  color: #555;
  margin-bottom: 15px;
  min-height: 55px;
}

.info {
  display: flex;
  justify-content: space-between;
  margin-bottom: 15px;
  font-size: 14px;
}

.preco {
  font-weight: 600;
  color: #eb5f07;
}

.btn-contratar {
  width: 100%;
  padding: 10px;
  border-radius: 8px;
  background: #eb5f07;
  border: none;
  color: #fff;
  cursor: pointer;
  transition: 0.3s;
  font-size: 14px;
}

.btn-contratar:hover {
  background: #d95103;
}
</style>
