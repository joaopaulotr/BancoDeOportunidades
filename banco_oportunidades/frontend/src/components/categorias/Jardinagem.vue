<template>
  
  <div>
    
    <section class="title-section">
      <div class="container">
     
        <nav class="breadcrumbs">
          <a href="index.html">Início</a>
          <span class="mx-2">&gt;</span>
          <a href="index.html#servicos">Serviços</a>
          <span class="mx-2">&gt;</span>
          <span>Jardinagem</span>
        </nav>
        <h1>Serviços de Jardinagem</h1>
        <p>Encontre os melhores profissionais de jardinagem perto de você.</p>
      </div>
    </section>

   
    <section class="filter-bar">
      <div class="container filter-wrapper">
        <div class="filter-buttons">
          <span class="label">Filtrar por:</span>
          <button class="btn-filter active">Todos</button>
          <button class="btn-filter">Paisagismo</button>
          <button class="btn-filter">Manutenção</button>
          <button class="btn-filter">Podar Árvores</button>
          <button class="btn-filter">Plantar Grama</button>
        </div>
        <div>
          <button class="btn-filter advanced">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6V4m0 16v-2m0-10v2M4 12h2m16 0h-2m-8 8v-2m0-10V4m0 4h2m-2 6h2m0 4h2M6 12h2m0-4h2m4 4h2m0 4h2"></path></svg>
            Filtros Avançados
          </button>
        </div>
      </div>
    </section>

    
    <section class="main-content">
      <div class="container">
        <div class="content-grid">

        
          <div class="main-column">
            <h2>Mostrando {{ servicos.length }} serviços disponíveis de jardinagem</h2>
          
            <div class="card-list">
              <div class="service-card"
                v-for="servico in servicos"
                :key="servico.id"
                @click="abrirPopup(servico)"
              >
                <img :src="servico.imagem" alt="" class="card-image">
                <div class="card-content">
                  <div>
                    <div class="card-header">
                      <h3>{{ servico.nome }}</h3>
                      <div class="card-status" :class="servico.status === 'ativo' ? 'status-ativo' : 'status-inativo'">
                        <span class="status-bolinha"></span>
                        <span>{{ servico.status || 'inativo' }}</span> <!-- Garante um fallback -->
                      </div>
                    </div>
                    <div class="card-info">
                      <span class="info-distance">📍 aprox. <span>{{ servico.distancia }} km</span> de você</span>
                      <span class="info-verified">✔️ verificado (gov.br)</span>
                    </div>
                    <p class="card-description">{{ servico.descricao }}</p>
                  </div>
                  <div class="card-footer">
                    <div class="card-tags">
                      <span v-for="tag in servico.tags" :key="tag" class="tag">{{ tag }}</span>
                    </div>
                    <button class="btn-ver">ver mais</button>
                  </div>
                </div>
              </div>
            </div>
          </div>

      
          <div class="sidebar-column">
            <div class="sticky-map">
              <h3>Sua Localização no Mapa</h3>
    <iframe
      src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3651.218476269941!2d-51.93290948445436!3d-23.42099998464416!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ecf01f87f7edc9%3A0xeec5e7e7e94e9981!2sMaring%C3%A1%2C%20PR!5e0!3m2!1spt-BR!2sbr!4v1700150000000!5m2!1spt-BR!2sbr"
      width="100%"
      height="380"
      style="border:0; border-radius: 12px;"
      allowfullscreen=""
      loading="lazy"
      referrerpolicy="no-referrer-when-downgrade"
    ></iframe>
            </div>
          </div>

        </div>
      </div>
    </section>

   
    <div v-if="popupVisivel" class="popup-overlay" @click.self="fecharPopup">
      <div class="popup">
        <button class="close-btn" @click="fecharPopup">×</button>
        <div class="popup-body">
          <div class="popup-info">
            <h2>{{ servicoSelecionado.nome }}</h2>
            <p>{{ servicoSelecionado.descricao }}</p>
            <p><strong>Rua:</strong> {{ servicoSelecionado.rua }}</p>
            <p><strong>Bairro:</strong> {{ servicoSelecionado.bairro }}</p>
            <p><strong>Cidade:</strong> {{ servicoSelecionado.cidade }}</p>
            <p><strong>Preço:</strong> R$ {{ servicoSelecionado.preco.toFixed(2) }}</p>
            <button class="btn-inscrever" @click="toggleInscricao">
              {{ inscrito ? "inscrito" : "se inscrever" }}
            </button>
          </div>
          <div class="popup-map">
            <iframe :src="servicoSelecionado.mapa" allowfullscreen loading="lazy"></iframe>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>


