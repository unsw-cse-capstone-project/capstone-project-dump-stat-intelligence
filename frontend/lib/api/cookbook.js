import api from "./api";
import paging from "../utils/paging";

const CookbookAPI = {
  get: async (limit, page, token) =>
    await api.get(`/user/cookbook?${paging(limit, page)}`, {
      headers: {
        Authorization: `Token ${token}`,
      },
    }),
  add: async (id, token) =>
    await api.post(`/user/cookbook`, JSON.stringify({ recipeId: id }), {
      headers: {
        Authorization: `Token ${token}`,
      },
    }),
  delete: async (id, token) =>
    await api.delete(`/user/cookbook/${id}`, {
      headers: {
        Authorization: `Token ${token}`,
      },
    }),
};

export default CookbookAPI;
