import axios from "axios";
import { SERVER_URL } from "../utils/constant";
import paging from "../utils/paging";

const CookbookAPI = {
  get: async (limit, page, token) =>
    await axios.get(`${SERVER_URL}/user/cookbook?${paging(limit, page)}`, {
      headers: {
        Authorization: `Token ${token}`,
      },
    }),
  add: async (id, token) =>
    await axios.post(
      `${SERVER_URL}/user/cookbook`,
      JSON.stringify({ recipeId: id }),
      {
        headers: {
          Authorization: `Token ${token}`,
        },
      }
    ),
  delete: async (id, token) =>
    await axios.delete(`${SERVER_URL}/user/cookbook/${id}`, {
      headers: {
        Authorization: `Token ${token}`,
      },
    }),
};

export default CookbookAPI;
