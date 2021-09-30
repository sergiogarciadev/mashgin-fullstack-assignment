import axios from 'axios'

export default {
  async getCategories (cb) {
    const resp = await axios.get('/api/category')
    return resp.data
  },
}
