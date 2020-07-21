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
    return await api.post(`/recipes/`, recipe);
  },
  update: async (id, recipe) => {
    return await api.put(`/recipes/${id}`, recipe);
  },
  delete: async (id) => api.delete(`/recipes/${id}/`),
  discover: async () => {
    return await api.get('/meta/');
  }
};

export default RecipeAPI;
