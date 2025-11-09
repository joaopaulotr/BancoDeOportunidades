<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-orange-100 to-pink-50 p-6">
    <!-- card principal -->
    <div class="bg-gradient-to-tr from-orange-400 to-pink-300 rounded-3xl shadow-2xl w-full max-w-lg p-8 transform transition-transform duration-300 hover:scale-105">
      <h2 class="text-3xl font-bold text-white mb-6 text-center drop-shadow-lg">Cadastrar Usuário</h2>
      
      <form @submit.prevent="UserCadastro" class="space-y-6">

        <!-- seção de informações pessoais -->
        <div class="bg-white rounded-2xl p-5 shadow-md space-y-4">
          <h3 class="font-semibold text-orange-500 mb-2">Informações Pessoais</h3>
          <div class="flex flex-col relative">
            <label class="absolute -top-3 left-3 bg-white px-1 text-sm text-orange-500 font-semibold">Nome</label>
            <input v-model="usuario.nome" type="text" placeholder="Seu nome" class="input-colorful"/>
          </div>
          <div class="flex flex-col relative">
            <label class="absolute -top-3 left-3 bg-white px-1 text-sm text-orange-500 font-semibold">Email</label>
            <input v-model="usuario.email" type="email" placeholder="email@exemplo.com" class="input-colorful"/>
          </div>
          <div class="flex flex-col relative">
            <label class="absolute -top-3 left-3 bg-white px-1 text-sm text-orange-500 font-semibold">Senha</label>
            <input v-model="usuario.senha" type="password" placeholder="********" class="input-colorful"/>
          </div>
          <div class="flex flex-col relative">
            <label class="absolute -top-3 left-3 bg-white px-1 text-sm text-orange-500 font-semibold">CPF / CNPJ</label>
            <input v-model="usuario.cpf_cnpj" type="text" placeholder="000.000.000-00" class="input-colorful"/>
          </div>
        </div>

        <!-- seção de contato -->
        <div class="bg-white rounded-2xl p-5 shadow-md space-y-4">
          <h3 class="font-semibold text-pink-500 mb-2">Contato</h3>
          <div class="flex flex-col relative">
            <label class="absolute -top-3 left-3 bg-white px-1 text-sm text-pink-500 font-semibold">Telefone</label>
            <input v-model="usuario.telefone" type="text" placeholder="(00) 00000-0000" class="input-colorful"/>
          </div>
          <div class="flex flex-col relative">
            <label class="absolute -top-3 left-3 bg-white px-1 text-sm text-pink-500 font-semibold">Endereço</label>
            <input v-model="usuario.endereco" type="text" placeholder="Rua Exemplo, 123" class="input-colorful"/>
          </div>
          <div class="flex flex-col relative">
            <label class="absolute -top-3 left-3 bg-white px-1 text-sm text-pink-500 font-semibold">Cidade</label>
            <input v-model="usuario.cidade" type="text" placeholder="Cidade" class="input-colorful"/>
          </div>
          <div class="flex flex-col relative">
            <label class="absolute -top-3 left-3 bg-white px-1 text-sm text-pink-500 font-semibold">UF</label>
            <input v-model="usuario.uf" type="text" placeholder="SP" class="input-colorful"/>
          </div>
        </div>

        <!-- seção tipo de usuário -->
        <div class="bg-white rounded-2xl p-5 shadow-md space-y-2">
          <label class="font-semibold text-purple-500">Tipo de usuário</label>
          <select v-model="usuario.tipoUsuario" class="input-colorful">
            <option disabled value="">Selecione...</option>
            <option value="cliente">Cliente</option>
            <option value="profissional">Profissional</option>
          </select>
        </div>

        <button type="submit" class="w-full py-3 rounded-xl bg-purple-500 text-white font-bold text-lg hover:bg-purple-600 transition-all duration-300 shadow-lg hover:shadow-xl">
          Cadastrar
        </button>
      </form>

      <p v-if="msg" class="mt-5 text-center text-red-600 font-semibold">{{ msg }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const usuario = ref({
  nome: '',
  email: '',
  senha: '',
  cpf_cnpj: '',
  tipoUsuario: '',
  telefone: '',
  endereco: '',
  cidade: '',
  uf: ''
})

const msg = ref('')

const UserCadastro = async () => {
  try {
    const response = await axios.post('http://localhost:8000/usuarios', {
      ...usuario.value,
      senha_hash: usuario.value.senha
    })
    msg.value = response.data.msg
  } catch (error) {
    msg.value = error.response?.data?.msg || 'Erro ao cadastrar usuário'
  }
}
</script>

<style>
.input-colorful {
  padding: 12px 15px;
  border-radius: 10px;
  border: 1px solid #e5e5e5;
  outline: none;
  transition: all 0.3s ease;
  box-shadow: 0 3px 6px rgba(0,0,0,0.08);
}
.input-colorful:focus {
  border-color: #eb5f07;
  box-shadow: 0 5px 15px rgba(235,95,7,0.3);
}
</style>
