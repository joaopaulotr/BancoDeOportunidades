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
      <p class="subtittle">
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

<section id="como-funciona">
  <h2 style="color: #131452;;">Como contratar um serviço?</h2>

  <div class="passos-container">

    <div class="passo">
      <div class="circulo">1</div>
      <h3>Busque pelo serviço</h3>
      <p>Use nossa barra de busca ou navegue pelas categorias para encontrar o que precisa.</p>
    </div>

    <div class="passo">
      <div class="circulo">2</div>
      <h3>Compare e escolha</h3>
      <p>Veja perfis, portfólios e avaliações de outros moradores para escolher o melhor profissional.</p>
    </div>

    <div class="passo">
      <div class="circulo">3</div>
      <h3>Contrate e avalie</h3>
      <p>Combine os detalhes, realize o pagamento com segurança e deixe sua avaliação.</p>
    </div>

  </div>
</section>

<section class="trust-section">
  <div class="trust-container">
    <h2 class="trust-title">Sua segurança é nossa prioridade</h2>

    <div class="trust-grid">

      <div class="trust-card">
        <svg class="trust-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
        </svg>
        <h3 class="trust-card-title">Perfis verificados</h3>
        <p class="trust-card-text">
          Integração com <strong>gov.br</strong> e SINE para validar cpf/cnpj dos profissionais.
        </p>
      </div>

      <div class="trust-card">
        <svg class="trust-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.921-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.783-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"></path>
        </svg>
        <h3 class="trust-card-title">Avaliações reais</h3>
        <p class="trust-card-text">
          Leia o que outros moradores acharam do serviço antes de contratar.
        </p>
      </div>

      <div class="trust-card">
        <svg class="trust-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m10 0h2a2 2 0 002-2V9a2 2 0 00-2-2m-9 7a2 2 0 01-2-2v-2m0 4h.01M17 17l-4-4m0 0l-4 4m4-4v12"></path>
        </svg>
        <h3 class="trust-card-title">Impulsione sua região</h3>
        <p class="trust-card-text">
          Contratar localmente fortalece a sua comunidade e resolve demandas coletivas.
        </p>
      </div>

    </div>
  </div>
</section>

        <section id="cadastro-profissional" class="cadastro-profissional" style="background-color: white">
           <div class="cadastro-wrapper">
  <div class="card-profissional">
                    <div>
                        <h2 style="font-size: 24px; color: white;">
                            Você é um prestador de serviço?
                        </h2>
                       <p class="subtittle-break" style="font-size: 15px; color: white;">
Cadastre-se no Banco de Oportunidades Locais e<br>
encontre novos clientes no seu próprio bairro.
</p>
                    </div>
                    <div>
                      <button class="card-profissional-button"> Quero me cadastrar </button> 
                        
                    </div>
                </div>
           </div>
        </section>
        <section class="featured-section">
  <div class="featured-container">
    <h2 class="featured-title">Profissionais em destaque na sua região</h2>

    <div class="featured-grid">

      <div class="featured-card">
        <div class="featured-photo" style="background-color:#ebf8ff;color:#3182ce;">foto profissional</div>
        <div class="featured-content">
          <div class="featured-head">
            <h3 class="featured-name">Carlos alberto</h3>
            <div class="featured-rating">
              <span class="star">★</span>
              <span>4.9</span>
            </div>
          </div>
          <p class="featured-role">Pintor e texturização</p>
          <p class="featured-desc">"Trabalho rápido e limpo, com foco em acabamento de primeira. Mais de 15 anos de experiência."</p>
          <a href="#" class="featured-link">Ver perfil completo →</a>
        </div>
      </div>

      <div class="featured-card">
        <div class="featured-photo" style="background-color:#e6fffa;color:#34a199;">foto profissional</div>
        <div class="featured-content">
          <div class="featured-head">
            <h3 class="featured-name">Maria da silva</h3>
            <div class="featured-rating">
              <span class="star">★</span>
              <span>5.0</span>
            </div>
          </div>
          <p class="featured-role">Costureira e estilista</p>
          <p class="featured-desc">"Ajustes, bainhas e transformações de roupas. Atendo com hora marcada no ateliê."</p>
          <a href="#" class="featured-link">Ver perfil completo →</a>
        </div>
      </div>

      <div class="featured-card">
        <div class="featured-photo" style="background-color:#fff5eb;color:#f6ad55;">foto profissional</div>
        <div class="featured-content">
          <div class="featured-head">
            <h3 class="featured-name">Jardel & Filhos</h3>
            <div class="featured-rating">
              <span class="star">★</span>
              <span>4.8</span>
            </div>
          </div>
          <p class="featured-role">Jardinagem e Paisagismo</p>
          <p class="featured-desc">"Manutenção de jardins residenciais e comerciais. Fazemos podas, plantio de grama e controle de pragas."</p>
          <a href="#" class="featured-link">Ver perfil completo →</a>
        </div>
      </div>

    </div>
  </div>
