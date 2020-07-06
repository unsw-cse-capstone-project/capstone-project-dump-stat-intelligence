import axios from "axios";
import { SERVER_URL } from "../utils/constant";
import paging from "../utils/paging";

const PantryAPI = {
  get: async (limit = 10, page = 1, token) =>
    await axios.get(`${SERVER_URL}/user/pantry?${paging(limit, page)}`, {
      headers: {
        Authorization: `Token ${token}`,
      },
    }),
  add: async (ingredient, token) =>
    await axios.post(
      `${SERVER_URL}/user/pantry`,
      JSON.stringify({ ingredient }),
      {
        headers: {
          Authorization: `Token ${token}`,
        },
      }
    ),
  delete: async (id, token) =>
    await axios.delete(`${SERVER_URL}/user/pantry/${id}`, {
      headers: {
        Authorization: `Token ${token}`,
      },
    }),
};

export default PantryAPI;
