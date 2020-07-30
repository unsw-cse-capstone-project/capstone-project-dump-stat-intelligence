import api from "./api";
import paging from "../utils/paging";

const PantryAPI = { 
  get: async (limit = 10, page = 1) =>
    await api.get(`/user/pantry/?${paging(limit, page)}`),
  add: async (ingredient) =>
    await api.post(`/user/pantry/`, ingredient),
  delete: async (id) => await api.delete(`/user/pantry/${id}/`, {}),
  update: async (id, ingredient) => await api.patch(`/user/pantry/${id}/`, ingredient)
};

export default PantryAPI;
