<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
import { ref } from "vue"
import jardinagem from "../assets/jardinagem.png"
import limpeza from "../assets/limpeza.png"
import pintura from "../assets/pintura.png"
import eletricista from "../assets/eletricista.png"
import pedreiro from "../assets/pedreiro.png"
import baba from "../assets/baba.png"
import cozinheira from "../assets/cozinheira.png"

const track = ref(null)


const cards = [
  { name: "jardinagem", img: jardinagem },
  { name: "limpeza", img: limpeza },
  { name: "pintura", img: pintura },
  { name: "eletricista", img: eletricista },
  { name: "mestre de obras", img: pedreiro },
  { name: "babá", img: baba },
  { name: "cozinheiro", img: cozinheira }
]



const scrollAmount = 260 // largura card + gap

const scrollLeft = () => {
  track.value.scrollBy({ left: -scrollAmount, behavior: "smooth" })
}

const scrollRight = () => {
  track.value.scrollBy({ left: scrollAmount, behavior: "smooth" })
}
</script>
<template>
  <div class="titulo-categoria">Categorias</div>
  <div class="carousel">

    <button class="btn-prev" @click="scrollLeft">‹</button>

    <div class="carousel-track" ref="track">
     <div class="card" v-for="(item, i) in cards" :key="i">
  <img :src="item.img" class="card-icon" alt="">
  <span class="label">{{ item.name }}</span>
</div>
    </div>

    <button class="btn-next" @click="scrollRight">›</button>
  </div>

</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Coiny&family=Momo+Trust+Display&family=Momo+Trust+Sans:wght@200..800&family=Paytone+One&display=swap');

.carousel {
  display: flex;
  align-items: center;
  gap: 10px;
  width: 100%;
}

.carousel-track {
  display: flex;
  overflow-x: auto;
  scroll-behavior: smooth;
  gap: 16px;
  padding: 20px 0;
  padding-left: 15px;
  padding-right: 14px;

}

.carousel-track::-webkit-scrollbar {
  display: none;

}

.card {
  min-width: 220px;
  height: 220px;
  background: white;
  border-radius: 20px;
  border: none;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 500;
  user-select: none;
  transition: 0.3s;
}


.card:hover {
  opacity: 0.85;
  background-color: #d8e2cd;
  transform: translateY(-2px) scale(1.02);
}

.btn-prev,
.btn-next {
  background: none;
  border: none;
  font-size: 40px;
  color: #555;
  cursor: pointer;
  padding: 0 5px;
  transition: .2s;
}

.btn-prev:hover,
.btn-next:hover {
  color: black;
}

.titulo-categoria {
  font-family: "Momo Trust Sans", sans-serif;
  font-weight: bolder;
  text-align: start;
  margin-left: 50px;
  display: flex;
  font-size: 18px;
  width: 125px;
  background: #ffffff;
  padding: 8px 18px;
  box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;
  border-radius: 999px;
  /* deixa oval */
  font-size: 16px;
  color: #333;
}

.momo-trust-sans {
  font-family: "Momo Trust Sans", sans-serif;
  font-optical-sizing: auto;
  font-style: normal;

}

.card-icon {
  width: 60px;   /* ajustável */
  height: 60px;  /* ajustável */
  object-fit: contain;
}

.label {
   font-family: "Momo Trust Sans", sans-serif;
  font-optical-sizing: auto;
  font-style: normal;
  font-size: 16px;
  text-transform: capitalize;
  font-weight: 600;
  color: #000000;
}

.imgs img {
 transition: 0.3s;
}

.imgs img:nth-child(1):hover {
  transform: scale(1.1);
  background-color: #9cd885 ;
}
</style>