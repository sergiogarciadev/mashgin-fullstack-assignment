<template>
  <router-view />
  <div>
    <router-link to="/categories">
      <div class="absolute w-12 h-12 bottom-12 left-12">
        <HomeIcon class="text-blue-500" />
      </div>
    </router-link>
    <router-link v-if="cartSize > 0" to="/cart">
      <div class="absolute w-12 h-12 bottom-12 right-12">
        <ShoppingCartIcon class="text-blue-500" />
        <div
          class="absolute top-0 right-0 w-6 h-6 pt-1 text-xs font-bold text-center text-white bg-red-600 rounded-full"
        >
          {{ cartSize }}
        </div>
      </div>
    </router-link>
  </div>
</template>

<script>
import { HomeIcon } from '@heroicons/vue/solid';
import { ShoppingCartIcon } from '@heroicons/vue/solid';

import { sum } from 'lodash';

export default {
  computed: {
    cartSize() {
      return sum(Object.values(this.$store.state.cart.items));
    },
  },
  components: {
    HomeIcon,
    ShoppingCartIcon,
  },
};
</script>
