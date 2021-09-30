<template>
  <div class="grid grid-cols-1 gap-5 p-10 sm:grid-cols-1 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-3">
    <ItemListItem v-for="item in items" :item="item" :key="item.id" />
  </div>
</template>

<script>
import { mapState } from 'vuex'

import ItemListItem from './ItemListItem.vue';

export default {
  created() {
    this.$store.dispatch('items/getAll');
  },
  computed: mapState({
    items(state) {
      return state.items.all.filter(i => i.category_id == this.$route.params.id);
    },
  }),
  components: {
    ItemListItem
  }
};
</script>
