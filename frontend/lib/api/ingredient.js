import api from "./api";
import paging from "../utils/paging";

const IngredientAPI = {
  getAll: async () => {
    return await api.get(`/ingredients/`);
  },
  search: async (name, page, limit = 10) =>
    api.get(`/ingredients/?search=${name}&${paging(limit, page)}`),
  get: async (id) => api.get(`/ingredients/${id}/`),
  create: async (ingredient) =>
    await api.post(`/ingredients/`, ingredient),
};

export default IngredientAPI;
