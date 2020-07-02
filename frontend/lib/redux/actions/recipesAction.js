import * as types from '../types';

import store from "../store";

/*
RECIPES

    Holds the redux state for the recipes on the explore page
    (currently a dict cause if we want to do pagination could lazy load extra pages to dict)
    recipes : {
        recipes : [{recipe}, {recipe}, ...]
    }


*/


//NO API, MAY NOT EVEN BE NECESSARY
export const recipes_clear = () => async dispatch => {
    dispatch({
        type : types.RECIPES_CLEAR
    })
}

//NEEDS API, NEW SEARCH 
export const recipes_update = () => async dispatch => {
    //explore = ["ingredient primary key", "", ""]
    let explore = store.getState().explore;
    
    //INSERT API - TAKE EXPLORE LIST AND TURN INTO RESULTANT RECIPES
    
    let result = [
        {name : "example"}
    ]
    
    dispatch({
        type : types.RECIPES_UPDATE,
        recipes : [{name : "bruh"}]
    })
}