<script>
export default {
  data() {
    return {
      servicos: [
        {
          id: 1,
          nome: "Paisagismo residencial",
          descricao: "Design completo de jardim com plantas selecionadas",
          imagem: "https://placehold.co/500x300/9ccc65/fff?text=paisagismo",
          distancia: 1.2,
          rua: "Rua das Flores, 145",
          bairro: "Zona 3",
          cidade: "maringá",
          mapa: "https://maps.google.com/maps?q=rua%20das%20flores%20145%20maringá&output=embed",
          preco: 250.00,
          tags: ["Paisagismo"],
          status: 'ativo'
        },
        {
          id: 2,
          nome: "Manutenção de jardim em prédio",
          descricao: "Poda, limpeza e cuidado contínuo",
          imagem: "https://placehold.co/500x300/7cb342/fff?text=manutenção",
          distancia: 0.9,
          rua: "Rua Neo alves Martins, 80",
          bairro: "Centro",
          cidade: "maringá",
          preco: 640.00,
          mapa: "https://maps.google.com/maps?q=rua%20neo%20alves%20martins%2080%20maringá&output=embed",
          tags: ["Manutenção"],
          status: 'ativo'
        },
        {
          id: 3,
          nome: "Plantio de grama",
          descricao: "Nivelamento de solo e aplicação de grama",
          imagem: "https://placehold.co/500x300/558b2f/fff?text=grama",
          distancia: 2.3,
          rua: "Rua Prudente de Morais, 210",
          bairro: "Zona 5",
          cidade: "maringá",
          preco: 762.00,
          mapa: "https://maps.google.com/maps?q=rua%20prudente%20de%20morais%20210%20maringá&output=embed",
          tags: ["Plantio"],
           status: 'inativo' 
        },
        {
          id: 4,
          nome: "Poda de árvores",
          descricao: "Poda de segurança e modelagem de copa",
          imagem: "https://placehold.co/500x300/6b8e23/fff?text=poda",
          distancia: 3.8,
          rua: "Avenida Mandacaru, 33",
          bairro: "Mandacaru",
          preco: 300.00,
          cidade: "maringá",
          mapa: "https://maps.google.com/maps?q=avenida%20mandacaru%2033%20maringá&output=embed",
          tags: ["Poda", "Arvores"],
          status: "ativo" 
        }
      ],
      popupVisivel: false,
      servicoSelecionado: {},
      inscrito: false
    }
  },
  methods: {
    abrirPopup(servico) {
      this.servicoSelecionado = servico;
      this.popupVisivel = true;
    },
    fecharPopup() {
      this.popupVisivel = false;
      this.inscrito = false;
    },
    toggleInscricao() {
      this.inscrito = !this.inscrito;
    }
  }
}
</script>

<style scoped>



/* Container (do servicos.html) */
.container {
  width: 100%;
  max-width: 1280px;
  margin-left: auto;
  margin-right: auto;
  padding-left: 1rem;
  padding-right: 1rem;
}

