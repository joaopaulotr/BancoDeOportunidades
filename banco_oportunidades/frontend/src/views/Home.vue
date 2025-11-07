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



const scrollAmount = 260

const scrollLeft = () => {
  track.value.scrollBy({ left: -scrollAmount, behavior: "smooth" })
}

const scrollRight = () => {
  track.value.scrollBy({ left: scrollAmount, behavior: "smooth" })
}
</script>
<template>
<section class="prof flex flex-col items-center justify-center text-center py-20" style="background-color: white; height: 160px; margin-top: 200px;">
<div class="propaganda">
<h1 class="titulo1 mb-6">
        Encontre serviços e profissionais de confiança no seu bairro.
      </h1>
      <p class="text-lg text-gray-600 max-w-4xl mx-auto mb-10" style="font-size: 18px">
        Conectamos profissionais qualificados a quem busca serviços, fortalecendo a economia da sua região.
      </p>
</div>
      
      
  </section>
<section id="categorias-sec" class="categorias-sec">
  <div class="categorias-wrapper">

    <div class="titulo-categoria">Categorias</div>

    <div class="carousel">
      <button class="btn-prev" @click="scrollLeft">‹</button>

      <div class="carousel-track" ref="track">
        <div class="card" v-for="(item, i) in cards" :key="i"
          @click="router.push({ name: 'Servicos', params: { categorias: item.name.toLowerCase().replace(/ /g, '') } })">
          <img :src="item.img" class="card-icon" alt="">
          <span class="label">{{ item.name }}</span>
        </div>
      </div>

      <button class="btn-next" @click="scrollRight">›</button>
    </div>

  </div>
</section>

        <section id="cadastro-profissional" class="cadastro-profissional" style="background-color: white">
           <div class="cadastro-wrapper">
  <div class="card-profissional">
                    <div>
                        <h2 style="font-size: 30px; color: white;">
                            Você é um prestador de serviço?
                        </h2>
                        <p class="text-blue-100 text-lg max-w-lg">
                            Cadastre-se no Banco de Oportunidades Locais e encontre novos clientes no seu próprio bairro.
                        </p>
                    </div>
                    <div class="mt-6 md:mt-0 md:ml-6 flex-shrink-0">
                        <a href="#" class="bg-white text-blue-600 px-6 py-3 rounded-full font-bold text-lg hover:bg-gray-100 transition duration-300">
                            Quero me cadastrar
                        </a>
                    </div>
                </div>
           </div>
              
          
        </section>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Coiny&family=Momo+Trust+Display&family=Momo+Trust+Sans:wght@200..800&family=Paytone+One&display=swap');

html {
  scroll-behavior: smooth;
}

.carousel {
  display: flex;
  align-items: center;
  gap: 10px;
  width: 1200px;
    justify-content: center;

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
  min-width: 230px;
  height: 230px;
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


.card:nth-child(1):hover {
  opacity: 0.85;
  background-color: #c1d68879;
  transform: translateY(-2px) scale(1.02);

}

.card:nth-child(2):hover {
  opacity: 0.85;
  background-color: #d196178e;
  transform: translateY(-2px) scale(1.02);
}

.card:nth-child(3):hover {
  opacity: 0.85;
  background-color: #d117b24b;
  transform: translateY(-2px) scale(1.02);
}

.card:nth-child(4):hover {
  opacity: 0.85;
  background-color: #6fc7dd9c;
  transform: translateY(-2px) scale(1.02);
}

.card:nth-child(5):hover {
  opacity: 0.85;
  background-color: #9a98fa86;
  transform: translateY(-2px) scale(1.02);
}

.card:nth-child(6):hover {
  opacity: 0.85;
  background-color: #17d1a367;
  transform: translateY(-2px) scale(1.02);
}

.card:nth-child(7):hover {
  opacity: 0.85;
  background-color: #e2613a88;
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
   margin-right: 980px;   
  margin-bottom: 8px;
  display: flex;
  font-size: 18px;
  width: 125px;
  background: #ffffff;
  padding: 8px 18px;
box-shadow: rgba(0, 0, 0, 0.18) 0px 2px 4px;
  border-radius: 999px;
  font-size: 16px;
  color: #333;
}

.momo-trust-sans {
  font-family: "Momo Trust Sans", sans-serif;
  font-optical-sizing: auto;
  font-style: normal;

}

.card-icon {
  width: 60px;
  height: 60px;
  object-fit: contain;
}

.label {
  font-family: "Momo Trust Sans", sans-serif;
  font-optical-sizing: auto;
  font-style: normal;
  margin-top: 18px;
  font-size: 16px;
  text-transform: capitalize;
  font-weight: 600;
  color: #111a3f;
}

.categorias-sec {
  width: 100%;
  background: rgb(241, 248, 255); 
  height: 380px;
  padding-top: 30px;
}

.categorias-wrapper {
  width: 100%;
  display: flex;
  flex-direction: column;
   align-items: center;
  justify-content: center;
}

.propaganda {
 position: relative;
 bottom: 12px;
 
}
.titulo1{
 font-family: "Momo Trust Sans", sans-serif;
 font-size: 45px;
 font-weight: 700;
}

.card-profissional {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 40px;
  background-color:  #eb5f07;
  color: white;
  padding: 40px 60px;
  border-radius: 15px;
 box-shadow: 0 3px 6px rgba(0,0,0,0.1), 0 3px 6px rgba(0,0,0,0.1);
  width: 50%;
}


.cadastro-profissional {
  width: 100%;
  background: rgb(241, 248, 255); 
  padding-top: 70px;
  height: 360px;
}

.cadastro-wrapper {
  width: 100%;
  display: flex;
  flex-direction: column;
   align-items: center;
  justify-content: center;
}

</style>