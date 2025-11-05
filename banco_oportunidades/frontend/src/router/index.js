import { createRouter, createWebHistory } from 'vue-router'
import Cadastro from '../views/Cadastro.vue'
import Home from '../views/Home.vue'
import Servicos from '../views/Servicos.vue'
import Perfil from '../views/Perfil.vue'

const routes = [
  { path: '/', name: 'Cadastro', component: Cadastro },
  { path: '/home', name: 'Home', component: Home },
  { path: '/servicos', name: 'Servicos', component: Servicos },
  { path: '/perfil', name: 'Perfil', component: Perfil }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
 