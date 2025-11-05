<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
</script>
<template>
  <div class="container text-center">
  <div class="row row-cols-2 row-cols-lg-5 g-2 g-lg-3">
    <div class="col">
      <div class="p-3">
        <div class ="card-jardinagem">

        </div>
      </div>
    </div>
    <div class="col">
      <div class="p-3">Row column</div>
    </div>
    <div class="col">
      <div class="p-3">Row column</div>
    </div>
    <div class="col">
      <div class="p-3">Row column</div>
    </div>
    <div class="col">
      <div class="p-3">Row column</div>
    </div>
    <div class="col">
      <div class="p-3">Row column</div>
    </div>
    <div class="col">
      <div class="p-3">Row column</div>
    </div>
    <div class="col">
      <div class="p-3">Row column</div>
    </div>
    <div class="col">
      <div class="p-3">Row column</div>
    </div>
    <div class="col">
      <div class="p-3">Row column</div>
    </div>
  </div>
</div>
</template>

<style scoped>
.card-jardinagem{
  width: 210px;
  height: 210px;
  border-radius: 20px;
  background-color: rgb(255, 255, 255);
   box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
</style>