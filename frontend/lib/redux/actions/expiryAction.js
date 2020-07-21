import * as types from "../types";
import store from "../store";

//No API, frontend only
export const load_expiry = (name, category, expiry) => async (dispatch) => {
    dispatch({
        type : types.LOAD_EXPIRY,
        name : name,
        category : category,
        expiry : expiry
    })
}

//No API, frontend only
export const clear_expiry = () => async (dispatch) => {
    dispatch({
        type : types.CLEAR_EXPIRY,
    })
}

//NEEDS API
export const change_expiry = (expiry) => async (dispatch) => {
    let ingredient = store.getState().expiry;
    //INSERT API, TELL BACKEND TO UPDATE INGREDIENT
    
    dispatch({
        type : types.CHANGE_EXPIRY,
        expiry : expiry,
    })
}