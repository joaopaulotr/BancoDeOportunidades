
<template>
  <nav class="navbar fixed-top">
    <div class="nav-content">

      
      <router-link to="/home" class="logo-wrap">
        <img src="https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg" class="logo" alt="logo">
      </router-link>

      
      <form class="search-start">
        <div class="search-wrapper">
          <input class="search-input" type="search" placeholder="Pesquisar . . ."   v-model="busca">
          <div class="circulo-search"><svg class="search-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0,0,256,256">
            <g fill="#ffffff"><g transform="scale(8.53333,8.53333)">
            <path d="M13,3c-5.511,0 -10,4.489 -10,10c0,5.511 4.489,10 10,10c2.39651,0 4.59738,-0.85101 6.32227,-2.26367l5.9707,5.9707c0.25082,0.26124 0.62327,0.36648 0.97371,0.27512c0.35044,-0.09136 0.62411,-0.36503 0.71547,-0.71547c0.09136,-0.35044 -0.01388,-0.72289 -0.27512,-0.97371l-5.9707,-5.9707c1.41266,-1.72488 2.26367,-3.92576 2.26367,-6.32227c0,-5.511 -4.489,-10 -10,-10zM13,5c4.43012,0 8,3.56988 8,8c0,4.43012 -3.56988,8 -8,8c-4.43012,0 -8,-3.56988 -8,-8c0,-4.43012 3.56988,-8 8,-8z"/>
            </g></g>
          </svg></div>
          
        </div>
      </form>

      <div class="nav-links">
        <router-link to="/home">home</router-link>
        <a href="#categorias-sec">categorias</a>
         <a href="#como-funciona">contratar</a>
        <a href="#sou-profissional">sou profissional</a>
      <router-link to="/perfil">
        <img src="https://img.icons8.com/fluency-systems-regular/48/user-male-circle--v1.png" alt="perfil" class="perfil-icon">
      </router-link>    </div>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  background: #fff;
  box-shadow: 0 4px 12px rgba(0,0,0,.08);
  padding: 12px 0;
  font-family: "Lexend", sans-serif;
}

.nav-content {
  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 45px;
}

.logo {
  width: 38px;
  cursor: pointer;
  transition: transform 0.2s ease;
}

.logo:hover {
  transform: scale(1.05);
}

.search-start {
  flex: 1;
  display: flex;
  justify-content: start;
  margin-left: 40px;
  margin-right: 40px;
}

.search-wrapper {
  position: relative;
  width: 100%;
  max-width: 480px;
}

.search-input {
  width: 100%;
  height: 46px;
  padding: 8px 50px 9px 22px;
  border-radius: 40px;
  border: 1px solid #e5e7eb;
  background: #f8f9fa;
  font-size: 15px;
  font-family: "Lexend", sans-serif;
  font-weight: 400;
  color: #131452;
  transition: all 0.2s ease;
}

.search-input:focus {
  background: #fff;
  border-color: #eb5f07;
  box-shadow: 0 0 0 4px rgba(235, 95, 7, 0.15);
  outline: none; 
}

.search-input::placeholder {
  color: #9ca3af;
  font-weight: 300;
}


.circulo-search {
  position: absolute;
  right: 6px;
  top: 50%;
  transform: translateY(-50%);
  width: 34px; 
  height: 34px;
  border-radius: 50%;
  background-color: #eb5f07;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
}

.circulo-search:hover {
  background-color: #d45506;
  transform: translateY(-50%) scale(1.05);
}

.search-icon {
  width: 18px;
  height: 18px;
  fill: #ffffff; 
}

.nav-links {
  display: flex;
  gap: 32px;
  align-items: center;
}

.nav-links a {
  font-size: 15px;
  color: #131452;
  text-decoration: none;
  font-weight: 500;
  text-transform: capitalize;
  transition: color 0.2s ease;
}

.nav-links a:hover {
  color: #eb5f07;
}

.nav-links .router-link-active {
  color: #eb5f07;
  font-weight: 600;
}

.nav-links a[href="#sou-profissional"] {
  color: #eb5f07;
  font-weight: 600;
}

.perfil-icon {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  cursor: pointer;
  opacity: 0.8;
  transition: opacity 0.2s ease;
  padding: 1px;
}

.perfil-icon:hover {
  opacity: 1;
}
</style>
