import { createRouter, createWebHistory } from 'vue-router'
import Cadastro from '../views/Cadastro.vue'
import Home from '../views/Home.vue'
import Servicos from '../views/Servicos.vue'

const routes = [
  { path: '/', name: 'Cadastro', component: Cadastro },
  { path: '/home', name: 'Home', component: Home },
  { path: '/servicos', name: 'Servicos', component: Servicos }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
 