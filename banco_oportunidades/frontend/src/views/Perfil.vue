<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import jardinagem from '../assets/jardinagem.png'
import garden2 from '../assets/garden2.png'
import pintor from '../assets/pintor.png'

// small page-level class so the background can be adjusted like other pages
onMounted(() => document.body.classList.add('profile-page'))
onUnmounted(() => document.body.classList.remove('profile-page'))

const router = useRouter()

const gardener = ref({
    name: 'Mariana Silva',
    title: 'Jardineira e paisagista',
    avatar: jardinagem,
    location: 'Vila Verde, São Paulo',
    rating: 4.8,
    jobs: 128,
    priceHour: 60,
    bio:
        'Cuido do seu jardim com carinho: poda, adubação, plantio e manutenção. Trabalho com paisagismo residencial e pequenos projetos comunitários. Experiência em plantas nativas e hortas caseiras.',
    services: [
        { name: 'Poda e manutenção', price: 50 },
        { name: 'Projeto de canteiro', price: 120 },
        { name: 'Implantação de horta', price: 180 }
    ],
    gallery: [garden2, pintor]
})

const showFullBio = ref(false)
const toggleBio = () => (showFullBio.value = !showFullBio.value)

const stars = computed(() => {
    const full = Math.floor(gardener.value.rating)
    const half = gardener.value.rating - full >= 0.5
    const arr = []
    for (let i = 0; i < full; i++) arr.push('full')
    if (half) arr.push('half')
    while (arr.length < 5) arr.push('empty')
    return arr
})

function goBack() {
    router.back()
}

function contratar() {
    // placeholder behaviour: send user back to home or to a booking page if available
    router.push('/home')
}

</script>

<template>
    <div class="profile-root container">
        <div class="profile-header">
            <button class="btn-back" @click="goBack">← Voltar</button>
            <div class="profile-main">
                <img :src="gardener.avatar" alt="avatar" class="avatar" />
                <div class="info">
                    <h2>{{ gardener.name }}</h2>
                    <div class="sub">{{ gardener.title }} • {{ gardener.location }}</div>

                    <div class="meta">
                        <div class="rating">
                            <span v-for="(s, i) in stars" :key="i" class="star" :data-type="s">
                                <template v-if="s === 'full'">★</template>
                                <template v-else-if="s === 'half'">☆</template>
                                <template v-else>☆</template>
                            </span>
                            <span class="score">{{ gardener.rating }} • {{ gardener.jobs }} jobs</span>
                        </div>
                        <div class="price">R$ {{ gardener.priceHour }} / hora</div>
                    </div>
                </div>
            </div>
            <div class="actions">
                <button class="btn btn-outline" @click="router.push('/home')">Mensagem</button>
                <button class="btn btn-primary" @click="contratar">Contratar</button>
            </div>
        </div>

        <div class="profile-body">
            <div class="left-col">
                <section class="card bio">
                    <h3>Sobre</h3>
                    <p>
                        <span v-if="!showFullBio">{{ gardener.bio.slice(0, 140) }}<span v-if="gardener.bio.length &gt; 140">... </span></span>
                        <span v-if="showFullBio">{{ gardener.bio }}</span>
                        <button class="linkish" @click="toggleBio">{{ showFullBio ? 'Ver menos' : 'Ver mais' }}</button>
                    </p>
                </section>

                <section class="card services">
                    <h3>Serviços oferecidos</h3>
                    <div class="service-list">
                        <div class="service" v-for="(s, i) in gardener.services" :key="i">
                            <div class="service-name">{{ s.name }}</div>
                            <div class="service-price">R$ {{ s.price }}</div>
                        </div>
                    </div>
                </section>

                <section class="card reviews">
                    <h3>Avaliações</h3>
                    <div class="review">
                        <div class="review-head">
                            <strong>Ana P.</strong>
                            <span class="review-score">5.0</span>
                        </div>
                        <p>Excelente trabalho! Meu jardim nunca esteve tão bonito. Recomendo muito.</p>
                    </div>

                    <div class="review">
                        <div class="review-head">
                            <strong>Lucas M.</strong>
                            <span class="review-score">4.5</span>
                        </div>
                        <p>Profissional, pontual e atenciosa. Fez um ótimo projeto para o nosso canteiro.</p>
                    </div>
                </section>
            </div>

            <aside class="right-col">
                <section class="card contact-card">
                    <h4>Contato</h4>
                    <div class="contact-row"><strong>Telefone:</strong> (11) 9 9999-9999</div>
                    <div class="contact-row"><strong>Email:</strong> mari.silva@email.com</div>
                    <div class="contact-row"><strong>Atendimento:</strong> Seg-Sex, 8h–17h</div>
                </section>

                <section class="card gallery">
                    <h4>Galeria</h4>
                    <div class="gallery-grid">
                        <img v-for="(g, idx) in gardener.gallery" :key="idx" :src="g" alt="galeria" />
                    </div>
                </section>
            </aside>
        </div>
    </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Coiny&family=Momo+Trust+Display&family=Paytone+One&display=swap');

