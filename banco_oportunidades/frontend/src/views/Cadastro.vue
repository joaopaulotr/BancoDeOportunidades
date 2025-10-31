<script setup>
import { onMounted, onUnmounted } from 'vue'

onMounted(() => {
  document.body.classList.add('cadastro-page')
})

onUnmounted(() => {
  document.body.classList.remove('cadastro-page')
})
</script>
<template>
  <div class="card-registro">
<div class="card-welcome">
<div class="row">
  <div class="card-login col-lg" style="font-size: xx-large; font-family: Momo Trust Display; font-weight: 400;font-style: normal;">
    Bem vindo!
  </div>
   <input type="text" placeholder="Email"></input>
    <input type="password" placeholder="Senha"></input>
</div>

</div>
  </div>

</template>
<style>
@import url('https://fonts.googleapis.com/css2?family=Coiny&family=Momo+Trust+Display&display=swap');
body.cadastro-page {
  background-color: #e3e3e9;
  margin: 0;
  padding: 0;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;

}

.card-registro {
  width: 1200px;
  height: 500px;
   background-color: #b9d48b;
 
  border-radius: 15px;
}
.card-welcome{
  width: 400px;
  height: 500px;
   background-color: #d3e4c5;
   border-top-left-radius: 15px;   
  border-bottom-left-radius: 15px;
 display: flex;              
  flex-direction: column;      
  justify-content: center;     
  align-items: center;        
  text-align: center;
  
  color: #ffffff;
}


</style>