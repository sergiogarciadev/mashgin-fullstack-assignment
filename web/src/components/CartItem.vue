<template>
  <div
    class="relative mt-2 overflow-hidden text-2xl font-bold rounded shadow-lg"
    @click="addToCart"
  >
    <img class="object-cover w-32 h-32 hover:filter hover:grayscale" :src="imagePath" :alt="item.name" />
    <div class="absolute text-left top-2 left-36">{{ item.name }}</div>
    <div class="absolute text-right bottom-2 right-2">{{ quantity}} x {{ price }} = {{ totalPrice }}</div>
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
    quantity() {
      return this.$store.state.cart.items[this.item.id]
    },
    totalPrice() {
      return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(this.item.price * this.quantity);
    }
  },
};
</script>
