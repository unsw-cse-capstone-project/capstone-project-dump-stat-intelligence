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
    meal_cat : [],
    ingredients : [],
    image_URL : "",
    suggest : true,
}



export const createReducer = (state = initialState, action) => {
    switch (action.type) {
        case types.CAT_REMOVE_CREATE:
            let newCat = state[action.category];
            //removing relevant one
            for (let i = 0; i < newCat.length; i++) {
                if (newCat[i].name === action.name) {
                    newCat.splice(i, 1);
                    break;
                }
            }
            return {
                ...state,
                [action.category] : [...newCat]
            }
        case types.CAT_ADD_CREATE:
            newCat = state[action.category];
            newCat.push({name : action.name});
            return {
                ...state,
                [action.category] : [...newCat]
            }
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