</section>

<footer id="footer">
    <div class="footer-container">

        <div class="footer-col">
            <h4>Conecta Bairro</h4>
            <p>Nossa missão é fortalecer a economia local, conectando moradores a prestadores de serviço qualificados da própria região.</p>
        </div>

        <div class="footer-col">
            <h4>Para Clientes</h4>
            <ul>
                <li><a href="#como-funciona">Como Funciona</a></li>
                <li><a href="#">Encontrar Serviços</a></li>
                <li><a href="#">Segurança</a></li>
                <li><a href="#">FAQ</a></li>
            </ul>
        </div>

        <div class="footer-col">
            <h4>Para Profissionais</h4>
            <ul>
                <li><a href="#cadastro-profissional">Quero me cadastrar</a></li>
                <li><a href="#">Vantagens</a></li>
                <li><a href="#">Regras da Plataforma</a></li>
                <li><a href="#">Parceria SINE</a></li>
            </ul>
        </div>

        <div class="footer-col">
            <h4>Contato</h4>
            <ul>
                <li><a href="#">Fale Conosco</a></li>
                <li><a href="#">Imprensa</a></li>
                <li><a href="#">Parcerias</a></li>
            </ul>

            <div class="social">
                <a href="#"><img width="48" height="48" src="https://img.icons8.com/fluency-systems-regular/48/EBEBEB/instagram-new--v1.png" alt="instagram-new--v1"/></a>
                <a href="#"><img width="48" height="48" src="https://img.icons8.com/fluency-systems-regular/48/EBEBEB/whatsapp--v1.png" alt="whatsapp--v1"/></a>
            </div>
        </div>

    </div>

    <div class="footer-bottom">
        <p>© 2025 Banco de Oportunidades Locais. Todos os direitos reservados.</p>
        <p>Supervisionado pela Secretaria Municipal do Trabalho.</p>
    </div>
</footer>

</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Coiny&family=Lexend:wght@100..900&family=Momo+Trust+Display&family=Momo+Trust+Sans:wght@200..800&family=Paytone+One&display=swap');

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
  color: #131452;
}

.subtittle{
  font-family: "Lexend", sans-serif;
  color: #16175e;
}

.momo-trust-sans {
  font-family: "Momo Trust Sans", sans-serif;
  font-optical-sizing: auto;
  font-style: normal;
}

.lexend {
 font-family: "Lexend", sans-serif;
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
  color: #131452;
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
  color: #16175e;
}

.card-profissional {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 40px;
  background-color: #eb5f07;
  font-family: "Lexend", sans-serif;
  color: white;
  padding: 40px 60px;
  border-radius: 15px;
 box-shadow: 0 3px 6px rgba(0,0,0,0.1), 0 3px 6px rgba(0,0,0,0.1);
  width: 42%;
}

.subtittle-break {
  white-space: pre-line;
}


.cadastro-profissional {
  width: 100%;
  background: rgb(241, 248, 255); 
  padding-top: 70px;
  height: 360px;
}

.card-profissional-button{
  background-color: white;
  color: #eb5f07;
  font-weight: 700;
  padding: 12px 24px;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  font-size: 16px;
  transition: 0.3s;
}

.card-profissional-button:hover {
  transform: translateY(-2px) scale(1.02);
   box-shadow: rgba(221, 56, 6, 0.19) 0px 10px 20px, rgba(199, 64, 1, 0.767) 0px 6px 6px;

}

.cadastro-wrapper {
  width: 100%;
  display: flex;
  flex-direction: column;
   align-items: center;
  justify-content: center;
}

#como-funciona {
  background: white;
  padding: 80px 0;
  text-align: center;
}

#como-funciona h2 {
  font-size: 30px;
  font-weight: 700;
  color: #111a3f;
  margin-bottom: 60px;
  font-family: "Lexend", sans-serif;
}

.passos-container {
  display: flex;
  justify-content: center;
  gap: 80px;
  flex-wrap: wrap;
}

.passo {
  max-width: 230px;
  font-family: "Lexend", sans-serif;
}

.circulo {
  width: 70px;
  height: 70px;
  background: rgba(141, 196, 183, 0.35);
  color: #eb5f07;
  border-radius: 50%;
  font-size: 26px;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 14px;
}

.passo h3 {
  font-size: 20px;
  font-weight: 600;
  color: #111a3f;
  margin-bottom: 10px;
}

