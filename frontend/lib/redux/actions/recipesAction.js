import * as types from '../types';

import store from "../store";

export const recipes_clear = () => async dispatch => {
    dispatch({
        type : types.RECIPES_CLEAR
    })
}

export const recipes_update = () => async dispatch => {
    
    let explore = store.getState().explore;
    //SEARCH BACKEND WITH THE EXPLORE THING
    
    dispatch({
        type : types.RECIPES_UPDATE,
        recipes : ["bruh"]
    })
}