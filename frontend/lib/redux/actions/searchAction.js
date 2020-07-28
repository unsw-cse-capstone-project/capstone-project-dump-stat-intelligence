import * as types from "../types";
import IngredientAPI from "../../api/ingredient";
import store from "../store";

/*
SEARCH

    Holds the redux state for the search query to add a new ingredient to running list. 
    IMPORTANTLY, can hold results from pantry only and also backend

    search : {
        searchString : "String they are entering",
        results : [{ingredient}, {}, {}, ...],
        pantryOnly : bool
    }

*/
export const search_type = (pantryOnly) => async dispatch => {
    dispatch({
        type: types.SEARCH_TYPE,
        pantryOnly : pantryOnly
    })
}


export const update_search = (query) => async dispatch => {
    const pantryOnly = store.getState().search.pantryOnly;
    let match = [];
    if (query === "") {
        //WANT EMPTY QUERY
    } else if (pantryOnly) {
        const pantryIngredients = store.getState().pantry.meta
        var val;
        for (val of pantryIngredients) {
            if (val.startsWith(query)) {
                match.push({name : val});
            }
        }
    } else {

        const ingredients = await IngredientAPI.getAll();
    
        
    
        var i;
        for(i = 0; i < ingredients.data.length; i++) {
            if (ingredients.data[i].name.startsWith(query))
                match.push({name: ingredients.data[i].name, category: ingredients.data[i].category.name});
        }
    }

    dispatch({
        type : types.SEARCH,
        query : query,
        results: match.slice(0,10),
    })
}


export const clear_search = () => async dispatch => {
    dispatch({
        type : types.CLEAR_SEARCH
    })
}