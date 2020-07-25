import * as types from "../types";
import store from "../store";

/*
EXPLORE

    Holds the redux state for the running list

    explore : {
        ingredients : ["ingredient primary key", "", "", ...],
        meals : ["lunch", ...],
        
    }

    NOTE: Doesn't need API currently as search is activated with search button

*/

export const filter_clear = () => async (dispatch) => {
  dispatch({
    type: types.FILTER_CLEAR,
  });
};

export const filter_update = (category, name, status) => async (dispatch) => {
  dispatch({
    type: types.FILTER_UPDATE,
    category: category,
    name: name,
    status: status,
  });
};

export const explore_add = (toAdd) => async (dispatch) => {
  dispatch({
    type: types.EXPLORE_ADD,
    toAdd: toAdd,
  });
};

export const explore_remove = (toRemove) => async (dispatch) => {
  dispatch({
    type: types.EXPLORE_REMOVE,
    toRemove: toRemove.ingredient,
  });
};

export const explore_all = () => async (dispatch) => {
  //Add all the ingredients in the pantry to the running list
  let pantry = store.getState().pantry;
  let newList = [];
  let i = 0;
  Object.keys(pantry).map((key) => {
    if (key !== "meta") {
      for (i = 0; i < pantry[key].length; i++) {
        newList.push(pantry[key][i].name);
      }
    }
  });
  dispatch({
    type: types.EXPLORE_ALL,
    newList: newList,
  });
};

export const explore_clear = () => async (dispatch) => {
  //Do we do the recipeList here as well? something to consider
  dispatch({
    type: types.EXPLORE_CLEAR,
  });
};