.profile-page {
    background: linear-gradient(135deg, #f3f7ee 0%, #eef2f7 100%);
}

.profile-root.container {
    max-width: 1100px;
    margin: 28px auto;
    padding: 20px;
}

.profile-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    margin-bottom: 18px;
}

.btn-back {
    background: none;
    border: none;
    color: #3b6b3b;
    cursor: pointer;
    font-weight: 600;
}

.profile-main {
    display: flex;
    gap: 18px;
    align-items: center;
}

.avatar {
    width: 110px;
    height: 110px;
    border-radius: 14px;
    object-fit: cover;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
}

.info h2 { margin: 0; font-size: 22px }
.info .sub { color: #555; margin-top: 4px }

/* subtle green label backgrounds for headings and important inline text */
.info h2,
.info .sub,
.card h3,
.card h4,
.service-name,
.score,
.review-head strong {
    display: inline-block;
    background: rgba(108, 161, 92, 0.2); /* darker green tint */
    padding: 2px 8px;
    border-radius: 999px;
    backdrop-filter: blur(2px);
}

/* slightly stronger label for price to keep emphasis */
.price {
    background: linear-gradient(90deg, rgba(71,139,71,0.15), rgba(39,105,39,0.15));
    padding: 6px 12px;
    border-radius: 10px;
    color: #1d5620;
    font-weight: 800;
}

.meta { display:flex; align-items:center; gap: 12px; margin-top:8px }
.rating { display:flex; align-items:center; gap:8px }
.star { color: #f2b01e; font-size: 18px }
.score { color:#555; font-weight:600 }
.price { background:#e7f6ea; padding:6px 10px; border-radius:8px; color:#266b2a; font-weight:700 }

.actions { display:flex; gap:10px }
.btn { padding:8px 12px; border-radius:8px; cursor:pointer }
.btn-outline { border:1px solid #ccc; background:white }
.btn-primary { background:#3b6b3b; color:white; border:none }

.profile-body { display:flex; gap:18px }
.left-col { flex: 1 }
.right-col { width: 320px }

.card { background:white; padding:14px; border-radius:12px; box-shadow: 0 6px 20px rgba(0,0,0,0.05); margin-bottom:14px }
.card h3, .card h4 { margin:0 0 10px 0 }

.bio p { color:#444; line-height:1.4 }
.linkish { background:none; border:none; color:#2d7a2d; margin-left:8px; cursor:pointer }

.service-list { display:flex; flex-direction:column; gap:10px }
.service { display:flex; justify-content:space-between; align-items:center }
.service-name { font-weight:600 }
.service-price { color:#2d7a2d; font-weight:700 }

.reviews .review { border-top:1px solid #f1f1f1; padding-top:10px; margin-top:10px }
.review-head { display:flex; justify-content:space-between; align-items:center }
.review-score { background:#f7f7f7; padding:4px 8px; border-radius:8px }

.contact-row { margin:6px 0 }

.gallery-grid { display:grid; grid-template-columns:repeat(2,1fr); gap:8px }
.gallery-grid img { width:100%; height:120px; object-fit:cover; border-radius:8px }

@media (max-width: 900px) {
    .profile-body { flex-direction:column }
    .right-col { width:100% }
}

</style>