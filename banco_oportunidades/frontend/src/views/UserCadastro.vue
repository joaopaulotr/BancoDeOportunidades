<template>
  <div class="page-wrapper">
    <div class="cadastro-container">

     
      <div class="branding-side">
        <h2>Bem-vindo ao<br>Conecta Bairro!</h2>
        <p>Complete seu cadastro para começar a se conectar com profissionais e clientes da sua região.</p>
      </div>

     
      <div class="form-side">
        <h2>Cadastrar Usuário</h2>

      
        <div class="stepper">
          <div class="step" :class="{ active: currentStep >= 1 }">1</div>
          <div class="step-line" :class="{ active: currentStep > 1 }"></div>
          <div class="step" :class="{ active: currentStep >= 2 }">2</div>
          <div class="step-line" :class="{ active: currentStep > 2 }"></div>
          <div class="step" :class="{ active: currentStep >= 3 }">3</div>
        </div>

        <form @submit.prevent="UserCadastro">

         
          <fieldset v-if="currentStep === 1">
            <legend>Informações Pessoais</legend>
            <div class="form-group icon-group">
              <i class="fa-solid fa-user"></i>
              <input v-model="usuario.nome" type="text" placeholder="Seu nome completo" />
            </div>
            <div class="form-group icon-group email">
              <i class="fa-solid fa-envelope"></i>
              <input v-model="usuario.email" type="email" placeholder="email@exemplo.com" />
            </div>
            <div class="form-group icon-group senha">
              <i class="fa-solid fa-lock"></i>
              <input v-model="usuario.senha" type="password" placeholder="********" />
            </div>
            <div class="form-group icon-group cpf">
              <i class="fa-solid fa-id-card"></i>
              <input v-model="usuario.cpf_cnpj" type="text" placeholder="000.000.000-00" />
            </div>
          </fieldset>

          
          <fieldset v-if="currentStep === 2">
            <legend>Informações de Contato</legend>
            <div class="form-group icon-group telefone">
              <i class="fa-solid fa-phone"></i>
              <input v-model="usuario.telefone" type="text" placeholder="(00) 00000-0000" />
            </div>
            <div class="form-group icon-group endereco">
              <i class="fa-solid fa-location-dot"></i>
              <input v-model="usuario.endereco" type="text" placeholder="Rua Exemplo, 123" />
            </div>
            <div class="form-group icon-group cidade">
              <i class="fa-solid fa-city"></i>
              <input v-model="usuario.cidade" type="text" placeholder=" Sua cidade" />
            </div>
            <div class="form-group icon-group uf">
              <i class="fa-solid fa-map"></i>
              <input v-model="usuario.uf" type="text" placeholder="PR" />
            </div>
          </fieldset>

         
          <fieldset v-if="currentStep === 3">
            <legend>Tipo de Cadastro</legend>
            <div class="form-group icon-group tipo">
              <i class="fa-solid fa-user-tag"></i>
              <select v-model="usuario.tipoUsuario">
                <option disabled value="">Selecione...</option>
                <option value="cliente">Cliente (buscando serviços)</option>
                <option value="profissional">Profissional (oferecendo serviços)</option>
              </select>
            </div>
          </fieldset>

          <!-- Navegação -->
          <div class="form-navigation">
            <button type="button" class="btn btn-secondary" @click="prevStep" v-if="currentStep > 1">Voltar</button>
            <button type="button" class="btn btn-primary" @click="nextStep" v-if="currentStep < 3">Próximo</button>
            <button type="submit" class="btn btn-primary" v-if="currentStep === 3">Finalizar Cadastro</button>
          </div>
        </form>

        <p v-if="msg" class="message" :class="msg.includes('Erro') ? 'error' : 'success'">{{ msg }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const currentStep = ref(1)
const nextStep = () => { if (currentStep.value < 3) currentStep.value++ }
const prevStep = () => { if (currentStep.value > 1) currentStep.value-- }

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
  if(currentStep.value !== 3) return;

  try {
    const response = await axios.post('http://localhost:8000/usuarios', {...usuario.value, senha_hash: usuario.value.senha})
    msg.value = response.data.msg || 'Cadastro realizado com sucesso!'
  } catch (error) {
    msg.value = error.response?.data?.msg || 'Erro ao cadastrar usuário'
  }
}
</script>

<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css');


.page-wrapper {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #ffffff, #ffffff);
  padding: 2rem;
}

.cadastro-container {
  display: grid;
  grid-template-columns: 1fr;
  max-width: 1100px;
  width: 100%;
  background: #fff;
  border-radius: 24px;
 box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 12px;
  overflow: hidden;
}


.branding-side {
  display: none;
  background: linear-gradient(135deg,#eb5f07,#f18809);
  color: #fff;
  padding: 40px;
  flex-direction: column;
  justify-content: center;
  text-align: left;
}
.branding-side h2 { font-size:2.5rem; font-weight:700; line-height:1.2; margin-bottom:1rem; }
.branding-side p { font-size:1.1rem; opacity:0.9; }


.form-side { padding: 2.5rem; }
.form-side h2 { font-size:2rem; font-weight:700; color:#eb5f07; text-align:center; margin-bottom:24px; }


.stepper { display:flex; align-items:center; justify-content:space-between; margin-bottom:2rem; }
.step { width:30px;height:30px;border-radius:50%;background:#ddd;color:#555;display:flex;align-items:center;justify-content:center;font-weight:700;transition:0.4s; }
.step.active { background:#eb5f07; color:#fff; }
.step-line { flex:1;height:2px;background:#ddd;transition:0.4s; }
.step-line.active { background:#eb5f07; }


fieldset { border:none; padding:0; margin:0; animation: fadeIn 0.4s; }
legend { font-size:1.2rem; font-weight:600; margin-bottom:1rem; }


.icon-group { position: relative; margin-bottom: 1rem; }
.icon-group i {
  position: absolute; top:50%; left:12px; transform: translateY(-50%);
  color:#eb5f07; font-size:1.1rem;
  
}
.icon-group input,
.icon-group select {
  width:100%;
  padding:12px 12px 12px 36px;
  border-radius:22px;
  border:none;
  outline:none;
  font-size: 14px;
  transition: all 0.3s ease;
box-shadow: rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.06) 0px 1px 2px 0px;
}
.icon-group input:focus,
.icon-group select:focus { border-color:#eb5f07; box-shadow:0 5px 15px rgba(226, 215, 209, 0.3); }


.form-navigation { display:flex; justify-content:space-between; margin-top:1.5rem; }
.btn { padding:12px 24px; border:none; border-radius:12px; font-weight:700; font-size:1rem; cursor:pointer; transition:0.3s; box-shadow:0 4px 12px rgba(0,0,0,0.08); }
.btn:hover { transform:translateY(-2px); box-shadow:0 6px 16px rgba(0,0,0,0.12); }
.btn-primary { background:#eb5f07; color:#fff; }
.btn-primary:hover { background:#f18809; }
.btn-secondary { background:#ddd; color:#555; }
.btn-secondary:hover { background:#ccc; }


.message { margin-top:1.5rem; text-align:center; font-weight:600; padding:10px; border-radius:8px; }
.message.error { color:#D8000C; background:#FFD2D2; }
.message.success { color:#4F8A10; background:#DFF2BF; }


@media (min-width:768px) { .cadastro-container { grid-template-columns:1fr 1.2fr; } .branding-side { display:flex; } }


@keyframes fadeIn { from { opacity:0; transform:translateY(10px); } to { opacity:1; transform:translateY(0); } }
</style>
