<template>
  <div class="w-1/2 mx-auto text-2xl font-bold">
    <div class="relative overflow-hidden rounded shadow-lg" @click="addToCart">
      <img class="object-cover w-full h-64 hover:filter hover:grayscale" :src="imagePath" :alt="item.name" />
      <div class="absolute bottom-0 w-full pt-2 text-center bg-white bg-opacity-70">
        <div class="mb-2">{{ item.name }}</div>
      </div>
      <div class="absolute top-0 right-0 w-1/3 pt-2 text-center bg-white rounded bg-opacity-70">
        <div class="mb-2">{{ price }}</div>
      </div>
    </div>
    <div class="grid w-1/2 grid-cols-3 gap-5 p-10 mx-auto">
      <button @click="decrease">-</button>
      <input class="text-center" :value="quantity" readonly />
      <button @click="increase">+</button>
    </div>
    <div>
      <button v-if="quantity > 0" class="w-full p-2 text-white bg-blue-800" @click="addToCart">Add</button>
      <button v-if="quantity == 0" class="w-full p-2 text-white bg-red-800" @click="removeFromCart">Remove</button>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import { find } from 'lodash';

export default {
  data() {
    const item = find(this.$store.state.items.all, (i) => i.id == this.$route.params.id);

    return {
      item: item,
      quantity: this.$store.state.cart.items[item.id] || 1,
    };
  },
  computed: mapState({
    imagePath() {
      return `/images/${this.item.image_id}.jpg`;
    },
    price() {
      return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(this.item.price);
    },
  }),
  methods: {
    decrease() {
      if (--this.quantity < 0) {
        this.quantity = 0;
      }
    },
    increase() {
      ++this.quantity;
    },
    async addToCart() {
      await this.$store.dispatch('cart/add', {
        item_id: this.item.id,
        quantity: this.quantity,
      });
      this.$router.push(`/cart`);
    },
    async removeFromCart() {
      await this.$store.dispatch('cart/remove', {
        item_id: this.item.id,
      });
      this.$router.push(`/cart`);
    },
  },
};
</script>
