<template>
  <div class="grid grid-cols-1 gap-5 p-10 sm:grid-cols-1 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-3">
    <CategoryListItem
      v-for="category in categories"
      :category="category"
      :key="category.id"
      @click="selectedCategory = category.id"
    />
  </div>
</template>

<script>
import { mapState } from 'vuex'

import CategoryListItem from './CategoryListItem.vue';

export default {
  created() {
    this.$store.dispatch('categories/getAll');
  },
  computed: mapState({
    categories(state) {
      return state.categories.all;
    },
  }),
  components: {
    CategoryListItem,
  },
};
</script>
