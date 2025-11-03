<script setup>
import garden2 from '../assets/garden2.png'
import { onMounted, onUnmounted } from 'vue'

onMounted(() => {
  document.body.classList.add('cadastro-page')
})
onUnmounted(() => {
  document.body.classList.remove('cadastro-page')
})
</script>

<template>
  <div class="container-login">
    <div class="login-left">
      <div class="login-box">
        <h1>Bem Vindo!</h1>
        <p class="subtitle" style="font-size: medium;">
         Seu bairro, suas oportunidades. Cadastre-se e encontre serviços perto de você.
        </p>

        <div class="form">
          <div class="input-group">
            <input type="text" id="username" placeholder="Username" />
          </div>
          <div class="input-group">
            <input type="password" id="password" placeholder="Password" />
          </div>

          <a href="#" class="forgot">Esqueceu a senha?</a>
          <button class="btn-login">Login</button>

          <div class="divider">
            <span>ou continue com</span>
          </div>

          <div class="socials">
            <button class="circle-btn">G</button>
            <button class="circle-btn"></button>
            <button class="circle-btn">f</button>
          </div>

          <p class="register">
            Sem cadastro? <a href="#" class="link">Registre-se agora</a>
          </p>
        </div>
      </div>
    </div>

    <div class="login-right">
      <div class="illustration">
  <img :src="garden2" alt="Ilustração" />
        <p>
          Encontre empregos facilmente com <b>Nosso App</b>
        </p>
      </div>
    </div>
  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Coiny&family=Momo+Trust+Display&family=Paytone+One&display=swap');

body.cadastro-page {
  background: linear-gradient(135deg, #c2cfb8 0%, #e3e3e9 100%);
  margin: 0;
  padding: 0;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}


.container-login {
  width: 1150px;
  height: 650px;
  display: flex;
  border-radius: 25px;
  overflow: hidden;
  background: rgba(255, 255, 255, 0.45);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  box-shadow: 0 15px 50px rgba(0, 0, 0, 0.15);
  transition: 0.3s ease;
}


.login-left {
  width: 50%;
  background-color: rgba(255, 255, 255, 0.65);
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-box {
  width: 75%;
  max-width: 430px;
}

h1 {
   font-family: "Paytone One", sans-serif;
  font-weight: 400;
  font-style: normal;
  margin-bottom: 12px;
  color: #000;
}

.subtitle {
  color: #444;
  font-size: 1rem;
  margin-bottom: 35px;
}

.form {
  display: flex;
  flex-direction: column;
  gap: 18px;
}

.input-group input {
  width: 100%;
  height: 48px;
  border-radius: 30px;
  border: 1.5px solid #ccc;
  outline: none;
  padding: 0 18px;
  font-size: 15px;
  background-color: #fafafa;
  transition: 0.2s;
}

.input-group input:focus {
  border-color: #7cb78a;
  box-shadow: 0 0 0 3px rgba(124, 183, 138, 0.3);
  background-color: #fff;
}

.forgot {
  text-align: right;
  font-size: 12px;
  color: #444;
  text-decoration: none;
  margin-top: -10px;
}

.btn-login {
  width: 100%;
  height: 48px;
  border-radius: 30px;
  background-color: #000;
  color: white;
  border: none;
  font-weight: 600;
  cursor: pointer;
  transition: 0.3s;
}

.btn-login:hover {
  opacity: 0.85;
}

.divider {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 22px 0;
  font-size: 12px;
  color: #555;
}

.divider::before,
.divider::after {
  content: "";
  flex: 1;
  height: 1px;
  background-color: #ccc;
  margin: 0 10px;
}

.socials {
  display: flex;
  justify-content: center;
  gap: 18px;
  margin-bottom: 10px;
}

.circle-btn {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  border: none;
  font-size: 18px;
  font-weight: bold;
  cursor: pointer;
  background-color: #000;
  color: white;
  transition: 0.3s;
}

.circle-btn:hover {
  opacity: 0.85;
}

.register {
  text-align: center;
  font-size: 14px;
  color: #444;
}

.link {
  color: #4caf50;
  text-decoration: none;
  font-weight: 500;
}

.link:hover {
  text-decoration: underline;
}


.login-right {
  width: 50%;
  background-color: #e5ebbc;
  display: flex;
  justify-content: center;
  align-items: center;
}

.illustration {
  text-align: center;
  color: #333;
  max-width: 450px;
}

.illustration img {
  width: 350px;
  margin-bottom: 35px;
}

.illustration p {
  font-size: 1.1rem;
  color: #444;
  line-height: 1.5;
}
</style>
