import axios from "axios";
import { SERVER_URL } from "../utils/constant";
import paging from "../utils/paging";

const RecipeAPI = {
  getAll: async (
    meal = "",
    diet = "",
    ingredients = "",
    page = 1,
    limit = 10
  ) => {
    console.log("getting");
    // return axios.get(
    //   `${SERVER_URL}/recipes?meal=${meal}&diet=${diet}&ingredients=${ingredients}&${paging(
    //     limit,
    //     page
    //   )}`
    // );
    return axios.get(`${SERVER_URL}/recipes/`);
  },
  get: async (id) => axios.get(`${SERVER_URL}/recipes/${id}`),
  create: async (recipe, token) => {
    // TODO: token could be implemented at an axios level
    const res = await axios.post(
      `${SERVER_URL}/recipes`,
      JSON.stringify({ recipe }),
      { headers: { Authorization: `Token ${token}` } }
    );
    return res;
  },
  update: async (id, recipe, token) => {
    const res = await axios.put(
      `${SERVER_URL}/recipes/${id}`,
      JSON.stringify({ recipe }),
      { headers: { Authorization: `Token ${token}` } }
    );
    return res;
  },
  delete: async (id, token) =>
    axios.delete(`${SERVER_URL}/recipes/${id}`, {
      headers: { Authorization: `Token ${token}` },
    }),
};

export default RecipeAPI;
