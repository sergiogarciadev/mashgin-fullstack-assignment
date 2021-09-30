import { createStore } from 'vuex';
import createPersistedState from 'vuex-persistedstate';
import cart from './modules/cart';
import categories from './modules/categories';
import items from './modules/items';

export default createStore({
  modules: {
    cart,
    categories,
    items,
  },
  plugins: [createPersistedState()],
  strict: true,
});
