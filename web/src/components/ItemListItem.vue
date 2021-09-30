<template>
  <div
    class="relative z-0 overflow-hidden text-2xl font-bold transition-all rounded shadow-lg cursor-pointer hover:transform hover:scale-110 hover:z-10"
    @click="addToCart"
  >
    <img class="object-cover w-full h-96 hover:filter hover:grayscale" :src="imagePath" :alt="item.name" />
    <div class="absolute bottom-0 w-full pt-2 text-center bg-white bg-opacity-70">
      <div class="mb-2">{{ item.name }}</div>
    </div>
    <div class="absolute top-0 right-0 w-1/3 pt-2 text-center bg-white rounded bg-opacity-70">
      <div>{{ price }}</div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['item'],
  computed: {
    imagePath() {
      return `/images/${this.item.image_id}.jpg`;
    },
    price() {
      return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(this.item.price);
    },
  },
  methods: {
    addToCart() {
      this.$router.push(`/addToCart/${this.item.id}`)
    },
  },
};
</script>