.passo p {
  font-size: 14px;
  color: #818181;
  line-height: 1.4;
}


@media (max-width: 780px) {
  .passos-container {
    gap: 40px;
  }
}

@media (max-width: 500px) {
  #como-funciona h2 {
    font-size: 26px;
  }
}

.trust-section {
  padding: 80px 0;
  background-color: #d9e8e5;
}

.trust-container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 24px;
}

.trust-title {
  text-align: center;
  font-size: 28px;
  font-weight: 700;
   color: #111a3f;
  font-family: "Lexend", sans-serif;
  margin-bottom: 48px;
}

.trust-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 32px;
}

.trust-card {
  background: #ffffff;
  padding: 32px 24px;
  border-radius: 14px;
  text-align: center;
  box-shadow: 0px 4px 12px rgba(0,0,0,0.06);
  transition: transform .25s ease, box-shadow .25s ease;
}

.trust-card:hover {
  transform: translateY(-4px);
  box-shadow: 0px 8px 18px rgba(0,0,0,0.10);
}

.trust-icon {
  width: 46px;
  height: 46px;
  margin: 0 auto 12px auto;
  stroke: #eb5f07;
}

.trust-card-title {
  font-size: 16px;
  font-weight: 600;
  margin-bottom: 8px;
 color: #131452;
 font-family: "Lexend", sans-serif;
}

.trust-card-text {
  font-size: 13px;
  color: #4b5563;
  line-height: 1.5;
    font-family: "Lexend", sans-serif;
}

.featured-section {
  background: #e5ebbc;
  padding: 80px 0;
}

.featured-container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 24px;
}

.featured-title {
  text-align: center;
  font-size: 28px;
  font-weight: 700;
   font-family: "Lexend", sans-serif;
 color: #131452;
  margin-bottom: 48px;
}

.featured-grid {
  display: grid;
  gap: 32px;
}
@media(min-width: 600px) {
  .featured-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media(min-width: 900px) {
  .featured-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

.featured-card {
  background: #fff;
   font-family: "Lexend", sans-serif;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0,0,0,.08);
  transition: .3s;
}
.featured-card:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,.12);
}

.featured-photo {
  height: 150px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: 600;
  font-size: 18px;
}

.featured-content {
  padding: 20px;
}

.featured-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.featured-name {
  font-size: 18px;
  font-weight: 600;
  color: #080529;
}

.featured-rating {
  display: flex;
  align-items: center;
  color: #eb5f07;
  font-weight: 600;
}
.star {
  margin-right: 4px;
}

.featured-role {
  color: #eb5f07;
  font-size: 15px;
  font-weight: 500;
  margin: 6px 0 12px;
}

.featured-desc {
  color: #555;
  font-size: 13px;
  margin-bottom: 16px;
  line-height: 1.4;
}

.featured-link {
  color: #eb5f07;
  font-weight: 600;
  text-decoration: none;
  transition: .2s;
}
.featured-link:hover {
  text-decoration: underline;
}
#footer {
    background: #1f2937;
    color: #d1d5db;
    padding: 60px 0 30px;
    font-family: Arial, sans-serif;
}

.footer-container {
    width: 90%;
    max-width: 1200px;
    margin: auto;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 40px;
}

.footer-col h4 {
    color: #ffffff;
    font-size: 18px;
    margin-bottom: 16px;
    font-weight: 600;
}

.footer-col p {
    font-size: 14px;
    line-height: 1.6;
}

.footer-col ul {
    list-style: none;
    padding: 0;
}

.footer-col ul li {
    margin-bottom: 8px;
}

.footer-col ul li a {
    color: #d1d5db;
    text-decoration: none;
    font-size: 14px;
    transition: 0.3s;
}

.footer-col ul li a:hover {
    color: #ffffff;
}

.social {
    margin-top: 16px;
    display: flex;
    gap: 12px;
}

.social img {
    width: 20px;
    height: 20px;
    cursor: pointer;
    transition: 0.3s;
}

.social img:hover {
    opacity: 0.8;
}

.footer-bottom {
    width: 90%;
    max-width: 1200px;
    margin: 40px auto 0;
    border-top: 1px solid #374151;
    padding-top: 20px;
    text-align: center;
}

.footer-bottom p {
    font-size: 13px;
    margin: 4px 0;
}

/* Responsivo */
@media (max-width: 900px) {
    .footer-container {
        grid-template-columns: 1fr 1fr;
    }
}

@media (max-width: 600px) {
    .footer-container {
        grid-template-columns: 1fr;
        text-align: center;
    }

    .social {
        justify-content: center;
    }
}
</style>