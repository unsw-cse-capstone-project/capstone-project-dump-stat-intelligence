import * as types from "../types";

//NOTE - if id is null, it is assumed the recipe is yet to be added, if its not null then it is being edited.
const initialState = {
    name : "New Recipe",
    id : null,
    cook_time : "",
    ingredients : [],
    method : "",
    author : {
        id : null,
        username : "",

    },
    diet_req : [],
    ingredients : []
}



export const createReducer = (state = initialState, action) => {
    switch (action.type) {
        case types.UPDATE_CREATE:
            
            return {
                ...state,
                [action.category] : action.newVal    
            }
        case types.LOAD_CREATE:
            return {
                ...action.loaded
            }
        case types.CLEAR_CREATE:
            return {
                ...initialState
            }
        default:
            return {
                ...state
            }
    }
}