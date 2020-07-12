import api from "./api";
import paging from "../utils/paging";

const CookbookAPI = {
  get: async (limit, page) =>
    await api.get(`/user/cookbook/?${paging(limit, page)}`),
  add: async (id) =>
    await api.post(`/user/cookbook/`, JSON.stringify({ recipeId: id })),
  delete: async (id) => await api.delete(`/user/cookbook/${id}/`),
};

export default CookbookAPI;
