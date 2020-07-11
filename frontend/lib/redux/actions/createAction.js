import * as types from "../types";

import store from "../store";
import RecipeAPI from "../../api/recipe";

/*
CREATE

    Holds the redux state for the creation and edit of recipes
    create : {
        title : string,
        id : int,
        cook_time : string,
        ingredients : [{}, {}, ...],
        method : [string, string, ...]
    }


*/
//NO API, frontend only
export const update_create = (category, newVal) => async (dispatch) => {
  dispatch({
    type: types.UPDATE_CREATE,
    category: category,
    newVal: newVal,
  });
};

//NEEDS API
export const save_create = () => async (dispatch) => {
  let recipe = store.getState().create;
  //INSERT API, send to backend to add recipe
  RecipeAPI.create(recipe, "")
    .then((res) => {
      // do something
    })
    .catch((err) => {
      console.error(err.response);
    });

  //TODO: might need to update state locally rather than request user's owned reicpes again?
  dispatch({
    type: types.CLEAR_CREATE, //Just removing all left over info
  });
};

//NO API, frontend only
export const clear_create = () => async (dispatch) => {
  dispatch({
    type: types.CLEAR_CREATE,
  });
};

//NEEDS API
export const load_create = (id) => async (dispatch) => {
  let uid = store.getState().auth.uid;
  //INSERT API - actually load recipe from backend instead of dummy data
  
  //TEMPORARY ... LOAD RECIPE LIKE WHEN YOU VEIW A RECIPE
  let recipe = null
  RecipeAPI.get(id).then(({ data }) => {recipe = data}).then(() => {
    dispatch({
      type: types.LOAD_CREATE,
      loaded: recipe,
    })}
  )

};