.header { text-align: center; margin-bottom: 40px; }
.header h1 { font-size: 30px; }
.header p { color: #555; }

.card-list {
  display: flex;
  flex-direction: column;
  gap: 1.5rem; 
}


.service-card {
  background-color: #fff;
  border-radius: 12px;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  cursor: pointer;
  transition: .3s;
  box-shadow: 0 4px 6px rgba(0,0,0,.08);
}
.service-card:hover { box-shadow: 0 10px 18px rgba(0,0,0,.12); }

.card-image {
  width: 100%; 
  height: 200px; 
  object-fit: cover;
}

.card-content {
  padding: 1.5rem;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.card-header { display: flex; justify-content: space-between; }
.card-header h3 { font-size: 1.25rem; font-weight: 700; }



.card-info { display: flex; flex-wrap: wrap; gap: 1rem; font-size: .875rem; color: var(--cor-texto-secundario); margin: 0.5rem 0; }
.info-distance { color: #15803d; font-weight: 600; }
.info-distance span { font-weight: 700; }
.info-verified { color: #2563eb; font-weight: 500; }

.card-description { font-size: .875rem; margin: .5rem 0 1rem; color: var(--cor-texto-secundario); }

.card-footer { 
  display: flex; 
  flex-direction: column; 
}
.card-tags { display: flex; flex-wrap: wrap; gap: .5rem; margin-bottom: 1rem; }
.tag { background-color:#e5ebbc; ; padding: .2rem .6rem; border-radius: 999px; font-size: .75rem; color: #374151; font-weight: 500;}

.btn-ver {
  background: #eb5f07;
  border: none;
  color: white;
  padding: 8px 14px;
  border-radius: 6px;
  cursor: pointer;
  align-self: flex-start;
}
.btn-ver:hover { background: #d45606; }


.popup-overlay {
  position: fixed; inset: 0;
  background: rgba(0,0,0,.55);
  display: flex; justify-content: center; align-items: center;
  z-index: 100;
}
.popup {
  background: white;
  width: 90%;
  max-width: 750px;
  padding: 26px;
  border-radius: 14px;
  position: relative;
}
.close-btn { position: absolute; right: 14px; top: 10px; font-size: 24px; cursor: pointer; border: none; background: none; }

.popup-body { display: flex; flex-direction: column; gap: 18px; }
.popup-info { flex: 1; }

.popup-map {
  width: 100%; 
  height: 230px;
  overflow: hidden;
  border-radius: 10px;
}

.popup-map iframe { width: 100%; height: 100%; border: none; }

.btn-inscrever {
  margin-top: 12px;
  background: #eb5f07;
  border: none;
  color: white;
  padding: 10px 14px;
  border-radius: 8px;
  cursor: pointer;
}
.btn-inscrever:hover { background: #d45606; }


.card-status {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: .875rem;
  font-weight: 600;
}
.status-bolinha {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  display: inline-block;
}
.status-ativo .status-bolinha { background-color: #16a34a; }
.status-inativo .status-bolinha { background-color: #dc2626; }
.status-inativo { color: #dc2626; }
.status-ativo { color: #16a34a; }


.title-section {
  background-color: #ffffff;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
  padding: 2rem 0;
}
.breadcrumbs {
  font-size: 0.875rem;
  color: var(--cor-texto-secundario);
  margin-bottom: 0.5rem;
}
.breadcrumbs a:hover { color: #d45606 }
.breadcrumbs span:last-child {
  font-weight: 500;
  color: #1059be;
}
.title-section h1 {
  font-size: 2.25rem;
  font-weight: 900;
}
.title-section p {
  font-size: 1.125rem;
  color: var(--cor-texto-secundario);
  margin-top: 0.5rem;
}


.filter-bar {
  padding: 1rem 0;
   background-color: #ffffff;
 
}
.filter-wrapper {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
}
.filter-buttons {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  overflow-x: auto;
  padding: 0.5rem 0;
}
.filter-buttons .label {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--cor-texto-secundario);
  margin-right: 0.5rem;
  display: none; 
}
.btn-filter {
  padding: 0.5rem 1rem;
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 500;
  background-color: #ffffff;
  color: var(--cor-texto-secundario);
  border: 1px solid var(--cor-borda);
  transition: background-color 0.2s;
  white-space: nowrap;
}
.btn-filter:hover { background-color: #f3f4f6; }
.btn-filter.active {
  background-color: #d9e8e5;
  color: #ffffff;
  border-color: transparent;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
}
.btn-filter.advanced {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}
.btn-filter.advanced svg {
  width: 1rem;
  height: 1rem;
}


.main-content {
  padding: 3rem 0;
}
.content-grid {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}
.main-column {
  width: 100%;
}
.main-column h2 {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
}
.sidebar-column {
  width: 100%;
}
.sidebar-column h3 {
  font-size: 1.25rem;
  font-weight: 700;
  margin-bottom: 1rem;
}
.sticky-map {
  position: -webkit-sticky;
  position: sticky;
  top: 6rem; 
}
.map-placeholder {
  background-color: #e5e7eb;
  border-radius: 0.5rem;
  height: 24rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: var(--cor-texto-secundario);
  text-align: center;
  padding: 1rem;
}
.map-placeholder svg {
  width: 4rem;
  height: 4rem;
  color: #9ca3af;
  stroke-width: 1;
}


@media (min-width: 640px) {
  .container {
    padding-left: 1.5rem;
    padding-right: 1.5rem;
  }
  .service-card {
    flex-direction: row; 
  }
  .card-image {
    width: 12rem; 
    height: auto; 
  }
  .card-footer {
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
  }
  .card-tags {
    margin-bottom: 0;
  }
  .btn-ver {
    width: auto;
  }
  .popup-body {
    flex-direction: row; 
  }
  .popup-map {
    width: 40%;
  }
}


@media (min-width: 768px) {
  .filter-buttons .label {
    display: block; 
  }
}


@media (min-width: 1024px) {
  .container {
    padding-left: 2rem;
    padding-right: 2rem;
  }
  .content-grid {
    flex-direction: row; 
  }
  .main-column {
    width: 66.666667%; 
  }
  .sidebar-column {
    width: 33.333333%; 
  }
}
</style>