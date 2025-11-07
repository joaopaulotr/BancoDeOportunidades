<template>
  <nav class="navbar fixed-top">
    <div class="nav-content">

      
      <router-link to="/home" class="logo-wrap">
        <img src="https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg" class="logo" alt="logo">
      </router-link>

      
      <form class="search-start">
        <div class="search-wrapper">
          <input class="search-input" type="search" placeholder="pesquisar...">
          <svg class="search-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0,0,256,256">
            <g fill="#a8a8a8"><g transform="scale(8.53333,8.53333)">
            <path d="M13,3c-5.511,0 -10,4.489 -10,10c0,5.511 4.489,10 10,10c2.39651,0 4.59738,-0.85101 6.32227,-2.26367l5.9707,5.9707c0.25082,0.26124 0.62327,0.36648 0.97371,0.27512c0.35044,-0.09136 0.62411,-0.36503 0.71547,-0.71547c0.09136,-0.35044 -0.01388,-0.72289 -0.27512,-0.97371l-5.9707,-5.9707c1.41266,-1.72488 2.26367,-3.92576 2.26367,-6.32227c0,-5.511 -4.489,-10 -10,-10zM13,5c4.43012,0 8,3.56988 8,8c0,4.43012 -3.56988,8 -8,8c-4.43012,0 -8,-3.56988 -8,-8c0,-4.43012 3.56988,-8 8,-8z"/>
            </g></g>
          </svg>
        </div>
      </form>

      <div class="nav-links">
        <router-link to="/home">home</router-link>
        <router-link to="/servicos">serviços</router-link>
        <a href="#categorias-sec">categorias</a>
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
  box-shadow: 0 2px 12px rgba(0,0,0,.08);
  padding: 10px 0;
}

.nav-content {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 45px;
}

.logo {
  width: 38px;
  cursor: pointer;
}

.search-start {
  flex: 1;
  display: flex;
  justify-content: start;
  margin-left: 40px;
}

.search-wrapper {
  position: relative;
  width: 100%;
  max-width: 420px;
}

.search-input {
  width: 100%;
  padding: 8px 40px 8px 18px;
  border-radius: 40px;
  border: none;
  background: #f4f4f4;
  font-size: 14px;
}

.search-icon {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
}

.nav-links {
  display: flex;
  gap: 18px;
  align-items: center;
}

.nav-links a, .nav-links .router-link-active, .nav-links .router-link-exact-active {
  font-size: 16px;
  color: #1b1b1b;
  text-transform: lowercase;
  text-decoration: none;
}

.nav-links a:hover {
  color: #000;
}

.perfil-icon {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  cursor: pointer;
}
</style>
