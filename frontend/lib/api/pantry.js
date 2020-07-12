import api from "./api";
import paging from "../utils/paging";

const PantryAPI = {
  get: async (limit = 10, page = 1, token) =>
    await api.get(`/user/pantry?${paging(limit, page)}`),
  add: async (ingredient, token) =>
    await api.post(`/user/pantry`, JSON.stringify({ ingredient })),
  delete: async (id, token) => await api.delete(`/user/pantry/${id}`, {}),
};

export default PantryAPI;
