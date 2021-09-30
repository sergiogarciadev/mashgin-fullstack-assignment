import api from '../../api/order';

// initial state
const state = {
  items: {},
};

// getters
const getters = {};

// actions
const actions = {
  add({ commit }, { item_id, quantity }) {
    commit('addItem', { item_id, quantity });
  },
  remove({ commit }, { item_id }) {
    commit('removeItem', { item_id });
  },
  newCart({ commit }) {
    commit('newCart');
  },
  async checkout({ commit, state }, { card, cartItems }) {
    const order = {
      card_number: card.cardNumber.replace(/ /g, ''),
      card_expiry: card.cardExpiry.replace(/ /g, ''),
      card_cvc: card.cardCvc,

      items: cartItems.map((item) => ({
        item_id: item.id,
        quantity: state.items[item.id],
      })),
    };
    await api.addOrder(order)
  },
};

// mutations
const mutations = {
  addItem(state, { item_id, quantity }) {
    state.items[item_id] = quantity;
  },
  removeItem(state, { item_id }) {
    delete state.items[item_id];
  },
  newCart(state) {
    state.items = {};
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
