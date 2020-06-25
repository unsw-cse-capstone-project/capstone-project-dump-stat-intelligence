import axios from "axios";
import { SERVER_URL } from "../utils/constant";
import paging from "../utils/paging";

const RecipeAPI = {
  search: async (name, page, limit = 10) =>
    axios.get(
      `${SERVER_URL}/ingredients?search=${name}&${paging(limit, page)}`
    ),
  get: async (id) => axios.get(`${SERVER_URL}/ingredients/${id}`),
  create: async (ingredient) => {
    const res = await axios.post(
      `${SERVER_URL}/ingredients`,
      JSON.stringify({ ingredient })
    );
    return res;
  },
};

export default RecipeAPI;
