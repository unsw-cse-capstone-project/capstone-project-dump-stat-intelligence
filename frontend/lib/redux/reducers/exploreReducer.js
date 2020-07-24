import * as types from "../types";

const initialState = {
    ingredients : [],
    filters : {
        meal : {
            Breakfast : false,
            Lunch : false,
            Dinner : false,
            Snack : false,
            Dessert : false,
            Brunch : false
        },
        diet : {
            Vegan : false,
            Vegetarian : false,
            "Gluten-free" : false,
            "Dairy-free" : false

        }
    }
}

export const exploreReducer = (state = initialState, action) => {
    switch(action.type) {
        case types.FILTER_UPDATE:
            let newFilter = state.filters;
            newFilter[action.category][action.name] = action.status;
            return {
                ...state,
                filters : {
                    ...newFilter
                }
            }

        case types.FILTER_CLEAR:
            return {
                ...state, 
                filters : {
                    ...initialState.filters
                }
            }
        case types.EXPLORE_ALL:
            return {
                ...state,
                ingredients : action.newList
            }
        case types.EXPLORE_ADD:
            let idx = state.ingredients.indexOf(action.toAdd);
            let tempList = [...state.ingredients]
            if (idx === -1) {
                tempList.push(action.toAdd);
            }
            return {
                ...state,
                ingredients : tempList
            }
        case types.EXPLORE_REMOVE:
            idx = state.ingredients.indexOf(action.toRemove);
            tempList = [...state.ingredients]
            if (idx !== -1 ) {
                tempList.splice(idx, 1);
            }
            return {
                ...state,
                ingredients : tempList
            }
        case types.EXPLORE_CLEAR:
            return initialState
        default:
            return state
    }
}