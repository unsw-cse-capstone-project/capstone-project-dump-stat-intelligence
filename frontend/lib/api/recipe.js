import api from "./api";
import paging from "../utils/paging";

const RecipeAPI = {
  getAll: async (
    meal = "",
    diet = "",
    ingredients = "",
    page = 1,
    limit = 10
  ) => {
    return api.get(`/recipes/`);
  },
  get: async (id) => api.get(`/recipes/${id}/`),
  create: async (recipe) => {
    const res = await api.post(`/recipes/`, JSON.stringify(recipe));
    return res;
  },
  update: async (id, recipe) => {
    const res = await api.put(`/recipes/${id}`, JSON.stringify(recipe));
    return res;
  },
  delete: async (id) => api.delete(`/recipes/${id}/`),
};

export default RecipeAPI;
