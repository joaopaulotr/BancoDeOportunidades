<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-white fixed-top">
        <div class="container-fluid d-flex align-items-center justify-content-between">


            <a class="navbar-brand">
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg" class="logo" alt="logo">
            </a>

           <form class="search-center">
  <div class="search-wrapper">
    <input class="form-control search-input" type="search" placeholder="pesquisar...">
    <svg class="search-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0,0,256,256">
      <g fill="#a8a8a8"><g transform="scale(8.53333,8.53333)">
      <path d="M13,3c-5.511,0 -10,4.489 -10,10c0,5.511 4.489,10 10,10c2.39651,0 4.59738,-0.85101 6.32227,-2.26367l5.9707,5.9707c0.25082,0.26124 0.62327,0.36648 0.97371,0.27512c0.35044,-0.09136 0.62411,-0.36503 0.71547,-0.71547c0.09136,-0.35044 -0.01388,-0.72289 -0.27512,-0.97371l-5.9707,-5.9707c1.41266,-1.72488 2.26367,-3.92576 2.26367,-6.32227c0,-5.511 -4.489,-10 -10,-10zM13,5c4.43012,0 8,3.56988 8,8c0,4.43012 -3.56988,8 -8,8c-4.43012,0 -8,-3.56988 -8,-8c0,-4.43012 3.56988,-8 8,-8z"></path>
      </g></g>
    </svg>
  </div>
</form>

            <div class="d-flex align-items-center links-wrapper">
                <ul class="navbar-nav d-flex flex-row">
                    <li class="nav-item me-3">
                        <router-link class="nav-link" to="/home">home</router-link>
                    </li>
                    <li class="nav-item me-3">
                        <router-link class="nav-link" to="/servicos">serviços</router-link>
                    </li>
                </ul>

                <router-link to="/perfil" class="ms-3">
                    <img src="https://cdn-icons-png.flaticon.com/512/847/847969.png" alt="perfil" class="perfil-icon">
                </router-link>
            </div>

        </div>
    </nav>
</template>
<style scoped>
.perfil-icon {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    cursor: pointer;
}

.search-center {
  width: 100%;
  display: flex;
  justify-content: center;
}

.search-wrapper {
  position: relative;
  width: 100%;
  max-width: 450px;
}

.search-input {
  width: 100%;
  padding-right: 40px; 
  padding-left: 22px;
  height: 38px;
  background-color: rgb(248, 248, 248);
  border: none;
  border-radius: 40px;
  color: rgb(226, 226, 226);
}

.search-icon {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  pointer-events: none;
}

.logo {
    width: 40px;
}

.links-wrapper {
    margin-right: 120px;
   
}
</style>
